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
| 2026-08-20 | [AI Daily Roundup: OpenAI 20% Compute Overhead, Microsoft Copilot Flaw, Unitree $66B IPO, Samsung Foundry Hikes, Google Student Gemini, Cerebras CS-4](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-august-20-openai-microsoft-unitree-samsung-cerebras) |
| 2026-08-19 | [AI Daily Roundup – August 19, 2026: OpenAI ChatGPT for Teens, CISA Ray RCE Patch, Nebius $4.5B Notes, Temporal $12B+ Valuation, Unitree 629% IPO Pop, Cerebras CS-4 30x Speed, Anthropic Protein Binders, 18 Stories](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-august-19-openai-teens-cisa-ray-nebius-temporal-unitree-cerebras-anthropic-protein) |
| 2026-08-19 | [AI Daily Roundup – August 19, 2026: Stripe Buys OpenRouter $7B+, GPT-5.6 Luna Free Unlimited, Gemini 1B Users, DeepSeek Price Hike, Anthropic Watermarks, Claude Code Auto, 18 Stories](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-august-19-2026-stripe-openrouter-gemini-deepseek-anthropic-claude-code) |
| 2026-08-18 | [AI Daily Roundup – August 18, 2026: Nvidia $105B OpenAI Ohio Data Center, Anthropic $65B Revenue, Copilot Deep Research Ends, Cursor Origin Launches, DOJ Probes a16z](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-august-18-nvidia-105b-openai-anthropic-65b-copilot-deep-research-cursor-origin-doj-a16z) |
| 2026-08-17 | [AI Daily Roundup – August 17, 2026: Stripe Buys OpenRouter for $7B, GPT-5.6 Luna Free Tier, Gemini 1B Users, DeepSeek Price Hike, 12 Stories](https://blogs.thetrillioniar.me/blog/ai-daily-roundup-2026-08-17) |
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
```