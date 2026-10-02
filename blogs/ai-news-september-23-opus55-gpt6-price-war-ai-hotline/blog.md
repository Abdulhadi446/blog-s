---
title: "Two Flagships, 48 Hours: Claude Opus 5.5 and GPT-6 Slash Prices as a US-China AI Hotline Looms"
author: Abdul Hadi
date: 2026-09-23
slug: ai-news-september-23-opus55-gpt6-price-war-ai-hotline
description: "Claude Opus 5.5 and GPT-6 Sol/Luna launched hours apart with deep price cuts, OpenAI's ad pixel follows you across the web, and the US proposed a China AI incident hotline before the September 24 summit."
keywords: AI news, Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, OpenAI ad pixel, US-China AI hotline, Anthropic IPO, arXiv AI papers
tags: AI, LLM, TechNews, OpenAI, Anthropic, Safety
---

September 22 became the biggest model launch day of 2026. Anthropic and OpenAI shipped flagship-priced models hours apart, and every headline led with price. Meanwhile, a cross-site tracking cookie, an antitrust suit, and a US-China AI hotline story round out a wild day for developers.

## Claude Opus 5.5 and GPT-6 Land Hours Apart — Both Lead With Price

### Anthropic Cuts Opus Pricing by 20 Percent

Anthropic released Claude Opus 5.5 on September 22 at $4 per million input tokens and $20 per million output. That is 20% below Opus 5's $5/$25 list price. Cache reads dropped 60% to $0.20 per million tokens. The model carries a 1M-token context window, 128K max output, and a June 2026 knowledge cutoff.

### The Benchmarks Tell a Split Story

Opus 5.5 hits 66.4% on Terminal-Bench 4.0, beating GPT-6 Astra's 57.9%. It scores 1846 Elo on GDPval-AA v2.1 across 44 occupations. It still loses AutomationBench to Astra, 40.0% to 41.4%. Anthropic claims 40% lower running cost and 30% faster output than Opus 5.

### OpenAI Answers With GPT-6 Sol and Luna

OpenAI launched GPT-6 Sol at $2/$10 and GPT-6 Luna at $0.10/$0.50 — half their GPT-5.6 predecessors' prices. Cached reads get a 90% discount. Luna scores 66.6% on DeepSWE v1.1, near Sol's 68.8%, at one twentieth of Sol's price. Grok 4.7 joined the price war on September 21 at $2/$6.

### Four Breaking API Changes in Opus 5.5

Thinking cannot be disabled in Opus 5.5. `tool_choice: "any"` now returns a 400 error. Thinking blocks bind to the model and conversation, breaking replays. The old `computer_20251124` tool is rejected. Audit your code before swapping model strings.

**Sources:** [Anthropic — Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5), [Reuters — Anthropic unveils Claude Opus 5.5](https://www.reuters.com/business/anthropic-unveils-claude-opus-55-2026-09-22), [GitHub Changelog — Opus 5.5 in Copilot](https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot/), [AIToolsRecap — Two Flagship Launches in One Day](https://aitoolsrecap.com/Blog/ai-news-september-23-2026)

## OpenAI's Ad Pixel Quietly Ties Your Web Browsing to Your ChatGPT Account

### The `__obi` Cookie Survives a Full Year

Researchers reproduced a cross-site cookie named `__obi` on mobile. It is created when you visit ChatGPT, then sent back when you load an advertiser's site. The cookie uses `SameSite=None` and `Secure`, and lives for one year. OpenAI's other cookies block third-party requests; `__obi` does not.

### It Was Seen on 936 Advertiser Pixels

The investigation observed the tracker across 936 advertiser pixels on 1,029 hostnames. Events flow to `bzr.openai.com`, an internal collector reportedly codenamed "Bazaar." The pixel can collect page content, hashed emails and phone numbers, and unencrypted city and region data.

### Why Developers Should Care

This resembles standard conversion tracking from Meta or Google. The difference: it links off-site activity to an AI assistant account. If you run an ad-supported site, you may already serve OpenAI's pixel. Check your tag manager before your users do.

**Sources:** [CybersecurityNews — ChatGPT Ad Tracking Cookie](https://cybersecuritynews.com/chatgpt-ad-tracking-cookie-follows-users/), [OpenAI — Measurement Pixel docs](https://developers.openai.com/ads/measurement-pixel), [AI Weekly — September 22 roundup](https://aiweekly.co/ai-news-today), [tbreak — OpenAI `__obi` cookie](https://tbreak.com/chatgpt-ad-tracker-openai-obi-cookie)

## The US Proposes a China AI Incident Hotline Before the September 24 Summit

### Eight Hours of Talks in New York

US Treasury Secretary Scott Bessent and Chinese Vice Premier He Lifeng met for about eight hours at JPMorgan's headquarters on September 21. Bessent called the engagement "very successful." The two sides discussed trade and AI ahead of the Trump-Xi White House meeting on September 24.

### A Notification Mechanism for AI Emergencies

The US proposed a notification mechanism for serious AI incidents with national-security impact. Both sides agreed to create a new AI dialogue working group. Chip export controls were explicitly excluded from the discussions. The proposal now goes to Trump and Xi.

### Why Cyberattacks Lead the Agenda

Both nations fear AI-enabled cyberattacks launched by the other side. AI coding agents have already struck real targets this year. An incident hotline would let cybersecurity teams share information before attribution is complete. Policy experts also want limits on AI adaptive worms against civilian infrastructure.

**Sources:** [France 24 — US and China discuss AI communication channel](https://www.france24.com/en/americas/20260921-us-china-discuss-ai-communication-channel-ahead-of-trump-xi-summit), [Reuters — Xi rolls into Trump summit](https://www.reuters.com/world/china/xi-rolls-into-trump-summit-with-chinas-trade-engine-roaring-2026-09-21), [Tech Policy Press — Trump and Xi should talk about worms](https://www.techpolicy.press/trump-and-xi-should-talk-about-worms/)

## Four AI Subscribers Sue the Labs Over an Alleged "Slowdown Pact"

### The Sherman Act Claim

A class action filed September 18 in the US District Court for the Northern District of California accuses Anthropic, OpenAI, SpaceXAI, and Google of violating Sherman Act Section 1. The plaintiffs say the labs coordinated to slow AI development. Four named subscribers pay for ChatGPT, Claude, Grok, or Gemini.

### It All Traces to Dario Amodei's September 12 Essay

The suit centers on Amodei's 3,800-word pacing essay and a July 2026 joint statement. That statement acknowledged "intense competitive pressure not to unilaterally slow" development. Plaintiffs argue any agreement that progress "should be slower than competition would otherwise produce" harms consumers.

### The Industry Keeps Splitting

Cohere CEO Aiden Gomez accused US labs of forming a "cartel" under the guise of safety. OpenAI's policy chief Chris Lehane said no antitrust waiver is needed for safety talks. FTC Chair Andrew Ferguson said he would be "deeply suspicious" of exemption requests.

**Sources:** [CBS/AP — Lawsuit says labs made illegal AI slowdown deal](https://www.cbsnews.com/news/ai-slowdown-lawsuit-openai-anthropic-google/), [OPB/AP — Lawsuit over AI slowdown](https://www.opb.org/article/2026/09/20/lawsuit-says-anthropic-openai-spacexai-and-google-made-illegal-agreement-on-ai-slowdown/), [Bloomberg — OpenAI works with Anthropic, Google on safety](https://www.bloomberg.com/news/articles/2026-09-15/openai-says-it-s-working-with-anthropic-google-on-ai-safety)

## Anthropic's Revenue Pace Hits $100 Billion as Its IPO Slides to November

### From $65B to $100B in Two Months

The New York Times reports Anthropic now paces for over $100 billion in annualized revenue this year. That figure is 50% above the $65B disclosed in July and over 10x end-of-2025 levels. Claude Code and Cowork enterprise adoption drive the surge.

### The IPO Moves to Nab Q3 Financials

Anthropic pushed its IPO from October to November 2026 to include third-quarter numbers. Bankers target a valuation near $2 trillion on possible 2028 revenue of $190B–$200B. If it prices there, it becomes the largest IPO in history, beating SpaceX's $1.8T record.

### Nvidia May Anchor With $10 Billion

Reuters says Nvidia is in talks to back the Anthropic IPO with up to $10 billion. Pre-IPO futures across 19 exchanges already imply a $1.94 trillion average valuation. Polymarket gives the listing 67% odds by October 31 and 90% by year end.

**Sources:** [Yahoo Finance — Anthropic tops $100 billion revenue](https://finance.yahoo.com/technology/ai/articles/anthropic-tops-100-billion-revenue-224001996.html), [NYT — Anthropic could raise $100B in blockbuster IPO](https://www.nytimes.com/2026/08/21/technology/anthropic-ipo-100-billion.html), [Yahoo Finance — Nvidia could make Anthropic IPO bigger than SpaceX](https://finance.yahoo.com/markets/stocks/articles/nvidia-could-anthropic-ipo-bigger-120259563.html)

## arXiv's September 22 Batch: Agent Harnesses, Kimi Attention, and Cheaper Distillation

### Agents That Improve Their Own Harnesses

arXiv's cs.LG listing for September 22 shows 426 new entries. "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses" (arXiv:2609.24972) proposes agents that iteratively upgrade their own tool scaffolds. Google research authors regularize the loop to avoid runaway rewrites. It matters because harness quality now gates model performance more than raw parameters.

### Diagnosing Multi-Turn Tool Use Failures

"Critical-State RL" (arXiv:2609.24985) diagnoses which internal states remain trainable during long tool-use chains. The Salesforce-led team connects stalled RL training to state collapse across turns. Multi-turn agent training is where most teams lose reward signal.

### One Paper Explains Kimi Delta Attention

"Complex KDA" (arXiv:2609.24797) studies Kimi Delta Attention, the mechanism behind Moonshot's Kimi models. An international team analyzes its expressivity and proposes complex-valued extensions. Linear-attention designs are reshaping long-context inference costs for every developer.

### Just 1% of Tokens Suffice for Distillation Gradients

"1% of Tokens Can Be Enough" (arXiv:2609.24432) shows on-policy distillation works with a tiny fraction of tokens for gradient estimation. Also, "Muon Can Outperform Dedicated Continual Learning Methods" (arXiv:2609.24678) found the Muon optimizer beats purpose-built continual learners.

**Sources:** [arXiv cs.LG recent](http://arxiv.org/list/cs.LG/recent), [arXiv:2609.24972 — RRSI](https://arxiv.org/abs/2609.24972), [arXiv:2609.24985 — Critical-State RL](https://arxiv.org/abs/2609.24985), [arXiv:2609.24797 — Complex KDA](https://arxiv.org/abs/2609.24797), [arXiv:2609.24432 — 1% of Tokens](https://arxiv.org/abs/2609.24432)

## Snorkel Raises $350M, and an Autonomous Multi-Model Implant Surfaces

### Snorkel AI Triples Its Valuation

Snorkel AI raised $350 million at a $3.5 billion valuation, led by Insight Partners and S32. That roughly triples its previous mark. Snorkel sells training-data infrastructure for frontier model builders. As model prices fall, data tooling becomes the differentiator, and investors repriced it accordingly.

### Cisco Talos Discloses CLOSEDQUORUM

Cisco Talos released the CAIRN toolkit alongside CLOSEDQUORUM — what it calls the first fully autonomous, multi-model AI command-and-control implant. "Multi-model" is the key word. The implant routes between providers, so no single vendor can cut it off.

### Defenders Go Multi-Model Too

Palo Alto Networks launched Unit 42 Continuous Frontier AI Defense the same day. It combines Claude Mythos 5, GPT-5.6-Cyber, and open-weight models for vulnerability detection. Both attackers and defenders now run ensembles, because no single model catches everything.

**Sources:** [TechCrunch — Snorkel AI triples valuation](https://techcrunch.com/2026/09/22/snorkel-ai-triples-valuation-to-3-5b-as-demand-for-ai-training-data-booms/), [AIToolsRecap — September 23 roundup](https://aitoolsrecap.com/Blog/ai-news-september-23-2026), [SBS — Cisco Talos CAIRN](https://news.sbs.co.kr/english/article.do?news_id=N1008764381)

## Frequently Asked Questions

### What does Claude Opus 5.5 cost?

Claude Opus 5.5 costs $4 per million input tokens and $20 per million output tokens. Cache reads cost $0.20 per million. That is 20% below Opus 5's list price. Anthropic claims 40% lower total running cost on typical workloads.

### What is the OpenAI `__obi` cookie?

`__obi` is an OpenAI advertising cookie with a one-year lifetime and `SameSite=None`. It connects your ChatGPT session to your activity on advertiser websites. Researchers found it on 936 advertiser pixels across 1,029 hostnames. OpenAI says advertisers never see your conversations.

### Why are AI labs being sued for slowing down AI?

Subscribers allege a Sherman Act Section 1 violation. They claim Anthropic, OpenAI, SpaceXAI, and Google agreed their progress "should be slower than competition would otherwise produce." The suit follows Dario Amodei's September 12 slowdown essay and a July joint statement.

### What is the US-China AI incident hotline?

It is a proposed notification mechanism for serious AI incidents. Treasury Secretary Bessent floated it during eight hours of talks with Vice Premier He Lifeng on September 21. A new AI dialogue working group will advance it at the September 24 Trump-Xi summit.

### Which arXiv papers should developers read this week?

Start with RRSI (2609.24972) on self-improving agent harnesses and Critical-State RL (2609.24985) on multi-turn tool-use training. Complex KDA (2609.24797) explains Kimi Delta Attention. "1% of Tokens Can Be Enough" (2609.24432) cuts distillation costs dramatically.

---

*Compiled by Abdul Hadi on September 23, 2026. Sources linked throughout. Prices and benchmarks reflect launch-day disclosures.*
