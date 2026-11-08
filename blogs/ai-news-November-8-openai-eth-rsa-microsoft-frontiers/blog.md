---
title: "OpenAI's AI Disproves a 1998 Theorem, DeepMind Finds RSA Flaws, and AI Spending Slows"
meta_title: "AI News Nov 8 2026: ETH, RSA Flaws, MSR and AI Spend"
author: Abdul Hadi
date: 2026-11-08
updated: 2026-11-08
slug: ai-news-November-8-openai-eth-rsa-microsoft-frontiers
image_alt: "Dark infographic for November 8 2026 AI news: OpenAI disproves the exponential time hypothesis, Google DeepMind finds 1024-bit RSA flaws, Microsoft shuts AI Frontiers, Claude Code secret leaks, Nous Arete-27B, OpenAI funding, chip lead times, and stalling AI spend"
description: "OpenAI disproves a 1998 ETH, DeepMind finds 1024-bit RSA flaws, Microsoft shuts AI Frontiers, Claude leaks secrets, and AI spend stalls."
keywords: AI news November 8 2026, OpenAI exponential time hypothesis, Google DeepMind RSA weaknesses, Microsoft AI Frontiers shutdown, Claude Code secret leak, Nous Arete-27B, OpenAI funding, AI spending stall
tags: AI, LLM, TechNews, OpenAI, Anthropic
---

## Today's Storylines

### A Day for Theory, Security, and Money

November 8, 2026 tested theory, security, and markets at once. Eight stories matter for developers, researchers, and buyers.

## OpenAI's AI Disproves a 1998 Complexity Theorem

### ETH and the Quantum Baseline

Russell Impagliazzo and Ramamohan Paturi proposed the Exponential Time Hypothesis in 1998. It says 3-SAT needs roughly 2 to the power of n time. It underpinned years of complexity lower bounds.

### Two Lean-Verified Papers

OpenAI published a 67-page paper. Anthropic published a 49-page companion. Both present 3-SAT algorithms running in 2 to the power of o(n). Both reported heavy AI involvement. Both proofs were checked in Lean.

### A Human Reviewer Speaks

OpenAI says its AI found a natural-language disproof on October 16. Formalization followed the next day. Russell Impagliazzo called the result very shocking news. He added that stricter versions were expected to fall first.

### Still a Theory Result

Impagliazzo, Paturi, and Ryan Williams signed no certification. They asked OpenAI to release raw data and fund a community conference. OpenAI agreed. The speedup kicks in only past about 10 to the 2,389 variables. Anthropic's five-clause case waits until about 10 to the 10,000 variables. Neither result touches P versus NP.

### Why It Matters

Two frontier labs now publish Lean-verified math that founders still parse. That changes how AI contributes to science. Our [November 6 roundup](/blog/ai-news-November-6-gpt6-cyber-metr-anthropic-hy4-wyoming) traced METR's acceleration data behind this pace.

**Sources:** [AI Weekly alert](https://aiweekly.co/alerts/openais-ai-disproof-of-1998-eth-shocks-co-author-impagliazzo), [NYT report](https://www.nytimes.com/2026/11/06/science/ai-exponential-time-hypothesis.html)

## Google DeepMind Finds Two Flaws in 1024-bit RSA

### What Was Found

Google DeepMind announced the findings on November 6, 2026. Its AI agents, under human direction, exposed two weaknesses. One enables digital-signature forgery. The other cheapens batch factoring of related moduli.

### Why 1024-bit Still Pervades

Many legacy systems still run 1024-bit RSA. Attackers now face far less work than expected. Modern 2048-bit keys remain safe against this specific threat.

### Humans Still Steer

Dj Dvijotham and Abhradeep Thakurta led the work. Nadia Heninger and Emmanuel Thomé joined. AI sped exploratory testing that once took years.

### A Reported 1,600-fold Speedup

AI Weekly described the forgery advantage as a 1,600-fold speedup. Treat that figure as reported, not consensus. Watch the cryptographic review process next. Our [November 7 roundup](/blog/ai-news-November-7-psi-quantum-wyoming-oracle) covered a separate PSI theorem on quantum speedups.

**Sources:** [Cryptobriefing report](https://cryptobriefing.com/google-deepmind-ai-rsa-1024-bit-weaknesses/), [AI Weekly front page](https://aiweekly.co)

## Microsoft Research Shuts Down Its AI Frontiers Group

### Langford's Exit Post

John Langford wrote on November 7 that AI Frontiers is over. The group formed in 2023 with about 50 people. It shipped AutoGen, Fara 7B, Next Latent, Dion3, and Full Bandwidth Transformer work.

### Reorg Into Microsoft AI

Microsoft reorganized AI Frontiers into Microsoft AI in September 2026. Langford says the ex-Inflection leadership there favors scaling over research. That philosophy clash left the team sidelined.

### Why Researchers Left

Langford says every founding leader reached the same conclusion and left. He cited no path from research to real use. He also questions MSR's basic deal after the non-consensual reorg.

### A Research vs Scale Tradeoff

Langford argues returns to research are large. He cites ByteDance experiments that pair Full Bandwidth Transformer ideas with doubled-scale models. MSR may need to rebuild trust before top talent returns.

**Sources:** [Hunch.net post](https://hunch.net/?p=13764006)

## Claude Code's Don't Ask Again Leaks Secrets

### 1,122 Public Files Exposed

Apiiro found 1,122 public GitHub files leaking passwords and secrets. The leaks trace to Claude Code's Don't Ask Again approval flow. Coding-agent convenience now carries real exposure.

### Why Permission Prompts Matter

Broad, remembered approvals mask risky commands. Secrets in repos spread fast once permission is cached. Developers must review every persistent grant.

### What Teams Should Do Now

Audit repositories for keys and tokens. Rotate anything suspicious immediately. Tighten approval defaults and logs. Track coding-agent actions like any production change. The [November 5 post](/blog/ai-news-November-5-provable-inference-php2shell) covered another agent security trail.

**Sources:** [Apiiro blog](https://apiiro.com/blog/coding-agents-leaking-secrets-github-dont-ask-again)

## Nous Research's Arete-27B Shrinks Qwen Propaganda

### A 52.8 Million Token Recipe

Arete-27B is a supervised fine-tune of Qwen3.8-27B. Training used about 52.8 million tokens at 64k context. It ran two epochs and 1,202 steps. No RL, no preference optimization, no architecture changes.

### Propaganda Rate Falls

Propaganda-tagged answers fell from 22 percent to 0.9 percent. Nous evaluated 803 prompts across seven value categories. Factual recall rose from 2.32 to 2.98 on a 0 to 5 scale.

### Capabilities Barely Move

Hermes Bench slipped from 65.77 percent to 65.60 percent. Terminal-Bench-2.1 rose from 67 percent to 70 percent. Nous calls the first change noise. The model is Apache 2.0.

### A Single-Judge Caveat

Grok 4.7 graded the eval. Nous did not tell it which model answered. Watch for independent reruns before treating the 0.9 percent as settled. The broader trend favors open weights built on Chinese bases.

**Sources:** [Hugging Face model card](https://huggingface.co/NousResearch/Arete-27B), [AI Weekly alert](https://aiweekly.co/alerts/nous-researchs-arete-27b-cuts-qwen-propaganda-from-22-to-09)

## OpenAI Raises $11 Billion and Hires Hacktron

### Funding Falls Short of Target

OpenAI reportedly raised $11 billion at a $1.25 trillion valuation. The round may reach $20 billion and should close soon. Earlier targets were $30 billion at $1.4 trillion. OpenAI now expects an IPO in 2027.

### Anthropic Faces Pressure Too

Anthropic's valuation slipped from $2 trillion expected to $1.2 to $1.3 trillion. Price cuts and enterprise discounts are hitting revenue. Credit agencies may rate its debt near junk.

### Paying the Firm That Hit It

OpenAI hired Hacktron on November 6. Hacktron chained two flaws on July 25. The attack compromised ChatGPT accounts of several OpenAI employees. OpenAI paid a $6,500 bounty on September 1.

### Daybreak Red Expands Access

Joint teams will red-team OpenAI's third-party integrations. Hacktron now gets expanded frontier-model access via Daybreak Red. The deal signals a shift from bounty-only defense. Security partnerships with model access may spread.

**Sources:** [TechCrunch funding report](https://techcrunch.com/2026/11/06/openai-reportedly-raises-an-additional-11-billion-at-a-1-25-trillion-valuation/), [OpenAI Hacktron post](https://openai.com/index/partnering-with-hacktron/)

## Microchip Says AI Buyers Are Crowding Chip Factories

### Lead Times Stretch to 32 Weeks

Steve Sanghi said AI buyers took over OSAT packaging and test lines. Standard products now ship in six to 32 weeks, up from four to eight. Microchip's own customers wait longer. Moving work takes about six months.

### One-Time Gains Inflated Q3

September net sales were $1.622 billion. Non-GAAP EPS hit $0.97, while GAAP EPS was $0.68. About $53 million came from one-time high-margin items. December guidance trims both margins and earnings.

### December Outlook and AI Revenue

December guidance calls for $1.573 to $1.638 billion. Non-GAAP gross margin should land at 64 to 65 percent. Earnings should run $0.87 to $0.95. Microchip's own data center business topped $250 million, up 55.7 percent.

### A Buyer-Seller Squeeze

AI demand still fills factories for now. Sanghi suggested some demand slowdown would help. Price increases from foundries and OSATs loom in January. The backlog keeps rising either way.

**Sources:** [24/7 Wall St. report](https://247wallst.com/investing/2026/11/07/the-chip-shortage-is-back-and-microchip-says-ai-customers-are-crowding-everyone-out/)

## Ramp Data Shows AI Spending Stalling

### Token Spend Flattened

Token spend grew only 1.5 percent across August and September. July had grown 42 percent. Token volumes kept rising. Price cuts and smarter usage explain the gap.

### Top 1 Percent Stuttered

The most AI-pilled firms spent just below $10,000 per employee monthly. Median firms spend $12 to $15. The top 10 percent spend $600 to $1,000. The top cohort alone can swing total revenue.

### Price Wars Compress Revenue

OpenAI halved GPT-6 Sol and GPT-6 Luna API prices in September. Anthropic cut prices for Fable 5.1 and Opus 5.5. Those cuts reportedly cost about $600 million in revenue growth. Enterprise discounts lock in spend but hit revenue.

### Buyers Now Control the Market

Ramp's Ara Kharazian expects further slowdown. Cheaper open models and routers like Jev lower costs. October saw an 8.9 percent re-acceleration, but headwinds remain. Personal agents likely cannot restart hypergrowth.

**Sources:** [TechCrunch Ramp report](https://techcrunch.com/2026/11/06/ramp-data-shows-ai-spending-stalling-just-as-anthropic-nears-its-ipo/)

## Frequently Asked Questions

### Did AI Actually Solve a Famous Math Problem?

AI helped produce a Lean-verified disproof of the 1998 ETH. The co-proposers did not certify it. Review is ongoing and practical speedups remain enormous in scale.

### Are 1024-bit RSA Keys Unsafe Now?

Legacy 1024-bit keys face newly reported weaknesses. Modern 2048-bit keys remain safe from this threat. Migrate old systems anyway.

### Why Did Microsoft Shut Down AI Frontiers?

Langford says the group clashed with Microsoft AI's scaling-first culture. The non-consensual reorg eroded trust. Most leaders exited quickly.

### How Much Is AI Spending Really Slowing?

Token spend grew 1.5 percent in two months after 42 percent in July. Top buyers dipped below prior peaks. Price cuts explain much of the gap.

### What Should Developers Do About Leaked Secrets?

Rotate exposed credentials immediately. Audit agent permissions and logs. Review persistent approval defaults now.

## The Bottom Line

### Proof, Power, and Money Now Intersect

Theory, cyber, and finance moved together on November 8. Research, security, and spend are all under review.

### Control Systems Lag Behind

Claude Code leaks and RSA findings show tools outrun defaults. Monitoring and migration plans matter more than headlines.

### Signals to Watch

Track ETH peer review and DeepMind crypto follow-ups. Watch OpenAI funding closes and December chip guidance. Watch Ramp's next AI spend print.

Our [November 6 roundup](/blog/ai-news-November-6-gpt6-cyber-metr-anthropic-hy4-wyoming) covered GPT-6 Cyber finds and METR's acceleration claims. [The November 5 post](/blog/ai-news-November-5-provable-inference-php2shell) tracked provable inference and PHP2Shell. Verification, not hype, is the new bar.

---

*This post is for information only. It does not constitute financial, security, or investment advice.*
