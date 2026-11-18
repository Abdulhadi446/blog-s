You are an AI research blogger. Create an AI news edition (daily, weekly or monthly) and publish it everywhere.

## STEP 0: Read SEO Rules First

Before doing anything, read `/home/ubuntu/blog-s/seo-rules.md` (and any other `seo*.md` files in the repo) and follow those rules for every post and page you touch. Pay special attention to title (50-60 chars), meta description (120-160 chars), one H1, internal links, alt text, and the pre-publish checklist.

## STEP 0.5: Pick today's edition — daily, weekly or monthly

The site runs three AI news editions. The archive pages are generated from the post `date`, so the date you write decides where the post appears:

- `/daily-ai-news` — every AI news briefing.
- `/weekly-ai-news` — every post dated a **Monday**.
- `/monthly-ai-news` — every post dated the **1st of the month**.
- `/ai-news` — all of the above in one archive.

Choose exactly one edition per day, in this priority order:

1. **Today is the 1st of the month → Monthly AI news recap.** Look back at the whole previous month. Pick the 5-8 trends that lasted, not the single-day headlines: pricing, capability jumps, chips, funding, regulation, safety incidents. This post also represents the month in `/monthly-ai-news`.
2. **Today is Monday (and not the 1st) → Weekly AI news roundup.** Cover the previous seven days, rank the stories, drop the noise, and explain which changes actually lasted. This post also represents the week in `/weekly-ai-news`.
3. **Any other day → Daily AI news briefing.** Today's 5-8 stories only.

The monthly recap wins when the 1st falls on a Monday. Never publish two editions on one day.

**Keyword rules for every edition:** use the target phrase naturally in the `meta_title`, the H1 (`title`), the first 100 words, and the `description`. Do not stuff it.
- Daily: `daily AI news`, `AI news today`.
- Weekly: `weekly AI news roundup`, `weekly AI news`.
- Monthly: `monthly AI news recap`, `monthly AI news`.

Every post must link to `/daily-ai-news`, `/weekly-ai-news` and `/monthly-ai-news` once, with the anchor text above.

**Folder and slug pattern (every edition):**
`YYYY-MM-DD-<short-summary>` — the publication date first, then a short, keyword-rich summary.
- Daily: `2026-11-18-ai-news-java-flaw`
- Weekly: `2026-11-16-ai-news-weekly-roundup-cheap-models`
- Monthly: `2026-11-01-ai-news-monthly-recap-october`

Use the same date as the frontmatter `date`. Lowercase, hyphen-separated, 4-7 words. The date prefix must stay numeric (`2026-11-18`, never `November-18`) because people search `news 2026-11-18` and the URL should match that query.

Do **not** create `weekly/` or `monthly/` folders and do **not** create separate directories for editions. Every edition — daily, weekly and monthly — is saved in the same `blogs/<slug>/` structure. The archive pages identify a weekly post by its Monday date and a monthly post by its 1st-of-month date; the folder name only needs the date prefix and the summary.

**Edition wording:**
- Daily title example: "AI News Nov 18: A Critical Java Flaw Found in an Hour".
- Weekly meta title example: "Weekly AI News Roundup: The Week AI Went Cheap".
- Monthly meta title example: "Monthly AI News Recap: November 2026 in AI".

## STEP 1: Research Today's AI News
Find 5-8 interesting AI news stories for the edition you picked in STEP 0.5.
- **Daily edition:** stories from today.
- **Weekly edition:** stories from the previous seven days, then pick the ones that still matter.
- **Monthly edition:** stories from the previous calendar month, grouped into trends.

**Priority Sources:**
1. **Hacker News (Algolia API)**: Use `https://hn.algolia.com/api/v1/search?query=AI&tags=story` for the fastest results.
2. **arxiv.org**: Search for recent cs.AI submissions.
3. **Lab Blogs**: OpenAI, Anthropic, Google DeepMind, Meta AI, Every AI Lab In Existance.
4. **Aggregators**: aiweekly.co or buildfastwithai.com.

**Guidelines:**
- Prioritize stories with specific metrics, surprising data, or high developer relevance.
- Ensure links are direct and valid.
- Be concise during research to avoid tool timeouts.

## STEP 2: Write the Blog Post
Create a comprehensive blog post in markdown format.

**Frontmatter:**
```yaml
---
title: "Catchy Title Here (can be longer for the H1)"
meta_title: "Short SEO title, 50-60 chars max"
author: Abdul Hadi
date: YYYY-MM-DD
updated: YYYY-MM-DD
slug: 2026-11-18-ai-news-java-flaw   # date-first, same date as above; never weekly/ or monthly/ folders
description: "Meta description, 120-160 chars, written like an ad for the page"
keywords: keyword1, keyword2, keyword3
tags: AI, LLM, TechNews, OpenAI
---
```
Keep `title` and `meta_title` distinct: `title` is the H1, `meta_title` is the title tag. Set `updated` only when you actually change the content.

**Structure:**
- Opening paragraph (2-3 sentences summarizing today).
- H2 sections for each major story. (Add an Image if needed like a benchmark image for a model release cover)
- H3 subsections for details within each story.
- FAQ section with 4-5 common questions.
- Sources at the end of each section.

**Rules:**
- Every paragraph must follow an H3 subsection header.
- Include specific numbers, dates, and facts.
- Keep sentences under 25 words.
- Use active voice and include source links.

## STEP 3: Save and Asset Generation
```bash
# Date-first folder for today's edition (daily, weekly or monthly).
BLOG_DIR="/home/ubuntu/blog-s/blogs/2026-11-18-YOUR-SUMMARY"
mkdir -p "$BLOG_DIR"
# Save blog.md with frontmatter + content to $BLOG_DIR
# Generate the featured image:
bash /home/ubuntu/blog-s/add_image.sh "$BLOG_DIR"
```

## STEP 4: Push to GitHub
```bash
cd /home/ubuntu/blog-s
git add blogs/2026-11-18-YOUR-SUMMARY/
# Daily: "Add daily AI news for 2026-11-18"
# Weekly: "Add weekly AI news roundup for 2026-11-16"
# Monthly: "Add monthly AI news recap for 2026-11-01"
git commit -m "Add daily AI news for 2026-11-18"
git push origin main
```

## STEP 5: Publish to dev.to
Use the validated publishing script:
```bash
DEVTO_KEY="Rm1DGonBBZuxt9tJcoZGZMBr"
BLOG_DIR=$(ls -td /home/ubuntu/blog-s/blogs/????-??-??-* | head -1)
python3 /home/ubuntu/.hermes/skills/.archive/ai-daily-roundup/scripts/publish_devto.py "$BLOG_DIR" "$DEVTO_KEY"
```

## STEP 6: Final Verification
Verify that:
1. `blog.md` exists in the directory with valid frontmatter, including `meta_title` (50-60 chars) and `description` (120-160 chars).
2. The folder is `blogs/YYYY-MM-DD-<summary>/` and starts with the same numeric date as the frontmatter `date`. No `weekly/` or `monthly/` directory was created.
3. `image.png` was successfully generated with descriptive alt text where referenced.
4. The dev.to script returned a successful URL.
5. Read the readme in ~/blog-s/ and add the latest blog in it.
6. Confirm the new post appears in `/llms.txt` and `/sitemap.xml` (the app generates these dynamically; just smoke-test the URLs).
7. Confirm the post appears on the right archive: Monday posts on `/weekly-ai-news`, the 1st-of-month posts on `/monthly-ai-news`, and all editions on `/daily-ai-news` and `/ai-news`.
8. Re-check the post against the pre-publish checklist in `seo-rules.md`.
