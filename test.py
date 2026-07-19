import hashlib

from sqlalchemy import PrimaryKeyConstraint

def gravatar_url(email, size=200):
    email_hash = hashlib.md5(email.strip().lower().encode()).hexdigest()
    return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

import requests
import re
import time
from bs4 import BeautifulSoup

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
                print(f"⏱️ Fetched in {elapsed:.3f} seconds")
                return match.group(1)

        elapsed = time.time() - start_time
        print(f"⏱️ Fetched in {elapsed:.3f} seconds")
        return None

    except Exception as e:
        print(f"Bing error: {e}")
        return None

# # # Example usage
# # query = "getting-started-with-python"
# # image_url = fetch_first_bing_image(query)
# # if image_url:
# #     print("✅ Found image:", image_url)
# # else:
# #     print("❌ No image found.")

# def Images(username, blog_title):
#     avatar = gravatar_url(username + "@example.com")
#     image = fetch_first_bing_image(blog_title)
#     return avatar, image


# avatar, image = Images("Abdul Hadi", "Python Programming Basics")

# print("Avatar URL:", avatar)
# print("Blog Image URL:", image)

from flask import Flask, render_template, request, redirect, url_for, flash
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

@app.route('/upload', methods=['GET'])
def handle_upload():
    """Handle both the upload form display and form submission"""
    
    # If no query parameters, show the form
    if not request.args:
        return render_template('upload.html')
    
    # If query parameters exist, process the form data
    try:
        # Get all parameters from query string
        slug = request.args.get('slug', '')
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        author_image = gravatar_url(author + "@example.com")
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
                # Clean up the tags string and parse it
                tags_clean = tags.replace("'", '"')
                # Split by comma and parse each tag object
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
                # Fallback: create simple tag objects from comma-separated values
                tag_names = tags.split(',')
                tag_objects = [
                    {
                        'name': tag.strip(),
                        'slug': tag.strip().lower().replace(' ', '-')
                    }
                    for tag in tag_names if tag.strip()
                ]
        
        # Print all the data one by one
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
        # print(f"URL Path: {url_path}")
        # print(f"URL Slug: {url_slug}")
        print("-" * 30)
        print("PROCESSED DATA:")
        print("-" * 30)
        print(f"Keywords List: {keywords.split(',') if keywords else []}")
        print(f"Tag Objects: {tag_objects}")
        print(f"Timestamp: {datetime.now().isoformat()}")
        print("=" * 50)
        
        flash(f'Blog post "{title}" data printed to console!', 'success')
        return redirect(url_for('handle_upload'))
        
    except Exception as e:
        flash(f'Error processing upload: {str(e)}', 'error')
        return redirect(url_for('handle_upload'))

# Removed save_blog_post function and blog_posts route since we're just printing data

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    flash('Page not found', 'error')
    return redirect(url_for('handle_upload'))

if __name__ == '__main__':
    app.run(debug=True)