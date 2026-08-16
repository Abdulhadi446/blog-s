# [TechBlog](https://blogs.thetrillioniar.me/)

A modern, file-based blog platform built with Flask. Write posts in Markdown, manage content through an admin panel, and deploy with ease.

## Features

- **Markdown-Based Content** - Write blog posts in Markdown with YAML frontmatter
- **Admin Panel** - Secure admin interface for creating and managing posts
- **File-Based Storage** - Posts stored as individual folders with markdown and images
- **SEO Optimized** - Built-in sitemap.xml and robots.txt generation
- **Image Support** - Each post can have a featured image (image.png)
- **Search** - DuckDuckGo image search integration
- **Gravatar Support** - Automatic author avatar generation
- **Responsive Design** - Mobile-friendly templates
- **SQLite Database** - Lightweight database for metadata and sessions

## Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (via Flask-SQLAlchemy)
- **Templating**: Jinja2
- **Markdown Rendering**: Python markdown library
- **Web Scraping**: BeautifulSoup4
- **Search**: DuckDuckGo Search API

## All Blogs

| Date | Blog Post |
|------|-----------|
| 2026-08-16 | [AI Daily Roundup – August 16, 2026: Anthropic Model 2 Shelved, DeepSeek V4-Pro Price Shock, Qwen 3.8 27B, Gemini 3.7 Flash](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-08-16) |
| 2026-08-15 | [Muse Glimmer, Gemini Billion-User Milestone, and OpenAI Cyber Model](https://blogs.thetrillioniar.me/blog/ai-news-august-15-muse-glimmer-gemini-cohack) |
| 2026-08-14 | [AI Daily Roundup: GPT-5.6 Sol's 14X Speed, Claude Code Auto-Mode, and DeepMind's Shakeup](https://blogs.thetrillioniar.me/blog/ai-news-august-14-gpt56-sol-claude-auto-deepmind-chips) |
| 2026-08-13 | [AI News August 13: Humanoid Cleaners Hit SF, Suno Scales to 100M Users, and the 1 Trillion Liter Water Crisis](https://blogs.thetrillioniar.me/blog/ai-news-august-13-tau-robotics-suno-water-accel) |
| 2026-08-12 | [AI News August 12 – Nvidias 500B Alliance, Gemini 1B Users, Anthropic Riot Deal, CoT Attack](https://blogs.thetrillioniar.me/blog/ai-news-august-12-nvidia-500b-gemini-1b-anthropic-compute-cot-attack) |
| 2026-08-11 | [Meta Muse Glimmer Drops 30B Open Weights, OpenAI Ships Cybersecurity Model, and Intel Raises $15B for AI](https://blogs.thetrillioniar.me/blog/ai-news-august-11-meta-muse-glimmer-openai-cyber-intel-15b) |
| 2026-08-10 | [AI News August 10: Grok Imagine 2.0 Takes #2 on Arena, 500 US Data-Center Bans, Apple Tests Chinese Chips](https://blogs.thetrillioniar.me/blog/ai-news-august-10-grok-imagine-data-center-bans-apple-china-agents) |
| 2026-08-09 | [AI News August 9: OpenAI Astra Solves 10 Math Problems, EU AI Act Goes Live, DeepGrove Maple Runs at 127 tok/s on iPhone](https://blogs.thetrillioniar.me/blog/ai-news-august-9-openai-astra-eu-ai-act-maple-astera-labs-claude-fable) |

## Project Structure

```blog-s/
├── app.py              # Main Flask application
├── config.py           # Configuration classes
├── wsgi.py             # WSGI entry point for production
├── requirements.txt    # Python dependencies
├── start.sh            # Quick start script
├── blogs/              # Blog posts directory
│   └── <slug>/
│       ├── blog.md     # Post content (Markdown)
│       └── image.png   # Featured image
├── templates/          # HTML templates
├── static/             # Static assets (CSS, JS, images)
├── instance/           # Flask instance folder (secrets, DB)
├── logs/               # Application logs
└── pass.txt            # Admin password file
