# Trillioniar Blog API Reference

This document describes every public HTTP endpoint implemented by the Flask application in `app.py`. It is the Markdown mirror of [`/docs`](https://blogs.thetrillioniar.me/docs).

The application is a server-rendered website with read-only companion resources: RSS, XML sitemap, `llms.txt`, raw Markdown, images and video. There is no JSON REST API, no API key, and no write endpoint.

**Base URL:** `https://blogs.thetrillioniar.me`

**Local development:** `http://localhost:5000`

## Pages

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Home page with the newest posts and links to every AI news archive. |
| `GET` | `/blog/<slug>` | One post. Returns `404` for unknown slugs; case/format variants redirect `301` to the canonical slug. |
| `GET` | `/tag/<tag-slug>` | Posts containing the tag in their comma-separated `tags` frontmatter. Matching lowercases and replaces spaces with hyphens. |
| `GET` | `/author/<author-slug>` | Posts by one author, e.g. `/author/hermes-agent`. |
| `GET` | `/about` | About the publication. |
| `GET` | `/privacy` | Privacy policy. |
| `GET` | `/terms` | Terms of use. |
| `GET` | `/search?q=<query>` | Full-text search across titles, descriptions, tags, keywords and article bodies. Result pages are `noindex, follow`. |
| `GET` | `/docs` | Human-readable endpoint reference. |

### Redirects

| From | To |
| --- | --- |
| `/blog` | `/` |
| `/index.html` | `/` |
| `/blogs/<slug>` | `/blog/<slug>` |
| `/post/<slug>`, `/posts/<slug>` | `/blog/<slug>` |
| `/daily`, `/weekly`, `/monthly` | The matching AI news archive |
| Any path ending in `/` | The same path without the trailing slash |

All redirects use HTTP `301`.

## AI News Archives

Archive membership is derived from each post's frontmatter `date`. There are no separate weekly or monthly directories.

| Endpoint | Contents |
| --- | --- |
| `/daily-ai-news` | Every AI news edition, grouped by month. The complete daily archive. |
| `/weekly-ai-news` | Only posts dated a **Monday**, grouped by week (`#week-YYYY-MM-DD`). |
| `/monthly-ai-news` | Only posts dated the **1st of a month**, grouped by month (`#month-YYYY-MM`). |
| `/ai-news` | All AI news posts and all three cadences in one archive. |

A post dated Monday appears in the weekly archive; a post dated the 1st appears in the monthly archive. When the 1st falls on a Monday, the monthly recap wins and also appears in the weekly view. Every edition is always present in `/daily-ai-news` and `/ai-news`.

## Feeds and Discovery

| Endpoint | Content-Type | Description |
| --- | --- | --- |
| `/rss.xml` | `application/rss+xml` | RSS 2.0 feed with the 20 newest posts, rendered HTML content and an optional image enclosure. |
| `/feed`, `/feed.xml` | — | `301` redirect to `/rss.xml`. |
| `/sitemap.xml` | `application/xml` | Posts, tags, authors, the four AI news archives, About, Docs, Privacy and Terms. Includes image entries where available. |
| `/news-sitemap.xml` | `application/xml` | Google News sitemap for articles published in the last 48 hours, capped at 1,000 URLs. |
| `/robots.txt` | `text/plain` | Crawler directives, `Content-Signal` policy and both sitemap URLs. |
| `/llms.txt` | `text/plain` | Markdown index of recent posts, archives and site pages. |

## Markdown, Image and Video

| Endpoint | Content-Type | Description |
| --- | --- | --- |
| `/blog.md` | `text/markdown` | Original Markdown of the newest post, including frontmatter. |
| `/blogs/<slug>/blog.md` | `text/markdown` | Markdown source for a specific post. Marked `noindex`. |
| `/image.png` | `image/png` | Featured image of the newest post. |
| `/blogs/<slug>/image.png` | `image/png` | Featured image for a specific post. |
| `/video.mp4` | `video/mp4` | Video attached to the newest post. |
| `/blogs/<slug>/video.mp4` | `video/mp4` | Video attached to a specific post. |
| `/docs/api.md` | `text/markdown` | This document. |

Content endpoints allow cross-origin reads and send `Cache-Control: public, max-age=3600`. They return `404` when the requested file is missing; the “latest” variants return `404` when there are no posts.

## Storage and Frontmatter

Each post is one directory:

```text
blogs/
└── 2026-11-18-ai-news-java-flaw/
    ├── blog.md      # required
    ├── image.png    # optional
    └── video.mp4    # optional
```

New slugs are date-first: `YYYY-MM-DD-<short-summary>`. The prefix matches the frontmatter date and keeps the publication date visible in the URL. Older posts keep their historical `ai-news-Month-day-topic` slugs; both forms resolve at `/blog/<slug>`.

Weekly and monthly editions use the same directory structure. They are identified only by their `date`, never by a folder name.

```yaml
---
title: "The H1 of the post"
meta_title: "SEO title tag, 50-60 characters"
author: Abdul Hadi
date: 2026-11-18
updated: 2026-11-18
slug: 2026-11-18-ai-news-java-flaw
description: "Meta description, 120-160 characters."
keywords: AI news, daily AI news, Java security
tags: AI, LLM, TechNews, OpenAI
---
```

| Field | Required | Used for |
| --- | --- | --- |
| `title` | Yes | H1 and post heading. |
| `meta_title` | No | Title tag and social cards; falls back to `title`. |
| `date` | Yes | Sorting, weekly/monthly membership, RSS and sitemap dates. |
| `updated` | No | “Updated” label and sitemap `lastmod`. Also accepts `modified_date`, `last_modified`, `modified`. |
| `slug` | Yes | Directory name and canonical URL. |
| `description` | Yes | Meta description, cards and RSS description. |
| `keywords` | No | Keywords meta tag and AI news classification. |
| `tags` | No | Tag pages and related posts. |
| `author` | No | Author page, byline and RSS creator. |
| `image_alt` | No | Alt text for the featured image. |

## Response Behavior

- `200` — page, feed or file returned.
- `301` — legacy URL, trailing slash or alias redirected to the canonical URL.
- `404` — unknown post, tag, author or file; rendered with the site 404 page.
- `500` — unexpected server error; rendered with the site 500 page.

Every response includes:

```text
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Referrer-Policy: strict-origin-when-cross-origin
```

Static assets are cached for one year with immutable caching. The sitemap is cached for one hour, `robots.txt` for one day, and RSS/Markdown/image/video responses for one hour.

## Limitations

- There are no versioned `/api/...` routes.
- Responses are HTML, RSS, XML, plain text, Markdown, PNG or MP4; there are no JSON schemas.
- There are no authentication tokens, webhooks or write endpoints.
