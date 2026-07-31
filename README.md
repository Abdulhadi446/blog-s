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
| 2026-07-31 | [Claude Breaches Three Organizations in Cyber Tests, DeepMind Ships Gemini Robotics 2, and AWS Posts Record 37% Growth](https://blogs.thetrillioniar.me/blog/ai-news-july-31-claude-cyber-breach-gemini-robotics-aws-nscale) |
| 2026-07-30 | [AI News July 30: Microsoft Azure $100B, Samsung 1,814% Profit Surge, RufRoot CVSS 10.0, and Onyx Security $113M](https://blogs.thetrillioniar.me/blog/ai-news-july-30-microsoft-azure-meta-samsung-ruflo-onyx) |
| 2026-07-29 | [OpenAI's Rogue Agent Hacks Second Firm, Nasdaq Nears Correction, and Nvidia Launches Open Secure AI Alliance](https://blogs.thetrillioniar.me/blog/ai-news-july-29-rogue-agent-nasdaq-correction-open-secure-ai) |
| 2026-07-28 | [Nvidia Bets $5B on Sutskever's SSI, Microsoft Ships Cyber AI, and a Universal Jailbreak Breaks GPT-5.6 and Claude Opus 5](https://blogs.thetrillioniar.me/blog/ai-news-july-28-nvidia-ssi-microsoft-cybersecurity-eu-ai-act) |
| 2026-07-27 | [Kimi K3 Open Weights Drop, Anthropic Builds Custom Chips, and AI Finds 19 Redis Zero-Days](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-27) |
| 2026-07-26 | [AI Daily Roundup: Claude Opus 5, OpenAI Sandbox Escape, and the Open-Weight Revolution](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-26) |
| 2026-07-25 | [AI Daily Roundup – July 25, 2026: Claude Opus 5, Prentis AI Lab, and the Geopolitics of Model Distillation](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-25) |
| 2026-07-24 | [AI Daily Roundup – 2026-07-24](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-24) |
| 2026-07-23 | [AI Daily Roundup: Gemini 3.6 Flash, Claude Sonnet 5, Kimi K3, and July 2026's Monumental Shifts](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-23) |
| 2026-07-22 | [AI Daily Roundup – 2026-07-22](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-22) |
| 2026-07-21 | [AI Daily Roundup – 2026-07-21](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-21) |
| 2026-07-20 | [AI Daily Roundup – 2026-07-20](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-07-20) |
| 2026-07-20 | [Kimi K3 – The 2.8 Trillion-Parameter Open-Weight Model That's Reshaping AI](https://blogs.thetrillioniar.me/blog/kimi-k3-2.8-trillion-open-weight-model-reshaping-ai) |
| 2026-07-19 | [International AI Safety Report 2026](https://blogs.thetrillioniar.me/blog/international-ai-safety-report-2026) |


## Project Structure

```
blog-s/
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
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Quick Start

1. Clone the repository:

```bash
git clone <repository-url>
cd blog-s
```

2. Run the start script (creates venv and installs dependencies):

```bash
chmod +x start.sh
./start.sh
```

Or manually:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

3. Open your browser and navigate to `http://localhost:5000`

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_CONFIG` | Configuration mode (`development`/`production`) | `development` |
| `SECRET_KEY` | Flask secret key | `dev-secret-key-change-in-production` |
| `DATABASE_URL` | SQLite database URI | `sqlite:///blog.db` |
| `SITE_NAME` | Blog name | `TechBlog` |
| `SITE_DESCRIPTION` | Blog description | Your go-to source... |
| `SITE_AUTHOR` | Default author name | `TechBlog Team` |

### Admin Access

Set your admin password in `pass.txt`:

```bash
echo "your-secure-password" > pass.txt
```

Access the admin panel at `/admin/login`.

## Creating Blog Posts

Create a new folder in `blogs/` with a URL-friendly slug:

```bash
mkdir blogs/my-new-post
```

Create a `blog.md` file with frontmatter:

```markdown
---
title: My New Post
author: John Doe
date: 2024-01-15
description: A brief description of the post
tags: python, flask, tutorial
---

# My New Post

Your content here...

## Subheading

More content...
```

Optionally add an `image.png` to the same folder for a featured image.

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Post title |
| `author` | No | Author name |
| `date` | No | Publication date (YYYY-MM-DD) |
| `description` | No | Short description for SEO |
| `tags` | No | Comma-separated tags |

## Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn wsgi:application -b 0.0.0.0:8000
```

### Using the Start Script

```bash
export FLASK_CONFIG=production
./start.sh
```

## Development

### Running in Development Mode

```bash
export FLASK_CONFIG=development
python app.py
```

The development server runs on `http://localhost:5000` with debug mode enabled.

### Adding Dependencies

```bash
pip install <package>
pip freeze > requirements.txt
```

## License

MIT License - see [LICENSE](LICENSE) for details.
