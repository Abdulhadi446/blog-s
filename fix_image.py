import os
import requests
from PIL import Image

def main():
    blog_dir = "/home/ubuntu/blog-s/blogs/ai-news-October-23-formal-verification-openshell"
    img_path = os.path.join(blog_dir, "image.png")
    url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/1200px-ChatGPT_logo.svg.png"
    
    print(f"Downloading fallback image from {url}")
    try:
        resp = requests.get(url, timeout=10)
        with open(img_path, 'wb') as f:
            f.write(resp.content)
        
        img = Image.open(img_path)
        # Convert to RGB for PNG/JPG compatibility
        img = img.convert('RGB')
        target_w, target_h = 1920, 1080
        src_ratio = img.width / img.height
        tgt_ratio = target_w / target_h
        if src_ratio > tgt_ratio:
            new_h = img.height
            new_w = int(new_h * tgt_ratio)
        else:
            new_w = img.width
            new_h = int(new_w / tgt_ratio)
        left = (img.width - new_w) // 2
        top = (img.height - new_h) // 2
        img = img.crop((left, top, left + new_w, top + new_h))
        img = img.resize((target_w, target_h), Image.LANCZOS)
        img.save(img_path)
        print("Done")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
