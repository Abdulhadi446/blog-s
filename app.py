from flask import Flask, render_template, abort, request, url_for, flash, redirect, session, send_from_directory, Response
from datetime import datetime, timedelta
from urllib.parse import quote
from xml.sax.saxutils import escape as xml_escape, quoteattr as xml_quoteattr
import os
import json
import re
import math
import shutil
import struct
import csv
import fcntl
import time
import tempfile
from contextlib import contextmanager
from markdown import markdown as render_markdown
from functools import wraps

def create_app(config_name=None):
    app = Flask(__name__)
    
    from config import config
    config_name = config_name or os.environ.get('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    BLOGS_DIR = os.path.expanduser('~/blog-s/blogs')
    os.makedirs(BLOGS_DIR, exist_ok=True)
    
    # CSV file path for subscriber management (hidden in blog directory)
    SUBSCRIBER_CSV_PATH = os.path.join(BLOGS_DIR, '.subscribers.csv')

    def get_site_base():
        """Canonical site base URL: configured SITE_URL, else request root."""
        configured = app.config['SITE_CONFIG']['url'].rstrip('/')
        if configured:
            return configured
        base = request.url_root.rstrip('/')
        host = request.host.split(':')[0]
        is_local = host in ('localhost', '127.0.0.1', '0.0.0.0', '::1')
        if not is_local and base.startswith('http://'):
            base = 'https://' + base[len('http://'):]
        return base

    @app.context_processor
    def inject_site_config():
        seo = {
            'site_name': app.config['SITE_CONFIG']['name'],
            'site_description': app.config['SITE_CONFIG']['description'],
            'site_url': get_site_base(),
            'site_logo': app.config['SITE_CONFIG']['logo'],
            'current_year': app.config['SITE_CONFIG']['current_year'],
        }
        return {'site': app.config['SITE_CONFIG'], 'seo': seo, 'is_admin': session.get('admin')}

    def login_required(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get('admin'):
                return redirect(url_for('admin_login', next=request.url))
            return f(*args, **kwargs)
        return decorated_function

    def get_admin_password():
        try:
            with open('pass.txt', 'r') as f:
                return f.read().strip()
        except FileNotFoundError:
            return ''

    def _slug_key(value):
        """Normalize a slug for case/format-insensitive matching."""
        return re.sub(r'[^a-z0-9]+', '-', str(value).lower()).strip('-')

    def _post_exists(slug):
        return os.path.isfile(os.path.join(BLOGS_DIR, slug, 'blog.md'))

    @app.before_request
    def normalize_trailing_slash():
        """301 trailing-slash variants to their canonical no-slash URL."""
        if request.method not in ('GET', 'HEAD'):
            return None
        path = request.path
        if path == '/' or not path.endswith('/'):
            return None
        if path.startswith('/static/') or path.startswith('/blogs/') or path.startswith('/admin'):
            return None
        target = path.rstrip('/')
        if request.query_string:
            target += '?' + request.query_string.decode('utf-8', 'ignore')
        return redirect(target, code=301)

    @app.route('/admin')
    @app.route('/admin/')
    def admin_root():
        """Keep the admin area unlisted: bare /admin looks like any missing page."""
        abort(404)

    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if request.method == 'POST':
            password = request.form.get('password', '')
            stored = get_admin_password()
            if stored and password == stored:
                session['admin'] = True
                next_page = request.args.get('next')
                return redirect(next_page or url_for('index'))
            flash('Invalid password', 'error')
        return render_template('admin_login.html')

    @app.route('/admin/logout')
    def admin_logout():
        session.pop('admin', None)
        return redirect(url_for('index'))

    @app.route('/blogs/<slug>/image.png')
    def blog_image(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        image_path = os.path.join(post_dir, 'image.png')
        if os.path.exists(image_path):
            return send_from_directory(post_dir, 'image.png', mimetype='image/png')
        abort(404)

    @app.route('/blogs/<slug>/video.mp4')
    def blog_video(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        video_path = os.path.join(post_dir, 'video.mp4')
        if os.path.exists(video_path):
            response = send_from_directory(post_dir, 'video.mp4', mimetype='video/mp4')
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Cache-Control'] = 'public, max-age=3600'
            return response
        abort(404)

    @app.route('/video.mp4')
    def latest_video():
        # Serve the newest post that actually has a video, so this stable
        # alias never 404s just because the latest post is text-only.
        for post in get_all_posts():
            post_dir = os.path.join(BLOGS_DIR, post['slug'])
            video_path = os.path.join(post_dir, 'video.mp4')
            if os.path.exists(video_path):
                response = send_from_directory(post_dir, 'video.mp4', mimetype='video/mp4')
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Cache-Control'] = 'public, max-age=3600'
                return response
        abort(404)


    @app.route('/blogs/<slug>/blog.md')
    def blog_markdown(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        md_path = os.path.join(post_dir, 'blog.md')
        if not os.path.exists(md_path):
            abort(404)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        response = app.make_response(content)
        response.headers['Content-Type'] = 'text/markdown; charset=utf-8'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Cache-Control'] = 'public, max-age=3600'
        response.headers['X-Robots-Tag'] = 'noindex, nofollow'
        return response

    # --- File System Blog Logic ---
    def parse_blog_file(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Basic frontmatter parser (--- metadata --- content)
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                meta_raw = parts[1]
                body = parts[2].strip()
                meta = {}
                for line in meta_raw.strip().split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        v = v.strip().strip('"').strip("'")
                        meta[k.strip().lower()] = v
                return meta, body
        return {}, content

    def get_all_posts():
        posts = []
        if not os.path.exists(BLOGS_DIR):
            return posts
        
        for slug in os.listdir(BLOGS_DIR):
            post_dir = os.path.join(BLOGS_DIR, slug)
            if os.path.isdir(post_dir):
                md_path = os.path.join(post_dir, 'blog.md')
                if os.path.exists(md_path):
                    meta, body = parse_blog_file(md_path)
                    author = meta.get('author', 'Anonymous')
                    published_date = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
                    modified_date = meta.get('updated') or meta.get('modified_date') or meta.get('last_modified') or meta.get('modified') or published_date
                    posts.append({
                        'slug': slug,
                        'title': meta.get('title', slug.replace('-', ' ').title()),
                        'meta_title': meta.get('meta_title', meta.get('title', slug.replace('-', ' ').title())),
                        'description': meta.get('description', ''),
                        'author': author,
                        'author_slug': author.lower().replace(' ', '-'),
                        'published_date': published_date,
                        'modified_date': modified_date,
                        'featured_image': f'/blogs/{slug}/image.png' if os.path.exists(os.path.join(post_dir, 'image.png')) else None,
                        'image_alt': meta.get('image_alt', ''),
                        'content': body,
                        'tags': meta.get('tags', ''),
                        'keywords': meta.get('keywords', '')
                    })
        # Sort by date descending
        return sorted(posts, key=lambda x: x['published_date'], reverse=True)

    # --- AI news archives: daily, weekly (Mondays), monthly (the 1st) ---

    def _parse_post_date(value):
        try:
            return datetime.strptime(str(value)[:10], '%Y-%m-%d')
        except (ValueError, TypeError):
            return None

    def _is_ai_news(post):
        """True for posts that belong in the AI news archive."""
        haystack = ' '.join(str(post.get(k, '')) for k in
                            ('slug', 'title', 'description', 'tags', 'keywords')).lower()
        slug = str(post.get('slug', '')).lower()
        return ('ai-news' in slug
                or re.match(r'^\d{4}-\d{2}-\d{2}-', slug) is not None
                or 'ai news' in haystack
                or 'ai daily roundup' in haystack
                or 'technews' in haystack)

    def _tag_set(value):
        """Normalized tag set, used for search and related posts."""
        return {t.strip().lower() for t in str(value or '').split(',') if t.strip()}

    def _plain_text(value):
        """Strip the small amount of Markdown that appears in FAQ answers."""
        text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', str(value or ''))
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'[*_`]', '', text)
        text = re.sub(r'(^|\s)[>#]{1,6}\s*', r'\1', text)
        text = re.sub(r'(^|\s)[-*+]\s+', r'\1', text)
        return re.sub(r'\s+', ' ', text).strip()

    def _extract_faq(markdown_text):
        """Pull question/answer pairs out of a post's FAQ section."""
        lines = str(markdown_text or '').splitlines()
        start = None
        for i, line in enumerate(lines):
            if re.match(r'^#{2,3}\s+(faq|frequently asked questions)\s*$',
                        line.strip(), re.IGNORECASE):
                start = i + 1
                break
        if start is None:
            return []

        items = []
        question = None
        answer = []
        for line in lines[start:]:
            if re.match(r'^##\s+', line.strip()):
                break
            heading = re.match(r'^#{3,4}\s+(.+?)\s*$', line.strip())
            if heading:
                if question and answer:
                    items.append({'question': _plain_text(question),
                                  'answer': _plain_text(' '.join(answer))})
                question = heading.group(1)
                answer = []
            elif question and line.strip():
                answer.append(line.strip())
        if question and answer:
            items.append({'question': _plain_text(question),
                          'answer': _plain_text(' '.join(answer))})
        return [item for item in items if item['question'] and item['answer']]

    def _png_size(path):
        """Read PNG dimensions from the IHDR chunk, without Pillow."""
        try:
            with open(path, 'rb') as image_file:
                header = image_file.read(24)
            if len(header) == 24 and header[:8] == b'\x89PNG\r\n\x1a\n':
                return struct.unpack('>II', header[16:24])
        except (OSError, struct.error):
            pass
        return (1200, 630)

    SUBSCRIBER_LOCK_PATH = os.path.join(BLOGS_DIR, '.subscribers.lock')
    SUBSCRIBER_LOCK_TIMEOUT = 5.0  # seconds

    @contextmanager
    def _subscribers_lock():
        """Advisory file lock around read-modify-write cycles on the CSV.

        Survives multiple gunicorn workers because flock is per-process.
        Blocks until the lock is free or times out with TimeoutError.
        """
        lock_fd = os.open(SUBSCRIBER_LOCK_PATH, os.O_CREAT | os.O_RDWR, 0o600)
        deadline = time.monotonic() + SUBSCRIBER_LOCK_TIMEOUT
        try:
            while True:
                try:
                    fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    break
                except BlockingIOError:
                    if time.monotonic() >= deadline:
                        raise TimeoutError('Timed out waiting for subscriber lock')
                    time.sleep(0.05)
            yield
        finally:
            try:
                fcntl.flock(lock_fd, fcntl.LOCK_UN)
            finally:
                os.close(lock_fd)

    def _load_subscribers():
        """Load subscriber rows from CSV. Returns list of dicts {email, subscribed_at}."""
        try:
            if os.path.exists(SUBSCRIBER_CSV_PATH):
                with open(SUBSCRIBER_CSV_PATH, 'r', newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    return [
                        {'email': row.get('email', '').strip().lower(),
                         'subscribed_at': row.get('subscribed_at', '') or datetime.now().isoformat()}
                        for row in reader if row.get('email')
                    ]
        except (IOError, csv.Error, UnicodeDecodeError) as e:
            app.logger.warning(f"Failed to read subscriber CSV: {e}")
        return []

    def _save_subscribers(rows):
        """Atomically write subscriber rows to CSV. Never leaves a partial file on disk."""
        directory = os.path.dirname(SUBSCRIBER_CSV_PATH)
        os.makedirs(directory, exist_ok=True)
        fd, tmp_path = tempfile.mkstemp(dir=directory, prefix='.subscribers-', suffix='.tmp')
        try:
            with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['email', 'subscribed_at'])
                writer.writeheader()
                for row in rows:
                    writer.writerow({'email': row['email'],
                                     'subscribed_at': row.get('subscribed_at') or datetime.now().isoformat()})
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_path, SUBSCRIBER_CSV_PATH)
            app.logger.info(f"Subscriber CSV updated: {len(rows)} total")
        except (IOError, csv.Error) as e:
            app.logger.error(f"Failed to write subscriber CSV: {e}")
            raise
        finally:
            if os.path.exists(tmp_path):
                try:
                    os.unlink(tmp_path)
                except OSError:
                    pass

    def _email_is_valid(email):
        """Basic email format validation."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email.strip()) is not None

    def _add_subscriber(email):
        """Add an email to the subscriber list. Returns (success, message)."""
        email = email.strip().lower()
        if not _email_is_valid(email):
            return False, 'Please enter a valid email address.'
        try:
            with _subscribers_lock():
                subscribers = _load_subscribers()
                if any(s['email'] == email for s in subscribers):
                    return False, 'This email is already subscribed.'
                subscribers.append({'email': email, 'subscribed_at': datetime.now().isoformat()})
                _save_subscribers(subscribers)
            return True, 'Subscribed successfully!'
        except TimeoutError:
            app.logger.error("Timed out acquiring subscriber lock")
            return False, 'Server busy. Please try again.'
        except Exception as e:
            app.logger.error(f"Error adding subscriber: {e}")
            return False, 'Unable to add subscriber. Please try again.'

    def _remove_subscriber(email):
        """Remove an email from the subscriber list. Returns (success, message)."""
        email = email.strip().lower()
        try:
            with _subscribers_lock():
                subscribers = _load_subscribers()
                original_count = len(subscribers)
                subscribers = [s for s in subscribers if s['email'] != email]
                if len(subscribers) == original_count:
                    return False, 'Email not found in subscriber list.'
                _save_subscribers(subscribers)
            return True, 'Unsubscribed successfully.'
        except TimeoutError:
            app.logger.error("Timed out acquiring subscriber lock")
            return False, 'Server busy. Please try again.'
        except Exception as e:
            app.logger.error(f"Error removing subscriber: {e}")
            return False, 'Unable to remove subscriber. Please try again.'

    NEWS_HUBS = {
        'all': {
            'key': 'all',
            'path': '/ai-news',
            'nav_label': 'AI News',
            'cadence': 'daily, weekly and monthly',
            'changefreq': 'daily',
            'title_tag': 'AI News: Daily, Weekly and Monthly AI Updates',
            'meta_description': "AI news in three rhythms: a daily AI news briefing, a weekly AI news roundup every Monday and a monthly AI news recap on the first.",
            'h1': 'AI News, Organized by Day, Week and Month',
            'kicker': 'AI news archive',
            'keywords': 'AI news, daily AI news, weekly AI news roundup, monthly AI news recap, AI news today, artificial intelligence news',
            'intro': [
                'AI news arrives faster than anyone can read it, so this archive splits it by rhythm. The daily AI news briefing covers the releases, tools and incidents that changed something today. The weekly AI news roundup, published every Monday, connects seven days of stories. The monthly AI news recap, published on the first of each month, explains the trend behind the headlines.',
                'Start wherever your calendar is. Read the daily AI news for today, the weekly AI news roundup for the last seven days, or the monthly AI news recap for the big picture.',
            ],
            'faq': [
                ('What is the difference between daily, weekly and monthly AI news?',
                 'Daily AI news reports one day at a time. The weekly AI news roundup groups the previous seven days and ranks what mattered. The monthly AI news recap zooms out to the trends that lasted the whole month.'),
                ('How often is AI news published here?',
                 'A daily AI news briefing is published on most days. The weekly AI news roundup ships every Monday, and the monthly AI news recap ships on the first day of each month.'),
                ('Where should I start reading AI news?',
                 'Start with today\'s daily AI news briefing. If you have been away, read the weekly AI news roundup. If you want the whole narrative, open the monthly AI news recap.'),
            ],
        },
        'daily': {
            'key': 'daily',
            'path': '/daily-ai-news',
            'nav_label': 'Daily AI News',
            'cadence': 'every day',
            'changefreq': 'daily',
            'title_tag': "Daily AI News: Today's AI Briefing in Plain English",
            'meta_description': "Daily AI news in about five minutes: today's model releases, agents, chips, security and policy, explained in plain English with sources.",
            'h1': 'Daily AI News, Explained in Five Minutes',
            'kicker': 'Daily AI news',
            'keywords': 'daily AI news, AI news today, today AI news, AI daily briefing, AI news, daily news, artificial intelligence news',
            'intro': [
                'The daily AI news briefing is the fastest way to keep up with artificial intelligence. Every day we read the model releases, agent launches, chip deals, security incidents and policy fights, then write the handful of stories that actually change what you can build.',
                'Each daily AI news post takes about five minutes: what happened, why it matters and what to watch next. When you want the long view, the weekly AI news roundup and the monthly AI news recap are one click away.',
            ],
            'faq': [
                ('What is daily AI news?',
                 'Daily AI news is a short, dated briefing that covers the AI stories that changed something that day: model releases, agent tools, chips, security, funding and regulation. Each edition is written in plain English and linked to primary sources.'),
                ('How long does a daily AI news briefing take to read?',
                 'Most daily AI news posts take five to eight minutes. The opening summary gives you the five-minute version, and each section goes deeper on one storyline.'),
                ('Is the daily AI news free?',
                 'Yes. Every daily AI news post, weekly AI news roundup and monthly AI news recap on this site is free to read, with no paywall and no signup.'),
            ],
        },
        'weekly': {
            'key': 'weekly',
            'path': '/weekly-ai-news',
            'nav_label': 'Weekly AI News',
            'cadence': 'every Monday',
            'changefreq': 'weekly',
            'title_tag': "Weekly AI News Roundup: Every Monday's AI Recap",
            'meta_description': "The weekly AI news roundup, published every Monday: seven days of daily AI news ranked, connected and explained in one readable post.",
            'h1': 'The Weekly AI News Roundup',
            'kicker': 'Weekly AI news',
            'keywords': 'weekly AI news, weekly AI news roundup, AI news this week, weekly news, AI weekly recap, Monday AI news',
            'intro': [
                'This is the archive of weekly AI news roundups. A weekly AI news roundup is published every Monday and pulls the previous seven days of daily AI news into one story: the model that shipped, the benchmark that fell, the deal that moved a market and the risk nobody noticed.',
                'Monday is also the best day to catch the monthly AI news recap when a new month begins. Missing a day is fine — the weekly AI news page catches you up on everything that mattered in the last seven days.',
            ],
            'faq': [
                ('When is the weekly AI news roundup published?',
                 'The weekly AI news roundup is published every Monday. It collects the previous seven days of daily AI news into one post, so a missed weekday is never a missed story.'),
                ('What is the difference between weekly and daily AI news?',
                 'Daily AI news reports one day at a time. The weekly AI news roundup connects those days: it ranks the stories, drops the noise and explains which changes actually lasted.'),
                ('Can I read past weekly AI news editions?',
                 'Yes. Every Monday edition stays in this weekly AI news archive, newest first, with its date and summary.'),
            ],
        },
        'monthly': {
            'key': 'monthly',
            'path': '/monthly-ai-news',
            'nav_label': 'Monthly AI News',
            'cadence': 'the 1st of every month',
            'changefreq': 'monthly',
            'title_tag': 'Monthly AI News Recap: The Month in AI, Explained',
            'meta_description': "The monthly AI news recap, published on the first of every month: the trends behind the daily AI news, from model pricing to chips and regulation.",
            'h1': 'The Monthly AI News Recap',
            'kicker': 'Monthly AI news',
            'keywords': 'monthly AI news, monthly AI news recap, AI news this month, monthly news, AI monthly roundup, AI news summary',
            'intro': [
                'The monthly AI news recap is the big-picture edition, published on the first day of every month. It steps back from the daily AI news cycle and the weekly AI news roundup to explain the trends that lasted: pricing, capability, regulation, hardware supply and the stories that turned out to be noise.',
                'Use the monthly AI news archive to see how the AI narrative changed month by month. Every recap links back to the daily AI news briefings and weekly AI news roundups it draws from, so you can go as deep as you want.',
            ],
            'faq': [
                ('When is the monthly AI news recap published?',
                 'The monthly AI news recap is published on the first day of every month. It looks back at the previous month of daily AI news and weekly AI news roundups.'),
                ('What does the monthly AI news recap cover?',
                 'The monthly AI news recap covers the trends, not just the headlines: model pricing, capability jumps, chip supply, regulation, funding and the safety incidents that shaped the month.'),
                ('Should I read the daily, weekly or monthly AI news first?',
                 'Start with the monthly AI news recap for the big picture, use the weekly AI news roundup to catch up on the last seven days, and read the daily AI news briefing for today\'s story.'),
            ],
        },
    }

    def _news_editions(hub_key, posts):
        """Group posts into archive sections. Weekly = Monday editions, monthly = the 1st."""
        dated = [(post, _parse_post_date(post.get('published_date'))) for post in posts]
        dated = [(post, dt) for post, dt in dated if dt is not None]

        if hub_key == 'weekly':
            dated = [(post, dt) for post, dt in dated if dt.weekday() == 0]
        elif hub_key == 'monthly':
            dated = [(post, dt) for post, dt in dated if dt.day == 1]

        groups = {}
        for post, dt in dated:
            if hub_key == 'weekly':
                key = dt.strftime('%Y-%m-%d')
                label = 'Week of ' + dt.strftime('%B ') + str(dt.day) + ', ' + str(dt.year)
                sub = 'Weekly AI news · Monday, ' + dt.strftime('%B ') + str(dt.day) + ', ' + str(dt.year)
                anchor = 'week-' + key
            elif hub_key == 'monthly':
                key = dt.strftime('%Y-%m')
                label = dt.strftime('%B %Y')
                sub = 'Monthly AI news recap · ' + dt.strftime('%B ') + str(dt.day) + ', ' + str(dt.year)
                anchor = 'month-' + key
            else:
                key = dt.strftime('%Y-%m')
                label = dt.strftime('%B %Y')
                sub = ''
                anchor = 'month-' + key
            group = groups.setdefault(key, {
                'key': key, 'anchor': anchor, 'label': label, 'sub': sub,
                'date': dt, 'posts': [],
            })
            group['posts'].append(post)

        return sorted(groups.values(), key=lambda g: g['date'], reverse=True)

    def _render_news_hub(hub_key):
        hub = NEWS_HUBS[hub_key]
        all_posts = get_all_posts()
        posts = [p for p in all_posts if _is_ai_news(p)] if hub_key in ('all', 'daily') else all_posts
        groups = _news_editions(hub_key, posts)
        listed_posts = [p for group in groups for p in group['posts']] or posts
        return render_template(
            'news_hub.html',
            hub=hub,
            hubs=[NEWS_HUBS[k] for k in ('daily', 'weekly', 'monthly', 'all')],
            groups=groups,
            post_count=len(posts),
            edition_count=len(groups),
            latest_posts=listed_posts[:10],
            today=datetime.now().strftime('%Y-%m-%d'),
        )

    @app.route('/')
    def index():
        posts = get_all_posts()
        return render_template('index.html', posts=posts)

    @app.route('/search')
    def search():
        query = (request.args.get('q') or '').strip()
        results = []
        if query:
            terms = [term for term in re.findall(r'[a-z0-9]+', query.lower())
                     if len(term) > 1] or [query.lower()]
            scored = []
            for post in get_all_posts():
                haystack = ' '.join(str(post.get(key, '')) for key in
                                    ('title', 'description', 'tags', 'keywords',
                                     'content', 'author')).lower()
                if all(term in haystack for term in terms):
                    score = sum(haystack.count(term) for term in terms)
                    scored.append((score, post.get('published_date', ''), post))
            scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
            results = [post for _, _, post in scored[:40]]
        return render_template('search.html',
                               query=query,
                               results=results,
                               result_count=len(results))

    @app.route('/ai-news')
    def ai_news():
        return _render_news_hub('all')

    @app.route('/daily-ai-news')
    def daily_ai_news():
        return _render_news_hub('daily')

    @app.route('/weekly-ai-news')
    def weekly_ai_news():
        return _render_news_hub('weekly')

    @app.route('/monthly-ai-news')
    def monthly_ai_news():
        return _render_news_hub('monthly')

    @app.route('/daily')
    def daily_archive_alias():
        return redirect(url_for('daily_ai_news'), code=301)

    @app.route('/weekly')
    def weekly_archive_alias():
        return redirect(url_for('weekly_ai_news'), code=301)

    @app.route('/monthly')
    def monthly_archive_alias():
        return redirect(url_for('monthly_ai_news'), code=301)

    @app.route('/blog')
    def blog_list():
        return redirect(url_for('index'), code=301)

    @app.route('/index.html')
    def index_html():
        return redirect(url_for('index'), code=301)

    @app.route('/blogs/<slug>')
    @app.route('/blogs/<slug>/')
    def legacy_blog(slug):
        """Old /blogs/<slug> URLs -> canonical /blog/<slug>."""
        if _post_exists(slug):
            return redirect(url_for('blog_post', slug=slug), code=301)
        abort(404)

    @app.route('/post/<slug>')
    @app.route('/posts/<slug>')
    def legacy_post(slug):
        """Common legacy post URL patterns -> canonical /blog/<slug>."""
        if _post_exists(slug):
            return redirect(url_for('blog_post', slug=slug), code=301)
        abort(404)

    @app.route('/blog/<slug>')
    def blog_post(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        if not os.path.isdir(post_dir) or not _post_exists(slug):
            # Case/format-insensitive fallback for old or lowercased links.
            wanted = _slug_key(slug)
            match = None
            if os.path.isdir(BLOGS_DIR):
                for name in os.listdir(BLOGS_DIR):
                    if _slug_key(name) == wanted and _post_exists(name):
                        match = name
                        break
            if match:
                return redirect(url_for('blog_post', slug=match), code=301)
            abort(404)
        
        md_path = os.path.join(post_dir, 'blog.md')
        if not os.path.exists(md_path):
            abort(404)
            
        meta, body = parse_blog_file(md_path)
        
        author = meta.get('author', 'Anonymous')
        published_date = meta.get('date', datetime.now().strftime('%Y-%m-%d'))
        modified_date = meta.get('updated') or meta.get('modified_date') or meta.get('last_modified') or meta.get('modified') or published_date
        post = {
            'slug': slug,
            'title': meta.get('title', slug.replace('-', ' ').title()),
            'meta_title': meta.get('meta_title', meta.get('title', slug.replace('-', ' ').title())),
            'description': meta.get('description', ''),
            'author': author,
            'author_slug': author.lower().replace(' ', '-'),
            'published_date': published_date,
            'modified_date': modified_date,
            'content': body,
            'featured_image': f'/blogs/{slug}/image.png' if os.path.exists(os.path.join(post_dir, 'image.png')) else None,
            'image_alt': meta.get('image_alt', ''),
            'tags': meta.get('tags', ''),
            'keywords': meta.get('keywords', ''),
            'url': request.url
        }
        post_dt = _parse_post_date(published_date)
        post['is_monday'] = bool(post_dt and post_dt.weekday() == 0)
        post['is_month_start'] = bool(post_dt and post_dt.day == 1)
        if post['is_month_start']:
            post['edition_label'] = 'monthly AI news recap'
        elif post['is_monday']:
            post['edition_label'] = 'weekly AI news roundup'
        else:
            post['edition_label'] = 'daily AI news briefing'
        post['is_news'] = _is_ai_news(post)
        post['faq_items'] = _extract_faq(body)
        if post['featured_image']:
            width, height = _png_size(os.path.join(post_dir, 'image.png'))
            post['featured_image_width'] = width
            post['featured_image_height'] = height
        else:
            post['featured_image_width'] = 1200
            post['featured_image_height'] = 630

        # Related posts: specific shared tags count more than generic ones,
        # and headline/description overlap breaks ties.
        generic_tags = {'ai', 'ai news', 'technews', 'llm', 'artificial intelligence'}
        current_tags = _tag_set(post['tags'])
        current_specific = current_tags - generic_tags
        title_terms = set(re.findall(r'[a-z0-9]{4,}',
                                     f"{post['title']} {post['description']}".lower()))
        all_posts = get_all_posts()
        scored = []
        for other in all_posts:
            if other['slug'] == slug:
                continue
            other_tags = _tag_set(other['tags'])
            other_terms = set(re.findall(r'[a-z0-9]{4,}',
                                         f"{other['title']} {other['description']}".lower()))
            score = (3 * len(current_specific & other_tags)
                     + len((current_tags - current_specific) & other_tags)
                     + len(title_terms & other_terms))
            if score:
                scored.append((score, other.get('published_date', ''), other))
        scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
        related = [item[2] for item in scored[:3]]

        return render_template('blog.html',
                               blog=post,
                               site_name=app.config['SITE_CONFIG']['name'],
                               site_logo=app.config['SITE_CONFIG']['logo'],
                               current_year=app.config['SITE_CONFIG']['current_year'],
                               related_posts=related[:3])

    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html', site=app.config['SITE_CONFIG'])

    @app.route('/terms')
    def terms():
        return render_template('terms.html', site=app.config['SITE_CONFIG'])

    @app.route('/docs')
    def docs():
        return render_template('docs.html', site=app.config['SITE_CONFIG'])

    @app.route('/docs/api.md')
    def api_docs():
        docs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'docs')
        return send_from_directory(docs_dir, 'API.md', mimetype='text/markdown')

    def _normalize_tag(value):
        return str(value).strip().lower().replace(' ', '-')

    @app.route('/tag/<tag_slug>')
    def tag_posts(tag_slug):
        target = _normalize_tag(tag_slug)
        if tag_slug != target:
            return redirect(url_for('tag_posts', tag_slug=target), code=301)
        all_posts = get_all_posts()
        filtered = [p for p in all_posts if target in [_normalize_tag(t) for t in (p['tags'] or '').split(',')]]
        if not filtered:
            abort(404)
        display = next(
            (t.strip() for p in filtered for t in (p['tags'] or '').split(',') if _normalize_tag(t) == target),
            tag_slug.replace('-', ' ').title()
        )
        return render_template('tag.html',
                               posts=filtered,
                               tag=display,
                               noindex=len(filtered) < 2,
                               site=app.config['SITE_CONFIG'])

    @app.route('/author/<author_slug>')
    def author_posts(author_slug):
        target = _slug_key(author_slug)
        if author_slug != target:
            return redirect(url_for('author_posts', author_slug=target), code=301)
        all_posts = get_all_posts()
        filtered = [p for p in all_posts if _slug_key(p['author']) == target]
        if not filtered:
            abort(404)
        author_name = filtered[0]['author']
        return render_template('author.html',
                               posts=filtered,
                               author=author_name,
                               site=app.config['SITE_CONFIG'])
        if not request.args:
            return render_template('upload.html')
        
        try:
            slug = request.args.get('slug', '')
            title = request.args.get('title', '')
            author = request.args.get('author', '')
            description = request.args.get('description', '')
            content = request.args.get('content', '')
            date = request.args.get('publishedDate', datetime.now().strftime('%Y-%m-%d'))
            image_svg = request.args.get('image', '') # Expecting SVG content
            tags = request.args.get('tags', '')

            post_dir = os.path.join(BLOGS_DIR, slug)
            os.makedirs(post_dir, exist_ok=True)

            # Create blog.md with frontmatter
            md_content = f"---\ntitle: {title}\nauthor: {author}\ndate: {date}\ndescription: {description}\ntags: {tags}\n---\n\n{content}"
            with open(os.path.join(post_dir, 'blog.md'), 'w', encoding='utf-8') as f:
                f.write(md_content)

            # Save image.png if provided
            if image_svg:
                with open(os.path.join(post_dir, 'image.png'), 'w', encoding='utf-8') as f:
                    f.write(image_svg)

            flash(f'Blog post "{title}" uploaded successfully!', 'success')
            return redirect(url_for('blog_list'))
        except Exception as e:
            flash(f'Error processing upload: {str(e)}', 'error')
            return redirect(url_for('handle_upload'))

    @app.route('/blog.md')
    def latest_blog_markdown():
        posts = get_all_posts()
        if not posts:
            abort(404)
        latest = posts[0]
        post_dir = os.path.join(BLOGS_DIR, latest['slug'])
        md_path = os.path.join(post_dir, 'blog.md')
        if not os.path.exists(md_path):
            abort(404)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
        response = app.make_response(content)
        response.headers['Content-Type'] = 'text/markdown; charset=utf-8'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Cache-Control'] = 'public, max-age=3600'
        response.headers['X-Robots-Tag'] = 'noindex, nofollow'
        return response

    @app.route('/image.png')
    def latest_blog_image():
        # Newest post with an image, not merely the newest post.
        for post in get_all_posts():
            post_dir = os.path.join(BLOGS_DIR, post['slug'])
            image_path = os.path.join(post_dir, 'image.png')
            if os.path.exists(image_path):
                return send_from_directory(post_dir, 'image.png', mimetype='image/png')
        abort(404)

    @app.route('/about')
    def about():
        return render_template('about.html', site=app.config['SITE_CONFIG'])

    @app.route('/subscribe', methods=['GET', 'POST'])
    def subscribe():
        if request.method == 'POST':
            email = request.form.get('email', '').strip()
            success, message = _add_subscriber(email)
            if success:
                flash(message, 'success')
                return redirect(url_for('subscribe'))
            else:
                flash(message, 'error')
        return render_template('subscribe.html', site=app.config['SITE_CONFIG'])

    @app.route('/unsubscribe', methods=['GET', 'POST'])
    def unsubscribe():
        if request.method == 'POST':
            email = request.form.get('email', '').strip()
            success, message = _remove_subscriber(email)
            if success:
                flash(message, 'success')
                return redirect(url_for('unsubscribe'))
            else:
                flash(message, 'error')
        return render_template('unsubscribe.html', site=app.config['SITE_CONFIG'])

    @app.route('/llms.txt')
    def llms_txt():
        site_url = get_site_base()
        posts = get_all_posts()
        lines = [
            f"# {app.config['SITE_CONFIG']['name']}",
            '',
            f"> {app.config['SITE_CONFIG']['description']}",
            '',
            '## Recent posts',
        ]
        for post in posts[:30]:
            lines.append(f"- [{post['title']}]({site_url}/blog/{post['slug']}): {post['description']}")
        lines += [
            '',
            '## AI news archives',
            f"- [Daily AI News]({site_url}/daily-ai-news): today's AI briefing in plain English",
            f"- [Weekly AI News]({site_url}/weekly-ai-news): the roundup published every Monday",
            f"- [Monthly AI News]({site_url}/monthly-ai-news): the recap published on the first of the month",
            f"- [All AI News]({site_url}/ai-news): every daily, weekly and monthly edition",
            '',
            '## Site',
            f"- [Blog]({site_url}/): all articles",
            f"- [Search]({site_url}/search): search every AI news edition",
            f"- [API & Docs]({site_url}/docs): every public endpoint, feed, and file format",
            f"- [About]({site_url}/about): about this site and its author",
            f"- [RSS]({site_url}/rss.xml): RSS feed",
            f"- [Sitemap]({site_url}/sitemap.xml): XML sitemap",
            f"- [News sitemap]({site_url}/news-sitemap.xml): articles from the last 48 hours",
        ]
        return Response('\n'.join(lines), content_type='text/plain; charset=utf-8')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        if request.path == '/admin' or request.path.startswith('/admin/'):
            response.headers['X-Robots-Tag'] = 'noindex, nofollow'
            response.headers['Cache-Control'] = 'no-store'
        if request.path.startswith('/static/'):
            response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
        elif request.path in ('/sitemap.xml', '/news-sitemap.xml'):
            response.headers['Cache-Control'] = 'public, max-age=1800'
        elif request.path == '/robots.txt':
            response.headers['Cache-Control'] = 'public, max-age=86400'
        return response

    @app.template_filter('urlencode')
    def urlencode_filter(s):
        return quote(str(s))

    @app.template_filter('tag_list')
    def tag_list_filter(text):
        if not text: return []
        return [t.strip() for t in text.split(',') if t.strip()]

    @app.template_filter('tag_slug')
    def tag_slug_filter(text):
        return _normalize_tag(text)

    @app.template_filter('markdown')
    def markdown_filter(text):
        if not text: return ''
        return render_markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])

    @app.route('/news-sitemap.xml')
    def news_sitemap():
        """Google News sitemap: only articles published in the last 48 hours."""
        cutoff = datetime.now() - timedelta(days=2)
        posts = []
        for post in get_all_posts():
            post_dt = _parse_post_date(post.get('published_date'))
            if post_dt and post_dt >= cutoff:
                posts.append(post)
        posts.sort(key=lambda post: post.get('published_date', ''), reverse=True)
        return Response(render_template('news_sitemap.xml', posts=posts[:1000]),
                        mimetype='application/xml')

    @app.route('/sitemap.xml')
    def sitemap():
        site_url = get_site_base()
        urls = [{
            'loc': url_for('index', _external=True),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'daily',
            'priority': '1.0',
            'image': None,
            'image_title': None
        }]
        all_posts = get_all_posts()

        all_tags = {}
        tag_counts = {}
        all_authors = {}
        for post in all_posts:
            post_image = None
            post_image_title = None
            if post.get('featured_image'):
                post_image = get_site_base() + post['featured_image']
                post_image_title = post['title']
            urls.append({
                'loc': url_for('blog_post', slug=post['slug'], _external=True),
                'lastmod': post.get('modified_date', post['published_date']),
                'changefreq': 'weekly',
                'priority': '0.8',
                'image': post_image,
                'image_title': post_image_title
            })
            for t in (post.get('tags') or '').split(','):
                t = t.strip()
                if t:
                    tag_slug = _normalize_tag(t)
                    all_tags.setdefault(tag_slug, t)
                    tag_counts[tag_slug] = tag_counts.get(tag_slug, 0) + 1
            all_authors.setdefault(_slug_key(post['author']), post['author'])

        for tag_slug in sorted(all_tags):
            if tag_counts.get(tag_slug, 0) < 2:
                continue
            urls.append({
                'loc': url_for('tag_posts', tag_slug=tag_slug, _external=True),
                'lastmod': datetime.now().strftime('%Y-%m-%d'),
                'changefreq': 'weekly',
                'priority': '0.6',
                'image': None,
                'image_title': None
            })

        for author_slug in sorted(all_authors):
            urls.append({
                'loc': url_for('author_posts', author_slug=author_slug, _external=True),
                'lastmod': datetime.now().strftime('%Y-%m-%d'),
                'changefreq': 'weekly',
                'priority': '0.5',
                'image': None,
                'image_title': None
            })

        for hub_key, endpoint in (
            ('daily', 'daily_ai_news'),
            ('weekly', 'weekly_ai_news'),
            ('monthly', 'monthly_ai_news'),
            ('all', 'ai_news'),
        ):
            hub = NEWS_HUBS[hub_key]
            hub_posts = ([p for p in all_posts if _is_ai_news(p)]
                         if hub_key in ('all', 'daily') else all_posts)
            hub_groups = _news_editions(hub_key, hub_posts)
            hub_lastmod = (hub_groups[0]['posts'][0].get('modified_date')
                           if hub_groups else datetime.now().strftime('%Y-%m-%d'))
            urls.append({
                'loc': url_for(endpoint, _external=True),
                'lastmod': hub_lastmod,
                'changefreq': hub['changefreq'],
                'priority': '0.9',
                'image': None,
                'image_title': None
            })

        urls.append({
            'loc': url_for('about', _external=True),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.4',
            'image': None,
            'image_title': None
        })
        urls.append({
            'loc': url_for('docs', _external=True),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'monthly',
            'priority': '0.4',
            'image': None,
            'image_title': None
        })
        urls.append({
            'loc': url_for('privacy', _external=True),
            'lastmod': '2026-07-20',
            'changefreq': 'monthly',
            'priority': '0.3',
            'image': None,
            'image_title': None
        })
        urls.append({
            'loc': url_for('terms', _external=True),
            'lastmod': '2026-07-20',
            'changefreq': 'monthly',
            'priority': '0.3',
            'image': None,
            'image_title': None
        })

        base = get_site_base()
        if base.startswith('https://'):
            for entry in urls:
                if entry.get('loc', '').startswith('http://'):
                    entry['loc'] = 'https://' + entry['loc'][7:]
                if (entry.get('image') or '').startswith('http://'):
                    entry['image'] = 'https://' + entry['image'][7:]

        return Response(render_template('sitemap.xml', urls=urls),
                        mimetype='application/xml')

    @app.route('/robots.txt')
    def robots():
        site_url = get_site_base()
        content = f"""User-agent: *
Allow: /
Content-Signal: ai-train=yes, search=yes, ai-input=yes

Sitemap: {site_url}/sitemap.xml
Sitemap: {site_url}/news-sitemap.xml
"""
        return Response(content, content_type='text/plain; charset=utf-8')

    @app.route('/feed')
    @app.route('/feed.xml')
    def feed_alias():
        return redirect(url_for('rss_feed'), code=301)

    @app.route('/rss.xml')
    def rss_feed():
        all_posts = get_all_posts()
        site_url = get_site_base()
        site_name = app.config['SITE_CONFIG']['name']
        site_desc = app.config['SITE_CONFIG']['description']

        def cdata(value):
            """Escape a CDATA payload without breaking the section."""
            return str(value or '').replace(']]>', ']]]]><![CDATA[>')

        items = ''
        for post in all_posts[:20]:
            post_url = url_for('blog_post', slug=post['slug'], _external=True)
            try:
                pub_date = datetime.strptime(post["published_date"][:10], "%Y-%m-%d").strftime("%a, %d %b %Y 00:00:00 +0000")
            except (ValueError, TypeError):
                pub_date = datetime.utcnow().strftime("%a, %d %b %Y 00:00:00 +0000")
            content_html = render_markdown(post['content'], extensions=['fenced_code', 'codehilite', 'tables'])
            image_tag = ''
            if post.get('featured_image'):
                image_url = get_site_base() + post['featured_image']
                image_tag = f'''
    <enclosure url={xml_quoteattr(image_url)} type="image/png" length="0"/>'''
            items += f'''
  <item>
    <title>{xml_escape(str(post["title"]))}</title>
    <link>{xml_escape(post_url)}</link>
    <guid isPermaLink="true">{xml_escape(post_url)}</guid>
    <description><![CDATA[{cdata(post["description"])}]]></description>
    <content:encoded><![CDATA[{cdata(content_html)}]]></content:encoded>
    <dc:creator>{xml_escape(str(post["author"]))}</dc:creator>
    <pubDate>{pub_date}</pubDate>{image_tag}
  </item>'''

        rss_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{xml_escape(site_name)}</title>
    <link>{xml_escape(site_url)}/</link>
    <description>{xml_escape(site_desc)}</description>
    <language>en-us</language>
    <lastBuildDate>{datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")}</lastBuildDate>
    <atom:link href={xml_quoteattr(url_for("rss_feed", _external=True))} rel="self" type="application/rss+xml"/>
    <generator>Trillioniar Blog</generator>
    <ttl>60</ttl>{items}
  </channel>
</rss>'''

        return Response(rss_xml, mimetype='application/rss+xml; charset=utf-8')

    return app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
