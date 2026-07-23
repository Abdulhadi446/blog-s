from flask import Flask, render_template, abort, request, url_for, flash, redirect, session, send_from_directory
from datetime import datetime
from urllib.parse import quote
import os
import json
import re
import math
import shutil
from markdown import markdown as render_markdown
from functools import wraps

def create_app(config_name=None):
    app = Flask(__name__)
    
    from config import config
    config_name = config_name or os.environ.get('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    BLOGS_DIR = os.path.expanduser('~/blog-s/blogs')
    os.makedirs(BLOGS_DIR, exist_ok=True)

    @app.context_processor
    def inject_site_config():
        seo = {
            'site_name': app.config['SITE_CONFIG']['name'],
            'site_description': app.config['SITE_CONFIG']['description'],
            'site_url': request.url_root.rstrip('/'),
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

    @app.route('/blogs/<slug>/image.png')
    def blog_image(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        image_path = os.path.join(post_dir, 'image.png')
        if os.path.exists(image_path):
            return send_from_directory(post_dir, 'image.png', mimetype='image/png')
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
                        meta[k.strip().lower()] = v.strip()
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
                    posts.append({
                        'slug': slug,
                        'title': meta.get('title', slug.replace('-', ' ').title()),
                        'description': meta.get('description', ''),
                        'author': meta.get('author', 'Anonymous'),
                        'published_date': meta.get('date', datetime.now().strftime('%Y-%m-%d')),
                        'featured_image': f'/blogs/{slug}/image.png' if os.path.exists(os.path.join(post_dir, 'image.png')) else None,
                        'content': body,
                        'tags': meta.get('tags', '')
                    })
        # Sort by date descending
        return sorted(posts, key=lambda x: x['published_date'], reverse=True)

    @app.route('/')
    def index():
        posts = get_all_posts()
        return render_template('index.html', posts=posts)

    @app.route('/blog')
    def blog_list():
        return index()

    @app.route('/blog/<slug>')
    def blog_post(slug):
        post_dir = os.path.join(BLOGS_DIR, slug)
        if not os.path.isdir(post_dir):
            abort(404)
        
        md_path = os.path.join(post_dir, 'blog.md')
        if not os.path.exists(md_path):
            abort(404)
            
        meta, body = parse_blog_file(md_path)
        
        post = {
            'slug': slug,
            'title': meta.get('title', slug.replace('-', ' ').title()),
            'description': meta.get('description', ''),
            'author': meta.get('author', 'Anonymous'),
            'published_date': meta.get('date', datetime.now().strftime('%Y-%m-%d')),
            'modified_date': meta.get('date', datetime.now().strftime('%Y-%m-%d')),
            'content': body,
            'featured_image': f'/blogs/{slug}/image.png' if os.path.exists(os.path.join(post_dir, 'image.png')) else None,
            'tags': meta.get('tags', ''),
            'url': request.url
        }

        current_tags = set(post['tags'].split(','))
        all_posts = get_all_posts()
        related = [p for p in all_posts if p['slug'] != slug and set(p['tags'].split(',')).intersection(current_tags)]

        return render_template('blog.html',
                               blog=post,
                               site_name=app.config['SITE_CONFIG']['name'],
                               site_logo=app.config['SITE_CONFIG']['logo'],
                               current_year=app.config['SITE_CONFIG']['current_year'],
                               related_posts=related[:3])

    @app.route('/tag/<tag_slug>')
    def tag_posts(tag_slug):
        all_posts = get_all_posts()
        filtered = [p for p in all_posts if tag_slug in (p['tags'] or '').split(',')]
        return render_template('tag.html',
                               posts=filtered,
                               tag=tag_slug.replace('-', ' ').title(),
                               site=app.config['SITE_CONFIG'])

    @app.route('/author/<author_slug>')
    def author_posts(author_slug):
        author_name = author_slug.replace('-', ' ').title()
        all_posts = get_all_posts()
        filtered = [p for p in all_posts if p['author'].lower().replace(' ', '-') == author_slug]
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
        return response

    @app.route('/image.png')
    def latest_blog_image():
        posts = get_all_posts()
        if not posts:
            abort(404)
        latest = posts[0]
        post_dir = os.path.join(BLOGS_DIR, latest['slug'])
        image_path = os.path.join(post_dir, 'image.png')
        if os.path.exists(image_path):
            return send_from_directory(post_dir, 'image.png', mimetype='image/png')
        abort(404)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    @app.template_filter('urlencode')
    def urlencode_filter(s):
        return quote(str(s))

    @app.template_filter('tag_list')
    def tag_list_filter(text):
        if not text: return []
        return [t.strip() for t in text.split(',') if t.strip()]

    @app.template_filter('markdown')
    def markdown_filter(text):
        if not text: return ''
        return render_markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])

    @app.route('/sitemap.xml')
    def sitemap():
        app.response_class.mimetype = 'application/xml'
        urls = [{
            'loc': url_for('index', _external=True),
            'lastmod': datetime.now().strftime('%Y-%m-%d'),
            'changefreq': 'daily',
            'priority': '1.0'
        }]
        all_posts = get_all_posts()
        for post in all_posts:
            urls.append({
                'loc': url_for('blog_post', slug=post['slug'], _external=True),
                'lastmod': post['published_date'],
                'changefreq': 'weekly',
                'priority': '0.8'
            })
        return render_template('sitemap.xml', urls=urls)

    @app.route('/robots.txt')
    def robots():
        app.response_class.mimetype = 'text/plain'
        return render_template('robots.txt', site_url=app.config['SITE_CONFIG']['url'])

    return app

if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=5000)
