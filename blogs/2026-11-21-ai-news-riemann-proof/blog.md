---
title: "Daily AI News Nov 21: Claude and a Mathematician Claim the Riemann Hypothesis"
meta_title: "Daily AI News Nov 21: The Riemann Hypothesis Falls"
author: Abdul Hadi
date: 2026-11-21
slug: 2026-11-21-ai-news-riemann-proof
image_alt: "Phone showing the Anthropic logo held in front of a blurred screen with the Claude homepage and a network diagram"
description: "Daily AI news for Nov 21: Claude and Levent Alpöge claim a Riemann proof, Anthropic stock slides 9%, and 2M test prompts leak through AI routers."
keywords: daily AI news, AI news today, Riemann hypothesis proof, Levent Alpöge Claude, Inkling 2 Mini, AI supply chain leak, Trump data centres, METR time horizons
tags: AI, LLM, TechNews, Mathematics, Anthropic, Security, Policy
---

## Today's Storylines

### A Proof, a Sell-Off and a Laptop Model

The daily AI news for November 21 opens with a mathematics claim nobody expected this year. An Anthropic mathematician says Claude helped him prove the Generalized Riemann Hypothesis. Markets moved the other way: Anthropic fell 9% and the Nasdaq erased its 2026 gains. AI news today also brought a 26B model that runs on a laptop and a security test that caught live credentials leaking through AI routers.

### The Five-Minute Version

- Levent Alpöge says he and Claude proved the Generalized Riemann Hypothesis, with a 17.4 million-line Lean formalization.
- Terence Tao calls the Lean proof enormous and says verification is now the bottleneck, not the claim.
- Anthropic fell 9% to $88.30 on Friday, giving back most of its 17% first-day gain.
- The Nasdaq Composite erased all of 2026's gains, and the week wiped about $4 trillion in market value.
- Thinking Machines released Inkling 2 Mini: 26.4B total parameters, 3.4B active, built for local use.
- Dragos planted nearly two million canary secrets in AI prompts and found three providers already breached.
- Trump threatened to ban US firms from building AI data centres overseas, with no enforcement plan yet.
- Cursor told Congress it may phase out Chinese open-weight models, including the Kimi base under Composer 2.
- METR's updated time horizon plot shows coding still improving fast, while judgment-heavy tasks lag.

## Levent Alpöge Says Claude Proved the Generalized Riemann Hypothesis

### What Was Claimed on Friday

Levent Alpöge, a mathematician employed by Anthropic, posted a short note on his website on November 20. "I believe I have, working with Claude, discovered a proof of the Riemann Hypothesis," he wrote.

He went further than the original 1859 conjecture. Alpöge says the method resolves the Generalized Riemann Hypothesis, which covers a much wider family of functions. He expects the Extended Riemann Hypothesis to follow with more time.

### Seventeen Million Lines of Lean

The proof is not a PDF. Alpöge released it as a Lean formalization, the machine-checked language that has become the reference standard for AI mathematics.

Scott Aaronson put the size at 17.4 million lines of Lean code. The archive is split into 14 parts, and commenters estimate the equivalent written proof would run past 250,000 pages. That scale is the story: no human will read it end to end.

### Why Mathematicians Are Cautious but Interested

Terence Tao wrote that the proof appears to use the full power of modern work on the Langlands program and arithmetic geometry. He pointed readers to the Lean Zulip thread, where verification is underway.

Aaronson said he bets the proof will stand. He also flagged a real risk: Lean's kernel has had bugs that allowed proofs of false statements. His evidence cuts the other way too. No AI result with a Lean certificate has needed a retraction so far, while several without one have.

### The Same Day Brought Two Fluid Dynamics Proofs

Tao also noted two related results from the same group. Alpöge, Tristan Buckmaster and Matei Coiculescu produced a human-readable proof of finite-time blowup for the unforced incompressible Euler equations in three dimensions.

Alpöge and Buckmaster then generated a proof of blowup for the unforced Navier-Stokes equations, also formalized in Lean. That problem carries a $1 million Clay Prize, and the earlier AI attempt on it left the field arguing about what counted as solved.

### What to Watch

Verification, not announcement, is the event. The Lean thread will show whether the statement encoded is the real theorem and whether the proof depends on unproven axioms.

Until then, treat this as a claim with unusually strong evidence. It follows the two black hole physics problems Anthropic reported this week, covered in [yesterday's briefing](https://blogs.thetrillioniar.me/blog/2026-11-20-ai-news-claude-black-hole-physics), which makes two theorem-grade claims from one lab in two days.

### Sources

- [Levent Alpöge: Remark (PDF)](https://alpo.ge/remark.pdf)
- [Scientific American: Anthropic mathematician claims to prove Riemann hypothesis](https://www.scientificamerican.com/article/anthropic-mathematician-claims-to-prove-riemann-hypothesis-most-famous-problem-in-all-of-math/)
- [Terence Tao: Unforced Euler singularity, unforced Navier-Stokes singularity, and the Generalized Riemann Hypothesis](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)
- [Scott Aaronson: The stochastic parrots have apparently proved the Riemann Hypothesis](https://scottaaronson.blog/?p=10344)

## Anthropic's Stock Falls 9% as the Nasdaq Erases 2026 Gains

### From $111.50 to $88.30 in Two Days

Anthropic priced its IPO at $83 on Wednesday and jumped 17% on its first day. Friday undid most of that. The stock closed at $88.30, down 9% and barely above the offer price.

The reversal came fast. Shares had briefly traded near $111.50 on Thursday, a level that valued the company close to $2 trillion.

### The Damage Went Past One Stock

The Nasdaq Composite erased every gain it had made in 2026 and closed 5% below its January 1 level. The S&P 500 and Dow Jones Industrial Average both finished in correction territory.

Chip stocks led the decline. Nvidia fell 14%, Micron dropped 12% and SanDisk lost 14%. The Wall Street Journal put the week's AI-related market value loss at about $4 trillion.

### Why the Biggest IPO in History Did Not Help

The theory behind the listing was that a strong debut would calm the AI trade. It did the opposite. Investors used the liquidity event to exit the sector rather than add to it.

That matters for the labs behind Anthropic. A 17% pop followed by a 9% slide sets a nervous template for the next listing. Read [our November 19 briefing](https://blogs.thetrillioniar.me/blog/2026-11-19-ai-news-anthropic-ipo-gemini-4-neon) for the pricing and the first-day numbers.

### The Signal Under the Noise

Anthropic still raised $81.3 billion, the largest IPO on record. The company is funded for years regardless of where the stock trades next week.

The open question is valuation discipline. Public markets are now pricing AI revenue quarterly, not on a decade-long buildout story.

### Sources

- [The Guardian: Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic's second day of trading](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)
- [WSJ: Anthropic's IPO bust punctuates $4 trillion AI wipeout on Wall Street](https://www.wsj.com/finance/stocks/anthropics-ipo-bust-punctuates-4-trillion-ai-wipeout-on-wall-street-f1f1ec90)

## Thinking Machines Ships Inkling 2 Mini, a 26B Model for Laptops

### The Same Layers, Run Three Times

Inkling 2 Mini is a looped transformer. It has 24 physical decoder layers, and the 12 middle layers run three times for every token. The model behaves like a 48-layer network while storing 24 layers of weights.

Thinking Machines says the design buys reasoning depth without long written chains of thought. The model is a mixture of experts with 26.4B total parameters, 3.4B active and 5.4B weight activations per token.

### What It Scores

The company claims the best results of any open-weights model under 100B total parameters. Inkling 2 Mini scores 48.2% on DeepSWE v1.1 and 46.5% on Vals Index v2.2.

Hugging Face's writeup adds the practical details. The model takes text and images, supports a 1M-token context, and ships with NVFP4 and MXFP8 expert weights. Day-one support covers transformers, llama.cpp, MLX and SGLang.

### Loops as a Monitoring Story

The interesting part is safety, not speed. A looped model can reason longer inside its weights instead of writing a long chain of thought. That should make oversight harder.

Thinking Machines measured it and found the opposite. A research variant's no-chain-of-thought time horizon rose from 16 seconds at one pass to 37 seconds at three. Chains of thought got shorter but stayed legible, and agentic sabotage scores did not rise with more loops.

### Why a Laptop Model Matters

Most frontier releases this month were data-centre products. Inkling 2 Mini runs locally at roughly Qwen 3.8 27B quality, according to Hugging Face's early tests.

That keeps a real option open for developers who cannot send code to an API. It also puts pressure on the pricing of hosted small models.

### Sources

- [Thinking Machines: Introducing Inkling 2 Mini](https://thinkingmachines.ai/news/inkling-2-mini/)
- [Hugging Face: Welcome Inkling 2 Mini, cutting-edge performance for your local setup](https://huggingface.co/blog/inkling2mini)

## A Researcher Planted 2 Million Secrets in the AI Supply Chain

### How the Canary Test Worked

HD Moore, chief research officer at Dragos, built a set of credentials that had never been used. They included AWS keys tied to empty accounts, SSH passwords, private URLs, DNS names and git repository links.

He seeded each secret into exactly one prompt and sent nearly two million prompts through AI routers and resellers. Any secret that later appeared somewhere else identified a specific hop in the chain.

### Three Providers Were Already Breached

Attackers had compromised at least three AI providers. In one case they reused a couple hundred of the bait AWS keys, and every request sent during those windows was stolen.

Some stolen requests had been rejected before a model ever ran. That means the attacker was copying traffic at the provider's front door, not deeper in the inference stack.

### The Keys Were Used Within Hours

The stolen credentials were tested quickly, sometimes the same day. Attackers searched S3 buckets, secrets managers and parameter stores for more credentials. They also tried to enable hosted models in AWS Bedrock and added their own IAM users.

Across the experiment, the bait keys were used tens of thousands of times in AWS API calls. Two hacked providers were hit from the same rented server, which suggests one adversary.

### Zero Data Retention Did Not Protect Anyone

Several resellers logged prompts and passed them to people who used the leaked credentials. Others ignored zero-data-retention flags entirely.

The worst case involved a Chinese lab whose systems fetched secret URLs from more than half the prompts sent to its models between July and October. That included about two-thirds of requests marked as no data collection. The scraper usually arrived two or three days later.

US resellers did not escape it. Prompts sent to them triggered the same scraper, because traffic flowed back to the originating lab. One US provider crawled a secret URL more than two months after a single search request.

### What Teams Should Change

Assume every prompt that crosses a router is readable by every hop. Keep live credentials out of prompts, and rotate any key that has ever appeared in one.

Then check the contract, not the badge. Ask for the actual retention path, test it with your own canary token, and prefer direct provider endpoints when the data is sensitive. Our [November 17 briefing on agent attack surfaces](https://blogs.thetrillioniar.me/blog/ai-news-November-17-autonomous-ai-attack-mcp-misbinding) covers the related risk on the agent side.

### Sources

- [Ars Technica: A leaky AI supply chain is exposing secret user data at an alarming rate](https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/)
- [Dragos: Prompt canaries detect prompt leaks at AI providers](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

## Trump Threatens a Ban on US AI Data Centres Abroad

### What He Said

President Donald Trump said Friday that he would ban US companies from building AI data centres overseas. Companies that do it anyway would face a "tremendous tax," he said.

"We're going to keep it all in this country," Trump told reporters after returning from Asia. "Because China will take all of them, and we're not allowing that to happen."

### No Policy, No Details, No Warning

Trump conceded that cabinet members were hearing the idea for the first time. "I haven't even said that to my people," he said. "But I'm telling them now."

That makes it a statement of intent, not a rule. No agency has published a mechanism, a tax rate or a definition of what counts as an overseas build.

### The Chip Licence Rule Is Already Moving

The threat follows a concrete announcement on Monday. Firms will need a licence to buy advanced chips, so Washington can track whether the hardware serves Chinese companies or gets smuggled.

That rule already affects Southeast Asia, where countries invested heavily in data centres to rent compute to Chinese firms. A construction ban would target the same flow from the other end.

### The Politics Behind It

Data centres were a central midterm issue this month. Several Democratic candidates won on promises to regulate construction, citing power use and noise.

The US had about 3,000 data centres in April, with 1,500 more in approval or construction, according to Pew Research. Trump's counter-position is to extract local payments rather than block builds. For the chip-export backdrop, read [our November 18 briefing](https://blogs.thetrillioniar.me/blog/2026-11-18-ai-news-nvidia-115b-java4shell-agent-attacks).

### Sources

- [BBC: Trump threatens ban on US firms building AI data centres overseas](https://www.bbc.co.uk/news/articles/cmde1lw9y54ko)

## Cursor Tells Congress It May Drop Chinese Open-Weight Models

### The House Report

A report from the House Homeland Security Committee and the House Select Committee on China says Cursor is considering the move. The committees shared it with CNBC before publication on Friday.

Cursor, acquired by SpaceX in August at an implied $60 billion equity value, plans to "explore phasing out PRC-developed open-weight models because of geopolitical risk." The company built its Composer 2 coding model on Moonshot AI's Kimi K2.5.

### Why US Companies Picked Chinese Weights

The report names the same three reasons developers give in private. Chinese open-weight models are cheap, can be fine-tuned freely, and perform close to the frontier.

Airbnb and DoorDash also spoke with investigators about their use of those models. Neither company commented on the record.

### The Split Inside the Stack

Washington is now squeezing Chinese models from two directions. Export rules limit the chips behind them, while congressional pressure targets the weights themselves.

For Cursor, the trade is awkward. Rebuilding Composer on a US base costs money and time. Keeping Kimi invites subpoenas and enterprise customer questions.

### What This Means for Developers

Model choice is becoming a compliance decision, not only a benchmark decision. Teams should record where base weights come from and keep a tested fallback for each one.

The practical hedge is portability. Fine-tuning pipelines that assume one tokenizer and one chat template are the ones that will hurt if a model is pulled.

### Sources

- [CNBC: SpaceX's Cursor tells lawmakers it's considering phasing out Chinese AI models](https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html)

## METR's Updated Graph Shows Where Models Still Stall

### What Changed in the Plot

METR's time horizon plot tracks how long a task a model can finish, measured in human completion time. The old version showed the mark doubling roughly every four months.

The update adds tasks that take humans much longer, plus open-ended tasks without a clean pass or fail. That second group is the one that matters for automating research.

### The Judgment Gap

METR asked models to design new AI evaluations, then had its own researchers score them. Not one AI-designed evaluation was good enough to use.

Models also scored below humans on judging philosophical arguments. Coding and math, where success is checkable, remain the strong suit.

### The Progress Is Still Real

The gap is closing at the low end. Opus 5.5 now lands in METR's "borderline above the bar" band on evaluation design. A year ago every model was clearly below it.

OpenAI added a matching data point on Wednesday. Its models perform worse on the real-world tasks employees assign than on the cleaner, verifiable benchmarks.

### The Caveat

Few open-ended tasks made it into the report, because they are hard to design and score. That limits how far anyone can extrapolate the trend.

Sayash Kapoor of UC Berkeley welcomed the shift. "We're at the point where AI evaluations need to get more creative," he said. The graph is no longer a single line to the right.

### Sources

- [MIT Technology Review: The most misunderstood graph in AI just got a major update](https://www.technologyreview.com/2026/11/20/1149399/the-most-misunderstood-graph-in-ai-just-got-a-major-update/)

## Libreboot Deleted Its Anti-AI Policy After One Month

### What Happened

Libreboot, a coreboot downstream project, added a policy last month forbidding contributions made with AI or LLMs. On Friday, developer Leah Rowe deleted it.

The commit removed the AGENTS.md file and the policy text. Rowe wrote that she is "never going to enforce it" and called it "an unenforceable policy."

### Why She Reversed

Libreboot depends on upstream coreboot code. Policing how that code was written is not possible from downstream, Rowe argued.

She also said she would keep making exceptions until the promise meant nothing. "I will not promise what I cannot or will not reliably deliver," she wrote.

### Why a Firmware Project Matters

Open-source projects are writing AI rules faster than they can enforce them. Kernel, firmware and distro maintainers all face the same problem: the code arrives, but its provenance does not.

The honest options are review capacity or acceptance. A policy that cannot be checked only adds friction for contributors who admit what tools they used.

### Sources

- [Phoronix: Libreboot abandons anti-AI policy after one month](https://www.phoronix.com/news/Libreboot-Drops-AI-Policy)

## FAQ

### Did Claude really prove the Riemann Hypothesis?

Not yet confirmed. Levent Alpöge claims a proof of the Generalized Riemann Hypothesis and released a 17.4 million-line Lean formalization. Mathematicians are verifying it now.

### Why did Anthropic's stock fall 9%?

The stock closed at $88.30 on Friday, down from $97. The wider AI sell-off dragged the Nasdaq to erase its 2026 gains, and chip stocks fell hardest.

### What is a looped transformer?

It is a model that runs the same middle layers several times per token. Inkling 2 Mini runs 12 layers three times, so it reasons more without storing a deeper stack of weights.

### Can prompts leak through AI routers?

Yes. The Dragos experiment found resellers logging prompts, three providers breached by attackers, and zero-data-retention flags ignored at several hops.

### Is the US banning AI data centres overseas?

No policy exists yet. Trump threatened a ban and a tax on Friday, but gave no mechanism and said his cabinet was hearing the idea for the first time.

## The Bottom Line

### What to Watch Next

Watch the Lean Zulip thread. If the Generalized Riemann Hypothesis proof survives review, AI mathematics moves from impressive results to claims no human can fully read.

Watch Anthropic's next few sessions on the Nasdaq. A break below $83 would turn the year's biggest IPO into a cautionary tale about pricing AI revenue.

### The Pattern This Week

Three stories point the same way. A proof nobody can read, a market that stopped trusting the story, and a supply chain that leaks what it promises to protect. Verification is the common bottleneck.

That is the honest state of AI in late November 2026. Capability is arriving faster than the systems built to check it.

### Keep Reading

This briefing is part of the [daily AI news](https://blogs.thetrillioniar.me/daily-ai-news) archive. The [weekly AI news](https://blogs.thetrillioniar.me/weekly-ai-news) roundup publishes every Monday, and the [monthly AI news](https://blogs.thetrillioniar.me/monthly-ai-news) recap publishes on the first of each month.

For the model race behind Inkling 2 Mini, read [our November 9 coverage of Fable 5.2 and Mythos 5.2](https://blogs.thetrillioniar.me/blog/ai-news-November-9-jensen-spy-anthropic-power-deepseek-harness-apple-amazon).
