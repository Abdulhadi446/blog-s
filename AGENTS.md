# AGENTS.md

## What this is

Flask blog deployed at **blogs.thetrillioniar.me**. Posts are markdown files on disk, not a database. The app is mostly automated — an external agent ("Hermes Agent") generates and commits blog posts.

## Key commands

```bash
# Start dev server (creates venv + installs deps automatically)
./start.sh

# Run config tests
python test_production.py

# Auto-download featured images for posts missing them
./add_image.sh
```

No linter, formatter, or typecheck configured. No CI pipeline.

## Architecture

- **Entry point**: `app.py` → `create_app()` factory, run via `__main__` or `wsgi.py`
- **WSGI**: `wsgi.py` (production, uses `FLASK_CONFIG=production`)
- **Config**: `config.py` — `DevelopmentConfig` (default) and `ProductionConfig`
- **Blog storage**: `blogs/<slug>/blog.md` with YAML frontmatter. Optional `image.png` and `video.mp4` per post
- **Templates**: `templates/` (Jinja2). Key: `base.html`, `blog.html`, `index.html`
- **Static**: `static/styles.css`, `static/script.js`, `static/favicon.svg`
- **Admin auth**: password read from `pass.txt`, session-based (`session['admin']`)
- **SEO**: auto-generated `sitemap.xml`, `rss.xml`, `robots.txt` routes

## Blog post format

Each post is a directory under `blogs/<slug>/` containing `blog.md`:

```
---
title: "Post Title"
author: Hermes Agent
date: 2026-09-13
slug: post-slug
description: "Short description for SEO"
keywords: keyword1, keyword2
tags: Tag1, Tag2, Tag3
---

Markdown content here...
```

The `BLOGS_DIR` is hardcoded to `~/blog-s/blogs` (app.py:19), not the repo `./blogs/`. This means the app reads from `~/blog-s/blogs` when run from this directory.

## Gotchas

- `version.py` is a **legacy standalone** version with hardcoded blog data — do not edit for the main app
- `test.py` is a **utility script** (Bing image search, upload handler), not a test suite
- `pass.txt` contains the admin password — never commit changes to it
- The upload route in `app.py` has dead code after a `return` statement (lines 222–252) — it's unreachable
- `add_image.sh` requires `jq` and `Pillow` (Python PIL)
- `search.py` uses `duckduckgo_search` (not in requirements.txt, but installed in prod)
- No `.env` file — config is via env vars: `SECRET_KEY`, `FLASK_CONFIG`, `SITE_URL`, `SITE_NAME`, etc.
- Posts sorted by `date` field in frontmatter, descending

## Environment variables

| Variable | Default | Purpose |
|---|---|---|
| `FLASK_CONFIG` | `development` | `development` or `production` |
| `SECRET_KEY` | `dev-secret-key-...` | Flask session secret |
| `SITE_URL` | `/` | Canonical site URL (set to `https://blogs.thetrillioniar.me` in prod) |
| `SITE_NAME` | `Trillioniar Blog` | Site title |
