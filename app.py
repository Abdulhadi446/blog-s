from flask import Flask, render_template, abort, request, url_for, flash, redirect, session, g
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from urllib.parse import quote, urlparse
import hashlib
import os
import json
from regex import F
import ast
import hashlib
from sqlalchemy import PrimaryKeyConstraint
import requests
import re
import time
from bs4 import BeautifulSoup
from functools import wraps
from markdown import markdown as render_markdown
import math

# Initialize extensions
db = SQLAlchemy()

def create_app(config_name=None):
    app = Flask(__name__)
    
    # Import config after app creation to avoid circular imports
    from config import config
    config_name = config_name or os.environ.get('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Make site config available in all templates
    @app.context_processor
    def inject_site_config():
        seo = {
            'site_name': SITE_CONFIG['name'],
            'site_description': SITE_CONFIG['description'],
            'site_url': request.url_root.rstrip('/'),
            'site_logo': SITE_CONFIG['logo'],
            'current_year': SITE_CONFIG['current_year'],
        }
        return {'site': SITE_CONFIG, 'seo': seo, 'is_admin': session.get('admin')}

    # --- Admin auth helpers ---
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

    @app.route('/admin/login', methods=['GET', 'POST'])
    def admin_login():
        if request.method == 'POST':
            password = request.form.get('password', '')
            if password == get_admin_password():
                session['admin'] = True
                next_page = request.args.get('next')
                return redirect(next_page or url_for('handle_upload'))
            flash('Invalid password', 'error')
        return render_template('admin_login.html')

    @app.route('/admin/logout')
    def admin_logout():
        session.pop('admin', None)
        return redirect(url_for('index'))

    # --- Database model ---
    class BlogPost(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        slug = db.Column(db.String(255), unique=True, nullable=False)
        title = db.Column(db.String(255), nullable=False)
        description = db.Column(db.Text, nullable=False)
        content = db.Column(db.Text, nullable=False)
        author = db.Column(db.String(100), nullable=False)
        author_avatar = db.Column(db.String(255))
        author_url = db.Column(db.String(255))
        published_date = db.Column(db.String(50))
        published_date_formatted = db.Column(db.String(50))
        modified_date = db.Column(db.String(50))
        featured_image = db.Column(db.String(255))
        reading_time = db.Column(db.Integer)
        keywords = db.Column(db.Text)
        tags = db.Column(db.Text)
        url = db.Column(db.String(255))

        def tag_list(self):
            return [t.strip() for t in (self.tags or '').split(',') if t.strip()]

        def keywords_list(self):
            return [k.strip() for k in (self.keywords or '').split(',') if k.strip()]

    # --- Site Config ---
    SITE_CONFIG = app.config['SITE_CONFIG']

    # --- Related posts logic ---
    def get_related_posts(current_slug, limit=3):
        current_post = BlogPost.query.filter_by(slug=current_slug).first()
        if not current_post or not current_post.tags:
            return []

        current_tags = set(current_post.tags.split(','))
        related = []

        for post in BlogPost.query.filter(BlogPost.slug != current_slug).all():
            if not post.tags:
                continue
            if current_tags.intersection(post.tags.split(',')):
                related.append(post)

        return related[:limit]

    def gravatar_url(email, size=200):
        email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " +
                      "AppleWebKit/537.36 (KHTML, like Gecko) " +
                      "Chrome/115.0.0.0 Safari/537.36"
    }

    def fetch_first_bing_image(query):
        """Fetch the first image URL from Bing Images search."""
        try:
            start_time = time.time()

            resp = requests.get(
                "https://www.bing.com/images/search",
                headers=HEADERS,
                params={"q": query},
                timeout=10
            )
            soup = BeautifulSoup(resp.text, "html.parser")
            for a in soup.select("a.iusc"):
                m = a.get("m", "")
                match = re.search(r'"murl":"(https?://[^"]+)"', m)
                if match:
                    elapsed = time.time() - start_time
                    if not app.config['DEBUG']:  # Only log in debug mode
                        pass  # Suppress logging in production
                    return match.group(1)

            elapsed = time.time() - start_time
            if not app.config['DEBUG']:
                pass  # Suppress logging in production
            return None

        except Exception as e:
            if not app.config['DEBUG']:
                pass  # Suppress logging in production
            return None

    # --- Routes ---
    @app.route('/')
    def index():
        posts = BlogPost.query.order_by(BlogPost.id.desc()).all()
        return render_template('index.html', posts=posts)

    @app.route('/blog')
    def blog_list():
        return index()

    @app.route('/blog/<slug>')
    def blog_post(slug):
        post = BlogPost.query.filter_by(slug=slug).first_or_404()
        post.url = request.url
        related_posts = get_related_posts(slug)
        return render_template('blog.html',
                               blog=post,
                               site_name=SITE_CONFIG['name'],
                               site_logo=SITE_CONFIG['logo'],
                               current_year=SITE_CONFIG['current_year'],
                               related_posts=related_posts)

    @app.route('/tag/<tag_slug>')
    def tag_posts(tag_slug):
        filtered = []
        for post in BlogPost.query.all():
            if tag_slug in (post.tags or '').split(','):
                filtered.append(post)
        return render_template('tag.html',
                               posts=filtered,
                               tag=tag_slug.replace('-', ' ').title(),
                               site=SITE_CONFIG)

    @app.route('/author/<author_slug>')
    def author_posts(author_slug):
        author_name = author_slug.replace('-', ' ').title()
        filtered = []
        for post in BlogPost.query.all():
            if post.author.lower().replace(' ', '-') == author_slug:
                filtered.append(post)
        return render_template('author.html',
                               posts=filtered,
                               author=author_name,
                               site=SITE_CONFIG)

    @app.route('/sitemap.xml')
    def sitemap():
        app.response_class.mimetype = 'application/xml'
        urls = [{
            'loc': url_for('index', _external=True),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'daily',
            'priority': '1.0'
        }]
        for post in BlogPost.query.all():
            urls.append({
                'loc': url_for('blog_post', slug=post.slug, _external=True),
                'lastmod': (post.modified_date or '')[:10],
                'changefreq': 'weekly',
                'priority': '0.8'
            })
        return render_template('sitemap.xml', urls=urls)

    @app.route('/robots.txt')
    def robots():
        app.response_class.mimetype = 'text/plain'
        return render_template('robots.txt', site_url=SITE_CONFIG['url'])

    @app.route('/upload', methods=['GET'])
    @login_required
    def handle_upload():
        """Handle both the upload form display and form submission"""

        # If no query parameters, show the form
        if not request.args:
            return render_template('upload.html')

        try:
            # Get all parameters from query string
            slug = request.args.get('slug', '')
            title = request.args.get('title', '')
            
            # Check if blog post with same title already exists
            post_exists = db.session.query(BlogPost.id).filter_by(title=title).first() is not None
            if post_exists:
                flash(f'Error: Blog post with title "{title}" already exists.', 'error')
                return redirect(url_for('handle_upload'))

            # Continue processing if no duplicate
            author = request.args.get('author', '')
            author_image = gravatar_url(author)
            description = request.args.get('description', '')
            content = request.args.get('content', '')
            published_date = request.args.get('publishedDate', '')
            formatted_date = request.args.get('formattedDate', '')
            modified_date = request.args.get('modifiedDate', '')
            image = request.args.get('image', '') or fetch_first_bing_image(title)
            keywords = request.args.get('keywords', '')
            tags = request.args.get('tags', '')

            # Parse tags from string format to actual objects
            tag_objects = []
            if tags:
                try:
                    tags_clean = tags.replace("'", '"')
                    tag_parts = tags_clean.split('},{')
                    for i, tag_part in enumerate(tag_parts):
                        if i == 0:
                            tag_part = tag_part.lstrip('[{')
                        if i == len(tag_parts) - 1:
                            tag_part = tag_part.rstrip('}]')
                        else:
                            tag_part = tag_part.rstrip('}')
                        
                        if not tag_part.startswith('{'):
                            tag_part = '{' + tag_part
                        if not tag_part.endswith('}'):
                            tag_part = tag_part + '}'
                        
                        tag_obj = json.loads(tag_part)
                        tag_objects.append(tag_obj)
                except json.JSONDecodeError:
                    tag_names = tags.split(',')
                    tag_objects = [
                        {
                            'name': tag.strip(),
                            'slug': tag.strip().lower().replace(' ', '-')
                        }
                        for tag in tag_names if tag.strip()
                    ]

            # Debugging Output (only in debug mode)
            if app.config['DEBUG']:
                print("=" * 50)
                print("BLOG POST DATA RECEIVED:")
                print("=" * 50)
                print(f"Slug: {slug}")
                print(f"Title: {title}")
                print(f"Author: {author}")
                print(f"Author Image: {author_image}")
                print(f"Description: {description}")
                print(f"Content: {content}")
                print(f"Published Date: {published_date}")
                print(f"Formatted Date: {formatted_date}")
                print(f"Modified Date: {modified_date}")
                print(f"Image URL: {image}")
                print(f"Keywords: {keywords}")
                print(f"Tags (raw): {tags}")
                print("-" * 30)
                print("PROCESSED DATA:")
                print("-" * 30)
                print(f"Keywords List: {keywords.split(',') if keywords else []}")
                print(f"Tag Objects: {tag_objects}")
                print(f"Timestamp: {datetime.now().isoformat()}")
                print("=" * 50)

            upload(slug, title, description, content, author, author_image, published_date, formatted_date, modified_date, image, keywords, tags)
            flash(f'Blog post "{title}" uploaded successfully!', 'success')
            return redirect(url_for('blog_list'))

        except Exception as e:
            if app.config['DEBUG']:
                flash(f'Error processing upload: {str(e)}', 'error')
            else:
                flash('Error processing upload. Please try again.', 'error')
            return redirect(url_for('handle_upload'))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    @app.template_filter('urlencode')
    def urlencode_filter(s):
        return quote(str(s))

    @app.template_filter('markdown')
    def markdown_filter(text):
        if not text:
            return ''
        html = render_markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])
        return html

    @app.template_filter('reading_time')
    def reading_time_filter(text):
        if not text:
            return 1
        words = len(text.split())
        minutes = max(1, math.ceil(words / 200))
        return minutes

    # --- DB Setup: Add one post if empty ---
    def create_tables_and_seed():
        db.create_all()
        if not BlogPost.query.filter_by(slug='web-development-trends-2024').first():
            post = BlogPost(
                slug='web-development-trends-2024',
                title='Web Development Trends to Watch in 2024',
                description='Discover the latest web development trends...',
                content='''Content goes here. This is a sample blog post about web development trends in 2024...''',
                author='Mike Johnson',
                author_avatar='https://www.gravatar.com/avatar/238d7ebd4d50cba6fa37be4b56e7716f?s=200&d=identicon',
                author_url='/author/mike-johnson',
                published_date='2024-02-20T14:30:00Z',
                published_date_formatted='February 20, 2024',
                modified_date='2024-02-20T14:30:00Z',
                featured_image='https://www.convergine.com/images/_1015x450_crop_center-center_none/Web-Development-Trends-of-2024_-Top-9-Insights.png',
                reading_time=6,
                keywords='web development, trends, 2024, AI, serverless, PWA',
                tags='web-development,trends,technology',
                url='http://127.0.0.1:5000/blog/web-development-trends-2024'
            )
            db.session.add(post)
            db.session.commit()
    
    # Register the function to run before the first request
    @app.before_request
    def initialize_database():
        if not hasattr(app, 'database_initialized'):
            create_tables_and_seed()
            app.database_initialized = True

    def upload(slug, title, description, content, author, author_avatar, published_date, formatted_date, modified_date, image, keywords, tags):
        words = len(content.split())
        reading_time = max(1, math.ceil(words / 200))
        post = BlogPost(
                slug=f'{slug}',
                title=f'{title}',
                description=f'{description}',
                content=f'{content}',
                author=f'{author}',
                author_avatar=f'{author_avatar}',
                author_url=f'mailto:{author}',
                published_date=f'{published_date}',
                published_date_formatted=f'{formatted_date}',
                modified_date=f'{modified_date}',
                featured_image=f'{image}',
                reading_time=reading_time,
                keywords=f'{keywords}',
                tags=f'{extract_slugs(tags)}',
                url=f'{request.url_root.rstrip("/")}/blog/{slug}'
            )
        db.session.add(post)
        db.session.commit()

    return app

def extract_slugs(input_str):
    # Ensure the string is wrapped in square brackets so it becomes a list of dicts
    formatted_str = f"[{input_str.strip().lstrip('#')}]"
    try:
        items = ast.literal_eval(formatted_str)  # Safely parse the string into Python objects
        slugs = [item['slug'] for item in items if 'slug' in item]
        return ', '.join(slugs)
    except (SyntaxError, ValueError):
        return "Invalid input"

# This allows running the app directly for development
if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)