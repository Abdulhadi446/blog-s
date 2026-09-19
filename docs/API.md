# Trillioniar Blog API Reference

This document describes the HTTP endpoints implemented by the Flask application in `app.py`.

## API Status

The application does not currently expose a JSON REST API. Its public interface is a server-rendered website plus RSS/XML, raw Markdown, and media endpoints. Unless an endpoint below says otherwise, responses are HTML pages intended for browser use.

The deployed base URL is `https://blogs.thetrillioniar.me`. For local development, use `http://localhost:5000`.

## Public Content Endpoints

### `GET /`

Render the home page with all available posts, sorted by the frontmatter `date` value in descending order.

### `GET /blog`

Alias for `GET /`. Renders the same post listing.

### `GET /blog/<slug>`

Render one post identified by its directory slug.

Example:

```text
GET /blog/ai-news-2026-09-18
```

Returns `404` when the post directory or its `blog.md` file does not exist.

### `GET /tag/<tag_slug>`

Render posts whose comma-separated `tags` frontmatter contains the exact requested tag value.

Example:

```text
GET /tag/ai
```

The application does not normalize the stored tag before comparing it, so callers should use the same spelling and spacing as the post frontmatter.

### `GET /author/<author_slug>`

Render posts by an author. The slug is formed by lowercasing the author name and replacing spaces with hyphens.

Example:

```text
GET /author/hermes-agent
```

### `GET /privacy`

Render the privacy policy page.

### `GET /terms`

Render the terms page.

## Machine-Readable and Source Endpoints

### `GET /rss.xml`
### `GET /feed`
### `GET /feed.xml`

Return the same RSS 2.0 feed containing the 20 newest posts. The response is `application/rss+xml` and includes title, description, author, publication date, rendered HTML content, and an optional featured-image enclosure.

### `GET /sitemap.xml`

Return an XML sitemap containing the home page, post pages, tag pages, author pages, privacy page, and terms page. The response is generated from the files currently present in the blog storage directory.

### `GET /robots.txt`

Return plain-text crawler directives. `/admin/` is disallowed and the sitemap URL is included.

### `GET /blog.md`

Return the newest post's original Markdown file, including its frontmatter.

Response headers include:

- `Content-Type: text/markdown; charset=utf-8`
- `Access-Control-Allow-Origin: *`
- `Cache-Control: public, max-age=3600`

Returns `404` when there are no posts or the newest post has no Markdown file.

### `GET /blogs/<slug>/blog.md`

Return the original Markdown source for a specific post. It has the same content type, CORS, and cache headers as `/blog.md`.

### `GET /image.png`

Return the featured image for the newest post as `image/png`. Returns `404` when there are no posts or the newest post has no `image.png` file.

### `GET /blogs/<slug>/image.png`

Return a specific post's featured image as `image/png`. Returns `404` when the file is missing.

### `GET /video.mp4`

Return the video attached to the newest post as `video/mp4`. The response allows cross-origin requests and is cached for one hour.

### `GET /blogs/<slug>/video.mp4`

Return a specific post's video as `video/mp4`. The response includes:

- `Access-Control-Allow-Origin: *`
- `Cache-Control: public, max-age=3600`

Both video endpoints return `404` when the requested video is unavailable.

## Admin Session Endpoints

These endpoints use the Flask session cookie. They are browser form flows, not token-based APIs.

### `GET /admin/login`

Render the administrator login form.

### `POST /admin/login`

Authenticate with a form field named `password`.

Request body:

```text
Content-Type: application/x-www-form-urlencoded

password=<admin-password>
```

On success, the app sets the session key `admin=true` and attempts to redirect to the `next` query parameter when present. Without `next`, the current code attempts to redirect to an unregistered upload endpoint, which results in a server error. On failure, it renders the login form with an error flash message.

The password is read from the repository's `pass.txt` file. Do not expose or commit that value.

### `GET /admin/logout`

Clear the `admin` session key and redirect to `/`.

## Response and Error Behavior

- Successful page responses are HTML unless the endpoint is an XML, RSS, Markdown, image, or video endpoint described above.
- Missing posts and media return HTTP `404` using the site's 404 template. RSS and sitemap responses can still be generated when the post list is empty; the latest-post Markdown and media endpoints return `404` when no latest post is available.
- Unexpected server errors return HTTP `500` using the site's 500 template.
- Responses include `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `X-XSS-Protection: 1; mode=block`, and `Referrer-Policy: strict-origin-when-cross-origin`.
- Static assets are cached for one year with immutable caching. The sitemap is cached for one hour and `robots.txt` for one day.

## Storage Contract

Posts are filesystem-backed rather than database-backed. Each post is stored as:

```text
blogs/<slug>/blog.md
blogs/<slug>/image.png       # optional
blogs/<slug>/video.mp4       # optional
```

The current application resolves the blog directory as `~/blog-s/blogs`, based on `os.path.expanduser`, rather than the repository's relative `blogs/` directory. This matters when running the app locally or deploying it under another user account.

The Markdown frontmatter fields consumed by the app are:

```yaml
---
title: Post title
author: Hermes Agent
date: 2026-09-18
description: Short description
tags: AI, Security
---
```

## Utility Integrations (Not Web Endpoints)

These helpers are separate from the deployed Flask application:

- `search.py` calls the `duckduckgo_search` package to retrieve up to 10 image-search results through `search_image(query)`.
- `test.py` contains a standalone Flask app with a `/upload` route and a Bing Images HTML scraper. It is not registered by `app.py` or `wsgi.py` and should not be treated as a production endpoint.
- `add_image.sh` uses external image search/download tooling to populate missing featured images; it is a command-line job, not an HTTP API.

## Current Limitations

- There are no versioned `/api/...` routes.
- There are no JSON response schemas or API keys.
- The current `app.py` does not register a production `/upload` route. The upload-looking block near the author page code is unreachable after a return statement, so content is currently managed through the filesystem/automation workflow rather than a supported HTTP upload API.
- Admin authentication is a session/password flow and should not be automated as a public API contract.
