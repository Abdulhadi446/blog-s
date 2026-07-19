from flask import Flask, render_template, abort, request, url_for
from datetime import datetime
import os
from urllib.parse import quote, unquote
import hashlib

def gravatar_url(email, size=200):
    email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

app = Flask(__name__)

# Sample blog data (in production, this would come from a database)
BLOG_POSTS = {
    'getting-started-with-python': {
        'title': 'Getting Started with Python: A Beginner\'s Guide',
        'description': 'Learn the fundamentals of Python programming with this comprehensive beginner\'s guide. Perfect for those new to coding.',
        'content': '''# Getting Started with Python

Python is one of the most popular programming languages in the world, and for good reason. It's **easy to learn**, **versatile**, and has a huge community of developers.

## Why Choose Python?

Python is perfect for beginners because:

- Simple and readable syntax
- Extensive standard library
- Large community support
- Cross-platform compatibility

## Your First Python Program

Let's start with the classic "Hello, World!" program:

```python
print("Hello, World!")
```

This simple line of code will output "Hello, World!" to the console.

## Variables and Data Types

Python has several built-in data types:

```python
# String
name = "John Doe"

# Integer
age = 25

# Float
height = 5.9

# Boolean
is_student = True

# List
hobbies = ["reading", "coding", "gaming"]
```

## Control Structures

### If Statements

```python
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

### Loops

```python
# For loop
for hobby in hobbies:
    print(f"I enjoy {hobby}")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
```

## Functions

Functions help organize your code:

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)
```

## Next Steps

Now that you know the basics, here are some next steps:

1. Practice with online coding platforms
2. Build small projects
3. Learn about libraries like NumPy and Pandas
4. Explore web frameworks like Flask or Django

> "The best way to learn programming is by practicing. Start small and build your way up!"

Happy coding! 🐍
''',
        'author': 'Jane Smith',
        'author_avatar': 'https://www.gravatar.com/avatar/1dac74dde9a4d23e7d37dd2fbd042bde?s=200&d=identicon',
        'author_url': '/author/jane-smith',
        'published_date': '2024-01-15T10:00:00Z',
        'published_date_formatted': 'January 15, 2024',
        'modified_date': '2024-01-15T10:00:00Z',
        'featured_image': 'https://datamites.com/blog/uploads/images/202408/image_750x_66ab59eeec745.jpg',
        'reading_time': 8,
        'keywords': 'python, programming, beginners, tutorial, coding',
        'tags': [
            {'name': 'Python', 'slug': 'python'},
            {'name': 'Programming', 'slug': 'programming'},
            {'name': 'Tutorial', 'slug': 'tutorial'}
        ],
        'url': '/blog/getting-started-with-python',
        'slug': 'getting-started-with-python'
    },
    'web-development-trends-2024': {
        'title': 'Web Development Trends to Watch in 2024',
        'description': 'Discover the latest web development trends that are shaping the industry in 2024. From AI integration to new frameworks.',
        'content': '''# Web Development Trends to Watch in 2024

The web development landscape is constantly evolving, and 2024 brings exciting new trends that are reshaping how we build and interact with websites.

## 1. AI-Powered Development

Artificial Intelligence is revolutionizing web development:

- **Code Generation**: Tools like GitHub Copilot and ChatGPT assist developers
- **Automated Testing**: AI-driven testing tools improve code quality
- **Personalization**: Dynamic content based on user behavior

## 2. Serverless Architecture

Serverless computing continues to gain popularity:

```javascript
// Example serverless function
exports.handler = async (event) => {
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
```

### Benefits:
- Reduced operational costs
- Automatic scaling
- Focus on code, not infrastructure

## 3. Progressive Web Apps (PWAs)

PWAs bridge the gap between web and mobile apps:

- Offline functionality
- Push notifications
- App-like experience
- Cross-platform compatibility

## 4. WebAssembly (WASM)

WebAssembly brings near-native performance to web browsers:

```c
// C code compiled to WebAssembly
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
```

## 5. Micro-Frontends

Breaking down monolithic frontends into smaller, manageable pieces:

- Independent deployment
- Technology diversity
- Team autonomy
- Scalability

## 6. Edge Computing

Moving computation closer to users:

- Reduced latency
- Improved performance
- Better user experience
- Global content delivery

## Conclusion

These trends are not just buzzwords – they're practical solutions that can improve your development workflow and user experience. Start experimenting with these technologies today!

> "The future belongs to those who adapt to change, not those who resist it."
''',
        'author': 'Mike Johnson',
        'author_avatar': 'https://www.gravatar.com/avatar/238d7ebd4d50cba6fa37be4b56e7716f?s=200&d=identicon',
        'author_url': '/author/mike-johnson',
        'published_date': '2024-02-20T14:30:00Z',
        'published_date_formatted': 'February 20, 2024',
        'modified_date': '2024-02-20T14:30:00Z',
        'featured_image': 'https://www.convergine.com/images/_1015x450_crop_center-center_none/Web-Development-Trends-of-2024_-Top-9-Insights.png',
        'reading_time': 6,
        'keywords': 'web development, trends, 2024, AI, serverless, PWA',
        'tags': [
            {'name': 'Web Development', 'slug': 'web-development'},
            {'name': 'Trends', 'slug': 'trends'},
            {'name': 'Technology', 'slug': 'technology'}
        ],
        'url': 'https://yourblog.com/blog/web-development-trends-2024',
        'slug': 'web-development-trends-2024'
    }
}

# Site configuration
SITE_CONFIG = {
    'name': 'TechBlog',
    'logo': '/static/images/logo.png',
    'description': 'Your go-to source for programming and technology insights',
    'url': 'https://yourblog.com',
    'author': 'TechBlog Team',
    'current_year': datetime.now().year
}

def get_related_posts(current_slug, limit=3):
    """Get related posts based on tags or simply return other posts"""
    related = []
    current_post = BLOG_POSTS.get(current_slug)
    
    if not current_post:
        return []
    
    current_tags = [tag['slug'] for tag in current_post.get('tags', [])]
    
    for slug, post in BLOG_POSTS.items():
        if slug == current_slug:
            continue
            
        post_tags = [tag['slug'] for tag in post.get('tags', [])]
        
        # Check if posts share any tags
        if any(tag in current_tags for tag in post_tags):
            related.append({
                'title': post['title'],
                'excerpt': post['description'],
                'url': url_for('blog_post', slug=slug)
            })
    
    return related[:limit]

@app.route('/')
def index():
    """Homepage with blog list"""
    posts = []
    for slug, post in BLOG_POSTS.items():
        posts.append({
            'title': post['title'],
            'description': post['description'],
            'author': post['author'],
            'published_date_formatted': post['published_date_formatted'],
            'reading_time': post['reading_time'],
            'featured_image': post.get('featured_image'),
            'url': url_for('blog_post', slug=slug),
            'tags': post.get('tags', [])
        })
    
    return render_template('index.html', posts=posts, site=SITE_CONFIG)
    
@app.route('/blog')
def blog_list():
    """Blog listing page"""
    return index()  # Redirect to homepage for now

@app.route('/blog/<slug>')
def blog_post(slug):
    """Individual blog post page"""
    if slug not in BLOG_POSTS:
        abort(404)
    
    post = BLOG_POSTS[slug].copy()
    post['url'] = request.url
    
    # Get related posts
    related_posts = get_related_posts(slug)
    
    return render_template('blog.html', 
                         blog=post,
                         site_name=SITE_CONFIG['name'],
                         site_logo=SITE_CONFIG['logo'],
                         current_year=SITE_CONFIG['current_year'],
                         related_posts=related_posts)

@app.route('/tag/<tag_slug>')
def tag_posts(tag_slug):
    """Posts filtered by tag"""
    filtered_posts = []
    for slug, post in BLOG_POSTS.items():
        post_tags = [tag['slug'] for tag in post.get('tags', [])]
        if tag_slug in post_tags:
            filtered_posts.append({
                'title': post['title'],
                'description': post['description'],
                'author': post['author'],
                'published_date_formatted': post['published_date_formatted'],
                'reading_time': post['reading_time'],
                'featured_image': post.get('featured_image'),
                'url': url_for('blog_post', slug=slug),
                'tags': post.get('tags', [])
            })
    
    return render_template('tag.html', 
                         posts=filtered_posts,
                         tag=tag_slug.replace('-', ' ').title(),
                         site=SITE_CONFIG)

@app.route('/author/<author_slug>')
def author_posts(author_slug):
    """Posts filtered by author"""
    author_name = author_slug.replace('-', ' ').title()
    filtered_posts = []
    
    for slug, post in BLOG_POSTS.items():
        if post['author'].lower().replace(' ', '-') == author_slug:
            filtered_posts.append({
                'title': post['title'],
                'description': post['description'],
                'author': post['author'],
                'published_date_formatted': post['published_date_formatted'],
                'reading_time': post['reading_time'],
                'featured_image': post.get('featured_image'),
                'url': url_for('blog_post', slug=slug),
                'tags': post.get('tags', [])
            })
    
    return render_template('author.html',
                         posts=filtered_posts,
                         author=author_name,
                         site=SITE_CONFIG)

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap for SEO"""
    app.response_class.mimetype = 'application/xml'
    
    urls = []
    
    # Add homepage
    urls.append({
        'loc': url_for('index', _external=True),
        'lastmod': datetime.now().strftime('%Y-%m-%d'),
        'changefreq': 'daily',
        'priority': '1.0'
    })
    
    # Add blog posts
    for slug, post in BLOG_POSTS.items():
        urls.append({
            'loc': url_for('blog_post', slug=slug, _external=True),
            'lastmod': post['modified_date'][:10],
            'changefreq': 'weekly',
            'priority': '0.8'
        })
    
    return render_template('sitemap.xml', urls=urls)

@app.route('/robots.txt')
def robots():
    """Robots.txt for SEO"""
    app.response_class.mimetype = 'text/plain'
    return render_template('robots.txt', site_url=SITE_CONFIG['url'])

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 page"""
    return render_template('404.html', site=SITE_CONFIG), 404

# Template filters
@app.template_filter('urlencode')
def urlencode_filter(s):
    """URL encode filter for Jinja2"""
    return quote(str(s))

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/images', exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5000)