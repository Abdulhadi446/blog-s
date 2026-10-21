# SEO Rules for Agents: Blogs and Websites

Version: October 2026. Give this to any agent that writes blog posts or builds web pages. Follow it on every task.

## 0. Prime directive

1. Write for the reader first, the search engine second. Google's own guidance has stayed the same through the March and May 2026 core updates: make helpful, reliable, people-first content.
2. Optimizing for Google's AI features (AI Overviews, AI Mode) is not a separate discipline. Google says there are no extra requirements and no special optimizations beyond normal SEO fundamentals. Do good SEO and you are covered.
3. Never trade quality for volume. Publishing many thin pages is the fastest way to get hit by the scaled content abuse spam policy.
4. When a rule below conflicts with what is best for the reader, the reader wins.

## 1. Before writing: research

1. Pick ONE primary topic per page and one primary search intent. Do not target the same query with two pages (keyword cannibalization).
2. Classify the intent: informational, commercial investigation, transactional, or navigational. Match the page type to it (guide, comparison, product page, docs).
3. Look at what currently ranks for the query. Search it. Note what the top results cover, what they miss, and what format they use. Your page must add something they don't: original data, first-hand testing, a clearer explanation, code, a worked example, a better visual.
4. List the primary keyword, 3 to 8 secondary phrases, and the questions people ask (People Also Ask, related searches). Google can expand a query into many sub-searches (query fan-out), so cover the subtopics around the main question, not just the exact phrase.
5. If you cannot say in one sentence what new value this page gives that existing results do not, do not write it.

### Keyword research and competitor research

1. Do keyword research before every post. Use a real tool: Ahrefs or Semrush (paid), or Google Keyword Planner, Google Search Console, and Google Trends (free). Record search volume, keyword difficulty, and intent for each target.
2. Prefer keywords the site can realistically rank for. A new site should start with low-difficulty, long-tail phrases and move up as it earns authority.
3. Check the competitors that rank for your target keywords. Note their top pages, the keywords they rank for that you do not, and the topics they have not covered.
4. Check where competitors promote themselves and earn links: guest posts, directories, communities, social channels, newsletters, podcasts, and press. Pull their backlink profiles in Ahrefs or Semrush and list the sources worth pursuing for this site (see section 6).
5. Save the research (keyword, volume, difficulty, intent, competitor URLs, gaps) next to the draft so a human can review it.

## 2. Content rules

### Quality and originality

1. Every page needs a real point of view or real information gain: first-hand experience, original benchmarks, screenshots, your own code, real numbers with a source, or expert analysis.
2. Never paraphrase competitor articles and call it new. Rewording existing content with no added value is exactly what Google's quality raters rate lowest.
3. Be specific. Replace vague claims with numbers, names, versions, dates, and examples.
4. Answer the main question early, in the first screen of the page, then go deeper.
5. Cut filler. No padding intros, no repeating the same point, no word-count targets. Length should match what the topic needs.

### Accuracy and trust (E-E-A-T)

1. Verify every factual claim, statistic, version number, price, and date. Cite the primary source (official docs, the original study) and link to it.
2. Show who is behind the content: real author name, short bio, link to an author page. Add an About page and contact details to the site.
3. Include a published date and a visible last-updated date. Only change the updated date when you actually changed the content.
4. For health, money, legal, or safety topics, be extra conservative: cite authoritative sources and add a plain note on the limits of the advice.
5. Do not invent quotes, studies, reviews, or author credentials. Ever.

### AI-assisted content

1. Google does not ban AI-generated content. It penalizes content produced at scale mainly to manipulate rankings, whoever or whatever wrote it. Google stated in May 2026 that its spam policies also apply to generative AI responses in Search.
2. A human (or a rigorous verification pass) must check facts, add the original value from section 2, and remove generic text before publishing.
3. Do not batch-generate dozens of near-identical pages (city or keyword templates with swapped words). Each page needs unique, useful content or it should not exist.
4. Do not scrape or republish content from other sources without meaningful change.
5. If the site uses AI-generated images or product data, follow platform rules (for example, Google Merchant Center requires IPTC DigitalSourceType metadata on AI-generated product images).

## 3. On-page structure

### Title tag

1. Unique per page. Lead with the primary keyword where it reads naturally.
2. Aim for roughly 50 to 60 characters so it is not cut off in results. This is a display guideline, not a Google rule.
3. Describe the page honestly. No clickbait that the content does not deliver. Google may rewrite titles it finds misleading or stuffed.

### Meta description

1. Unique per page, roughly 120 to 160 characters, written like an ad for the page: what the reader gets and why click.
2. It is not a ranking factor, but it affects click-through. Google may replace it with text from the page.

### Headings

1. Exactly one H1 per page, matching the page's main topic.
2. Use H2 for main sections and H3 for subsections. Never skip levels for styling. Headings should describe the content, and a reader skimming only the headings should understand the page.
3. Use question-style H2s where real users ask that question, and answer it directly in the first one or two sentences below.

### URLs

1. Short, lowercase, hyphen-separated, human-readable: `/blog/core-web-vitals-guide`.
2. No dates, IDs, or query parameters in URLs of evergreen content. Do not change a live URL without a 301 redirect.

### Body formatting

1. Short paragraphs (2 to 4 sentences). Use lists for steps and options, tables for comparisons, and code blocks for code.
2. Put the primary keyword in the title, H1, first paragraph, and URL naturally. Then stop. Never stuff keywords. Use synonyms and related terms the way a human would.
3. Add a clear summary or key takeaways near the top for long posts.
4. Add an FAQ section only when there are real, distinct questions. Do not pad with fake ones.

### Links

1. Internal links: link to 3 to 5 relevant pages on the same site with descriptive anchor text (never "click here"). Link from older related posts to the new one too. No orphan pages.
2. External links: cite authoritative sources. Open them normally. Mark paid, sponsored, or affiliate links with `rel="sponsored"` and user-generated links with `rel="ugc"`.
3. Fix or remove broken links.

### Images and media

1. Every meaningful image gets descriptive alt text (describe what is in it, naturally). Decorative images get empty alt.
2. Use descriptive file names (`lcp-waterfall-chart.webp`, not `IMG_2041.png`).
3. Use modern formats (WebP or AVIF), correct dimensions, and compress. Set explicit `width` and `height` to prevent layout shift.
4. Lazy-load images below the fold. Never lazy-load the main hero (LCP) image.
5. Add original screenshots, diagrams, or charts instead of generic stock images where possible.
6. If you embed video, put a text summary or transcript on the page.

## 4. Technical SEO for websites

### Crawl and index

1. Every important page must return 200, be reachable via internal links, and be listed in an XML sitemap. Submit the sitemap in Google Search Console and reference it in `robots.txt`.
2. `robots.txt` controls crawling, not indexing. To keep a page out of search, use `noindex`, and do not also block it in robots.txt or Google cannot see the tag.
3. Set a self-referencing canonical on every page. Use canonicals to resolve duplicate or parameter URLs.
4. Never ship a staging site or a `noindex` flag to production by accident. Check before launch.
5. Use proper status codes: 301 for permanent moves, 404 or 410 for removed pages. No soft 404s. Avoid redirect chains.
6. Key content and links must be in the HTML Google can render. If the site is JavaScript-heavy, prefer server-side rendering or static generation for content pages. Use real `<a href>` links, not click handlers.

### Mobile and security

1. Google indexes the mobile version of your site (mobile-first indexing). Mobile content must match desktop content, be readable without zooming, and have tap targets that are large enough.
2. Use HTTPS everywhere. Include `<meta name="viewport" content="width=device-width, initial-scale=1">`.
3. No intrusive pop-ups or interstitials that block the content on mobile.

### Core Web Vitals

The current set is LCP, INP, and CLS. INP replaced FID in March 2024, and the thresholds have not changed since. Targets are measured at the 75th percentile of real users:

| Metric | Good | Poor |
| --- | --- | --- |
| LCP (loading) | 2.5 s or less | over 4.0 s |
| INP (responsiveness) | 200 ms or less | over 500 ms |
| CLS (visual stability) | 0.1 or less | over 0.25 |

Rules:

1. LCP: preload and prioritize the hero image, compress it, serve it from a CDN, and keep server response time low. Slow hosting shows up directly in LCP.
2. INP: keep JavaScript small. Split bundles, defer non-critical scripts, avoid long tasks on the main thread, and audit third-party scripts.
3. CLS: reserve space for images, embeds, ads, and banners. Use `font-display: swap` with a matched fallback font to avoid font-swap jumps.
4. Measure with PageSpeed Insights, Search Console's Core Web Vitals report, and Chrome DevTools. Field data matters more than lab scores.
5. Keep perspective: Core Web Vitals are a real but modest ranking factor. Great content on a slightly slow page beats thin content on a fast one, but do not ship slow pages.

### Structured data (schema)

1. Use JSON-LD. Add `Article` or `BlogPosting` (with author, datePublished, dateModified, image) to posts, `Organization` and `WebSite` on the homepage, `BreadcrumbList` for navigation, and `Product`, `SoftwareApplication`, or `LocalBusiness` where they truly apply.
2. Markup must describe content that is visible on the page. Never mark up things that are not there.
3. Validate with Google's Rich Results Test and the Schema Markup Validator. Check the current Google docs for which features still produce rich results. Some types, such as FAQ and HowTo, have been heavily restricted or removed, so do not add them expecting a visual boost.

### Site architecture

1. Keep important pages within 3 clicks of the homepage. Build topic clusters: one comprehensive pillar page plus supporting posts, all interlinked.
2. Breadcrumbs on deeper pages. Clear main navigation. Consistent URL structure.
3. Include a custom 404 page that links back to useful content.

### Domain and site setup

1. Use one canonical domain. Pick either the `www` or the non-`www` version, and 301-redirect the other (and all `http://` URLs) to it.
2. Verify the domain in Google Search Console (a DNS TXT record is the most reliable method) and submit the sitemap there. Also add the site to Bing Webmaster Tools.
3. Make sure DNS, HTTPS certificate, and redirects work before launch. Confirm the site is not blocked by `robots.txt` or a `noindex` tag.

### robots.txt

1. Every site must have a `robots.txt` at the root (`/robots.txt`) that returns 200.
2. Allow crawling of all public pages, CSS, and JS. Block only things that should not be crawled (admin, cart, internal search results).
3. List the sitemap URL in it.
4. `robots.txt` blocks crawling, not indexing. Use `noindex` to keep a page out of results.
5. Review it after every site change. One stray `Disallow: /` removes the site from search.

Minimal example:

```text
User-agent: *
Allow: /
Disallow: /admin/

Sitemap: https://example.com/sitemap.xml
```

### llms.txt

1. Add an `/llms.txt` file at the root: a plain Markdown file that gives AI tools a short, curated map of the site.
2. Format: an H1 with the site name, a one-line blockquote summary, then sections of links with one-line descriptions to the most important pages (key guides, docs, about, contact).
3. Keep it accurate and update it when major pages change.
4. Be honest about its value: it is an emerging convention, and Google has not said it uses it. There is no confirmed ranking benefit. It is cheap to add, but it never replaces good content and normal SEO.
5. If you want to allow or block specific AI crawlers, do that in `robots.txt`, not in `llms.txt`.

Minimal example:

```markdown
# Example Blog

> Practical guides on AI engineering, written by practitioners.

## Guides
- [Core Web Vitals guide](https://example.com/blog/core-web-vitals-guide): how to pass LCP, INP, and CLS

## About
- [About](https://example.com/about): who writes this site
```

## 5. Writing for AI search (Google AI features, ChatGPT, Perplexity, etc.)

This is mostly good SEO, applied carefully.

1. Put a clear, self-contained answer directly under each heading. AI systems and featured snippets pull passages, so each section should make sense on its own.
2. Cover the topic comprehensively, including the follow-up questions, since AI systems may issue several related searches for one query.
3. Make entities explicit: name products, people, versions, and dates plainly instead of using vague pronouns.
4. Original data, tables, and clearly sourced facts get cited more than generic summaries.
5. Do not block Googlebot if you want to be in Google's AI features. For Google, robots.txt for Googlebot is the control. For other AI crawlers, decide deliberately which to allow and keep the rules in `robots.txt`.
6. Track visibility with Search Console (AI feature traffic is included in overall Search traffic) and by testing real queries. Judge success by signups, sales, and engagement, not just clicks.
7. Do not rely on unproven tricks. There is no confirmed requirement for special files or hidden markup to appear in AI answers.

## 6. Off-page SEO: backlinks

Backlinks from relevant, trusted sites are still one of the strongest signals. Earn them. Never buy them.

1. Create link-worthy assets first: original research, benchmarks, free tools, templates, and in-depth guides that others want to cite.
2. Run a competitor backlink gap analysis in Ahrefs or Semrush. List the sites that link to competitors but not to us, and decide which are realistic targets.
3. Replicate the legitimate sources competitors use: relevant guest posts, expert roundups, podcast or newsletter features, resource pages, and industry directories.
4. Take part in relevant communities (developer forums, Reddit, Hacker News, Dev.to, Hashnode, LinkedIn, GitHub). Add value first, and follow each community's self-promotion rules. Link drops are spam.
5. When republishing a post elsewhere (Medium, Dev.to, LinkedIn), set the canonical URL to the original post.
6. Reclaim lost links: find broken links pointing to the site and 301-redirect them to the best matching page. Ask for a link where the site is mentioned without one.
7. Prefer a few relevant, high-quality links over many low-quality ones. Avoid link farms, private blog networks, paid links without `rel="sponsored"`, and link exchange schemes.
8. Track new and lost backlinks monthly and note which pieces earn links, so the team can make more of them.

The agent drafts outreach and research lists, but a human should approve and send outreach.

## 7. Pre-publish checklist

The agent must confirm every item before marking a page done.

**Content**

- [ ] One clear primary topic and intent; no duplicate page for the same query
- [ ] Adds something original that top results lack
- [ ] Every fact, number, and date verified; sources linked
- [ ] Author, published date, and updated date shown
- [ ] Answer to the main question appears early
- [ ] No filler, no keyword stuffing, no fake FAQs

**On-page**

- [ ] Unique title (about 50 to 60 chars) and meta description (about 120 to 160 chars)
- [ ] One H1; logical H2/H3 structure
- [ ] Clean, short, descriptive URL
- [ ] 3 to 5 internal links with descriptive anchors; inbound links added from related posts
- [ ] Alt text, file names, compressed images with width and height set

**Technical**

- [ ] Indexable (no stray noindex), canonical set, in sitemap
- [ ] Returns 200; no broken links; redirects are single-hop 301s
- [ ] Renders correctly on mobile; HTTPS; viewport tag present
- [ ] LCP at or under 2.5 s, INP at or under 200 ms, CLS at or under 0.1
- [ ] JSON-LD added and validated
- [ ] Open Graph and Twitter card tags set (title, description, image)

**Site launch and setup (new sites and major changes)**

- [ ] Domain verified in Search Console, one canonical version (www or non-www) with 301s
- [ ] `robots.txt` exists, allows public pages, and lists the sitemap
- [ ] `llms.txt` added and kept current (optional)
- [ ] Meta title and meta description set on every page
- [ ] Keyword research and competitor check saved with the draft
- [ ] Backlink targets listed for the new piece

## 8. Never do this

1. Keyword stuffing, hidden text, cloaking, or doorway pages.
2. Mass-producing near-duplicate or thin pages (scaled content abuse).
3. Publishing third-party content on the site that has no relation to its topic to borrow its ranking (site reputation abuse), or buying expired domains just to host low-value content.
4. Buying links, link schemes, or comment and forum spam.
5. Fabricated authors, reviews, testimonials, statistics, or sources.
6. Copying or lightly rewording other sites.
7. Misleading titles or clickbait the page does not satisfy.
8. Blocking CSS or JS that Google needs to render the page.
9. Changing dates to fake freshness.
10. Chasing every algorithm update. Keep making helpful content.

## 9. Maintenance

1. Refresh important posts when facts change. Update the content itself, then the date.
2. Review Search Console monthly: queries, pages losing clicks, indexing errors, Core Web Vitals, manual actions.
3. Merge or remove thin and outdated pages (redirect merged pages with a 301).
4. After a Google core update, do not panic-edit. Wait for the rollout to finish, then compare against the helpful content self-assessment questions in Google's documentation.
5. Re-check this document against Google Search Central regularly. Search advice changes, and official docs are the source of truth.

## 10. Sources of truth

- Google Search Central: Search Essentials, SEO Starter Guide, spam policies, and "AI features and your website"
- Google's guidance on using generative AI content
- web.dev and Chrome documentation for Core Web Vitals
- Google Search Status Dashboard for update announcements
