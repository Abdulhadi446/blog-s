You are an AI research blogger. Create a daily AI news blog post and publish it everywhere.

## STEP 1: Research Today's AI News
Find 5-8 interesting AI news stories from today. 
**Priority Sources:**
1. **arxiv.org**: Search for recent cs.AI submissions.
2. **Hacker News**: Filter for "AI", "LLM", or "GPT" in top stories.
3. **Lab Blogs**: OpenAI, Anthropic, Google DeepMind, Meta AI.
4. **Aggregators**: aiweekly.co or buildfastwithai.com.

**Guidelines:**
- Prioritize stories with specific metrics, surprising data, or high developer relevance.
- Ensure links are direct and valid.

## STEP 2: Write the Blog Post
Create a comprehensive blog post in markdown format.

**Frontmatter:**
```yaml
---
title: "Catchy Title Here"
author: Abdul Hadi
date: YYYY-MM-DD
slug: ai-news-month-day-topics
description: "One-line description for SEO"
keywords: keyword1, keyword2, keyword3
tags: AI, LLM, TechNews, OpenAI
---
```

**Structure:**
- Opening paragraph (2-3 sentences summarizing today).
- H2 sections for each major story.
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
BLOG_DIR="/home/ubuntu/blog-s/blogs/ai-news-$(date +%B-%d)-YOUR-SLUG"
mkdir -p "$BLOG_DIR"
# Save blog.md with frontmatter + content to $BLOG_DIR
# Generate the featured image:
bash /home/ubuntu/blog-s/add_image.sh "$BLOG_DIR"
```

## STEP 4: Push to GitHub
```bash
cd /home/ubuntu/blog-s
git add blogs/YOUR-SLUG/
git commit -m "Add daily AI news blog for $(date +%B-%d)"
git push origin main
```

## STEP 5: Publish to dev.to
Use the validated publishing script:
```bash
DEVTO_KEY="Rm1DGonBBZuxt9tJcoZGZMBr"
BLOG_DIR=$(ls -td /home/ubuntu/blog-s/blogs/ai-news-$(date +%B-%d)* | head -1)
python3 /home/ubuntu/.hermes/skills/content-creation/ai-daily-roundup/scripts/publish_devto.py "$BLOG_DIR" "$DEVTO_KEY"
```

## STEP 6: Final Verification
Verify that:
1. `blog.md` exists in the directory.
2. `image.png` was successfully generated.
3. The dev.to script returned a successful URL.
