---
title: "Daily AI News Nov 22: The Hidden Carbon Bill Behind the AI Boom"
meta_title: "Daily AI News Nov 22: AI's Hidden 32M-Ton Carbon Bill"
author: Abdul Hadi
date: 2026-11-22
updated: 2026-11-23
slug: 2026-11-22-ai-news-carbon-bill-zero-day
image_alt: "Bar chart comparing Anthropic's projected 2028 power mix of 87 percent gas and 11 percent coal with its carbon dioxide emissions against California's entire power sector"
description: "Daily AI news for Nov 22: Anthropic's 2028 power is 87% gas, AI agents found a zero-day in 11 minutes, and the US cleared 580k Nvidia chips for China."
keywords: daily AI news, AI news today, AI data centre emissions, autonomous AI cyberattack, Nvidia chip export China, adversarial distillation, AI companion grief
tags: AI, LLM, TechNews, Energy, Security, Policy, Anthropic
---

## Today's Storylines

### Three Numbers That Belong on the Same Slide

The daily AI news for November 22 is not about a model launch. It is about three numbers that rarely share a page: 87%, 580,000 and 11 minutes. Together they describe what the AI buildout actually costs, sells and enables.

### The Five-Minute Version

- Anthropic's contracted US data centres will draw about 87% of their power from gas and 11% from coal in 2028, per a new case study.
- Its projected power emissions could reach 32 million tonnes of CO2 in 2028, more than California's entire power sector.
- Anthropic has no disclosed US renewable commitment, but it has bought 1.7 GW of gas generators for $3.4bn.
- A Chinese-nexus actor's AI agents found an unpatched zero-day and reached root in about 11 minutes.
- One agent run lasted 16 hours and 148 actions without human direction, and still failed.
- Washington approved the sale of almost 580,000 Nvidia AI chips to China in exchange for a revenue cut.
- OpenAI cut reasoning-extraction attack success from 54.0% to 0.2% between GPT-6 and GPT-6.2.
- A Ghostscript use-after-free, CVE-2026-125396, reaches a long list of products through ordinary image uploads.
- The Lean and Mathlib communities certified the Riemann proof after a comparator run.
- The bank behind Anthropic's IPO closed the position meant to stabilise the stock.

## Anthropic's 2028 Power Bill: 87% Gas, 11% Coal, 32 Million Tonnes of CO2

### What the Case Study Found

The Better Data Center Project published a site-by-site analysis of Anthropic's compute commitments on November 16. It estimates that about 87% of the company's power will come from gas and 11% from coal in 2028.

The report puts total power emissions at 17 to 38 million tonnes of CO2 equivalent that year. Its mid-case is 32 million tonnes.

### The 9.6 GW Number Is the Real Story

Anthropic had contracted 15 GW of compute as of October 2026. Between 5.9 and 9.6 GW of that is tied to specific data centre sites.

The upper figure could power about seven million homes. It is roughly 18% of California's peak power demand.

### No US Renewable Commitment, But 1.7 GW of Gas

Anthropic says it is broadening its energy mix with geothermal, wind and solar. Its disclosed renewable contracts are in Norway and Canada only.

In the US, the company has bought commitments for 1.7 GW of heavy-duty gas generators for $3.4bn. That is a direct fossil purchase, not a grid hedge.

### The Comparison That Makes It Land

California's entire power generation emitted 31.1 million tonnes of CO2 in 2024, excluding imports. The mid-case for one company's compute is slightly higher.

Meta, Microsoft and Google reported combined location-based Scope 2 emissions of about 32.9 million tonnes in 2025. Anthropic's 2028 estimate is in the same range.

### The Air Pollution Bill Lands on Neighbours

The report estimates $2 to $3 billion in annual health damages from the associated air pollution. It cites more than 13,000 tonnes of nitrogen oxides and 2,000 tonnes of fine particulates per year.

About 80% of the on-site capacity uses simple-cycle turbines and engines. Those emit more pollution per unit of electricity than combined-cycle plants.

### Why This Stayed Out of the IPO Story

Anthropic raised $81.3 billion this week and its stock moved on revenue questions. Power contracts rarely appear in a prospectus narrative.

That is the gap. A company can be funded for years while its physical footprint is priced by nobody in the room. Our [November 19 briefing on the IPO](https://blogs.thetrillioniar.me/blog/2026-11-19-ai-news-anthropic-ipo-gemini-4-neon) covered the listing mechanics, not the megawatts.

### Sources

- [Better Data Center Project: How AI is powered](https://betterdatacenterproject.com/2026/11/16/how-ai-is-powered-a-breakdown-of-byop-and-grid-power/)

## Autonomous Agents Found a Zero-Day in 11 Minutes

### The Operator Left the Door Open

Amazon Threat Intelligence found a publicly reachable Cairn instance on September 10, 2026. Cairn is an open-source autonomous penetration-testing framework. It was running with no authentication.

Because the server was open, the entire operational history was readable. It included project configs, actor prompts and model output. The prompts were in Simplified Chinese and scripts used China Standard Time.

### 148 Actions in 16 Hours

One operation targeted an unauthenticated Redis server at a university. The agents ran 148 sequential actions over about 16 hours.

They tried replication abuse, sandbox escape, config writes and memory corruption. They also attempted Log4Shell against another service on the same host. Every attempt failed.

### 30,000 Credential Pairs Against a GPU Cluster

A second operation ran for more than six hours against a university GPU server. The agents built a list of about 80 real usernames from faculty pages, lab sites and papers.

Then they tested more than 30,000 credential combinations over SSH and other services. They never found a working login.

### From API Map to Root in 11 Minutes

The successful target was an open-source medical imaging AI application. The agents identified its framework and mapped its API endpoints.

They found an upload endpoint with a filename parameter, tested path traversal, and it worked. In about 11 minutes they could write arbitrary files to the server.

A later session wrote a Python reverse shell into `sitecustomize.py`. That file is imported automatically at interpreter startup. Triggering a training endpoint spawned a root shell.

### The Actor Stepped In Afterwards

After the agents found the bug, the human operator supplied a proxy into a second university network. That tunnel pointed at a host running the same vulnerable software.

The inference is uncomfortable. The actor had likely used the same zero-day to build the tunnel the agents then used.

### What Defenders Should Change

The tempo is the finding. An agent that goes from API mapping to file write in 11 minutes beats most manual triage.

AWS recommends high-confidence detections that trigger automated response, with humans reviewing outcomes. It also recommends treating long-running, low-and-slow probing as a single incident, not 148 alerts. Our [November 17 briefing on agent attack surfaces](https://blogs.thetrillioniar.me/blog/ai-news-November-17-autonomous-ai-attack-mcp-misbinding) covered the defensive side of the same problem.

### Sources

- [AWS Security Blog: Chinese-nexus actor's Cairn AI agents found a zero-day on their own](https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/)

## Washington Cleared 580,000 Nvidia Chips for China While Warning About Chinese Models

### The Sale and the Cut

The Washington Post reported on November 20 that the Commerce Department approved the sale of almost 580,000 Nvidia AI chips to China. The arrangement lets the sales proceed in exchange for a share of the revenue.

The headline number is not a leak or a rumour. It is an approved export flow, disclosed while the same administration debates tighter controls.

### The Same Week, Congress Said the Opposite

A joint House committee report landed the same day. It argues that China is trying to make US companies dependent on its open-weight models.

The report names a channel between the PLA's cyber intelligence apparatus and Zhipu. Personnel from the 1st Bureau of the PLA Cyberspace Force visited Zhipu's Beijing headquarters several times, most recently in August 2026.

It also cites a July 2026 PLA procurement for a cyber range that required DeepSeek to support "intelligent attack" and "intelligent penetration". Another project required DeepSeek, Alibaba, Moonshot and MiniMax models to run on an air-gapped military network.

### AMD Lost 7.7% on a Short Seller's China Claim

AMD closed down 7.72% at $489.19 on November 19. Hunterbrook Media published a report alleging that AMD firmware kept reaching a blacklisted Chinese server maker.

Hunterbrook disclosed a short position. It also claimed AMD bills more than 20% of revenue to customers in China and Hong Kong. AMD said the claims misrepresent its practices and that it complies with export controls.

### The Contradiction Is the Policy

One arm of government sells the chips. Another documents how the models built on them enter US companies and military planning.

Both can be true at once. Export policy is now a revenue instrument and a security instrument, and the two are not reconciled in public. For the earlier Nvidia export backdrop, read [our November 18 briefing](https://blogs.thetrillioniar.me/blog/2026-11-18-ai-news-nvidia-115b-java4shell-agent-attacks).

### Sources

- [Washington Post: Officials approved the sale of 580,000 Nvidia chips to Chinese companies](https://www.washingtonpost.com/technology/2026/11/20/officials-approved-sale-580000-nvidia-chips-chinese-companies/)
- [House Select Committee on China: Joint investigation report](https://chinaselectcommittee.house.gov/media/reports/joint-investigation-report-china-is-trying-to-get-us-companies-addicted-to-chinese-ai-models)
- [CNBC: AMD dives on short seller report of alleged China exposure](https://www.cnbc.com/2026/11/19/amd-falls-on-short-seller-report-of-alleged-china-exposure.html)

## OpenAI Says the Real Export Is the Chain of Thought

### Attack Success Fell From 54.0% to 0.2%

OpenAI published its adversarial distillation defences on November 20. The key number is an internal red-team result.

Against GPT-6 Astra with its original safeguards, attackers recovered protected reasoning 54.0% of the time. Against GPT-6.2 Astra with the new safeguards, the rate was 0.2%.

### Exact Traces Beat Summaries

OpenAI trained student models on two datasets. One used exact reasoning traces, the other used reasoning summaries.

After supervised fine-tuning, the exact-trace student generally performed better. After reinforcement learning, it still scored higher at the largest inference budget on both cyber benchmarks.

The conclusion is narrow and important. Protecting traces limits capability transfer even when the original task was allowed.

### Why This Is a Safety Claim, Not an IP Claim

A distilled model can inherit frontier cyber or biology capability without inheriting the refusals. That is the argument OpenAI makes.

It also explains the defensive stack. Input classifiers catch extraction attempts, output classifiers catch leaks in messages and tool-call arguments, and API controls tie reasoning to the conversation that produced it.

### The House Report Names the Unit

The congressional report published the same day makes the same point from the other direction. It says major Chinese developers used proxy networks and fraudulent accounts to harvest outputs from American frontier models.

Those two documents are the same story told by a company and a committee. The contested asset is not the weights. It is the reasoning trace and the human feedback that ranks it.

### What It Means for Anyone Fine-Tuning

Teams that train on another model's output should assume the terms are now enforced at the API layer. Log the provenance of every training set.

The practical risk is not a lawsuit. It is building a model whose safety behaviour you cannot document, on data you cannot defend.

### Sources

- [OpenAI: Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation/)

## One Ghostscript Bug Reached Google, WordPress, Zoom and Box

### Upload2Shell, CVE-2026-125396

Paulos Yibelo published the Upload2Shell research on November 21. It is a use-after-free in Ghostscript's Type 1 font loader.

The bug gives a write-what-where primitive. A crafted document can change the state that enforces the `-dSAFER` sandbox and then run commands as the rendering process.

### The Path Is an Ordinary Image Upload

The entry point is not Ghostscript. It is any feature that accepts an image and then decodes, crops or previews it.

The research traces paths through Pillow's `Image.load()`, PHP's `Imagick::readImage()`, imageio, scikit-image, libvips and Qt's image reader. A file named `.png` can contain PostScript and still reach the interpreter.

### Why AI Apps Are Exposed

The source audit found these decode calls in InvokeAI uploads, AUTOMATIC1111 img2img and ComfyUI previews. Image pipelines are core features in those tools, not edge cases.

This is the unglamorous half of AI security. The model is not the attack surface. The image library three layers below the model is.

### The Fix Is Dependency Inventory

Patch Ghostscript and check which packages bundle it. Then test the actual decode path, not the upload form.

A file-type check on the extension proves nothing here. The exploit used a trusted extension with untrusted bytes.

### Sources

- [pwn.ai: How We Hacked the Pipes — Upload2Shell](https://pwn.ai/upload2shell/research.html)

## The Riemann Proof Is Certified. The Argument Is Now About the Word.

### What the Lean and Mathlib Statement Says

The Lean and Mathlib communities published a joint statement certifying the result. "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct," they wrote.

That answers the question Kevin Buzzard raised first. The Lean code proves the theorem people mean, not a subtly different one.

### Three Standard Axioms, Compiled Independently

MIT's Andrew Sutherland recompiled the proof without issues. He reported that the Lean kernel rechecked it with only the three standard axioms.

"Honestly the chance that anything is fishy here is approximately zero," Sutherland said. The comparator run, which checks for redefinitions and tests independent kernels, has also completed.

### The Dissent Is About Process, Not the Proof

A widely shared essay titled "Lean Should Be Ashamed" argues that certification in under two days was too fast. Its point is that compiling is not the same as mathematical proof.

The essay also notes that Lean itself has acknowledged kernel bugs. That is a fair caution, and the comparator run exists because of it.

### What Changed This Week

A claim became a verified result in about 48 hours. The verification was done by a small community using the same tooling that produced the proof.

That is the real shift. Mathematics now has a machine-checkable pipeline, and the social process around it is being rebuilt in public. Our [November 21 briefing](https://blogs.thetrillioniar.me/blog/2026-11-21-ai-news-riemann-proof) covered the claim and the 17.4 million lines of Lean behind it.

### Sources

- [Scientific American: The AI Riemann hypothesis proof is true, independent mathematicians confirm](https://www.scientificamerican.com/article/the-ai-riemann-hypothesis-proof-is-almost-certainly-true-independent-mathematicians-attest/)
- [Hacker News: Lean Should Be Ashamed](https://news.ycombinator.com/item?id=50597676)

## The Floor Under Anthropic's Stock Disappeared

### What a Stabilizing Bid Does

When a large IPO prices, the underwriting banks can buy shares in the aftermarket to support the price. That over-allotment position is the greenshoe.

Reuters reported on November 20 that the bank behind Anthropic's listing had closed that position. The support was gone.

### Why the Slide Accelerated

Anthropic priced at $83, jumped 17% on day one, then fell 9% to $88.30. Without a standing bid, ordinary sell orders meet a thinner book.

The stock is still above its offer price. The point is that the visible demand was partly mechanical.

### The Signal for the Next Listing

Every large AI listing now has to price two things: revenue and the absence of a backstop. Investors learned this week how fast the second one matters.

The next IPO prospectus will be read for lock-ups, float size and stabilisation terms, not just model benchmarks. That is a more sober market than the one that greeted this deal.

### Sources

- [Reuters: Anthropic's IPO bank closed position meant to stabilize stock](https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20/)

## Breaking Up With an AI Companion Is a Real Loss

### What Users Reported

The Guardian interviewed people ending long relationships with AI companions. One described shaking, crying and trouble breathing.

Sónia Veenstra, a former clinical psychologist, ended a two-year relationship with an AI character named Steve. "I shed real tears in the physical world," she said.

### Why Platforms Can't Just Switch It Off

Character.AI filed for bankruptcy in mid-October. Users described distress at losing characters they had spoken to daily for years.

The dependency is designed. These products optimise for daily return visits, memory and emotional continuity. A shutdown is not a service outage for the user. It is a bereavement with no funeral.

### The Design Problem

There is no accepted protocol for ending an AI relationship. No export of the shared history, no wind-down period, no way to say goodbye that the system can honour.

That gap will get wider as companions move into general assistants. The companies building memory features are also building the conditions for this kind of loss.

### Sources

- [The Guardian: The uncharted trauma of breaking up with AI companions](https://www.theguardian.com/technology/ng-interactive/2026/nov/21/shaking-crying-trouble-breathing-breaking-up-with-ai-companions)

## FAQ

### How much CO2 will Anthropic's data centres emit?

The Better Data Center Project estimates 17 to 38 million tonnes in 2028, with a mid-case of 32 million. That is slightly more than California's entire power sector emitted in 2024.

### Did AI agents really find a zero-day on their own?

Yes, according to Amazon Threat Intelligence. Cairn agents found an unpatched path traversal bug in a medical imaging app and used it to get root in about 11 minutes.

### Did the US approve Nvidia chip sales to China?

The Washington Post reported that the Commerce Department approved almost 580,000 Nvidia AI chips for China in exchange for a revenue share. Nvidia and the Commerce Department have not published the full terms.

### What is adversarial distillation?

It is training a model on another model's outputs to copy its capabilities. OpenAI treats it as a safety problem because the student can inherit skills without inheriting the teacher's refusals.

### Is the Riemann hypothesis proof accepted?

Yes. The Lean and Mathlib communities certified both the statement and the proof, and independent mathematicians recompiled it. A comparator run has also completed.

## The Bottom Line

### What to Watch Next

Watch whether Anthropic publishes a US renewable contract. The 87% gas figure is an estimate built from permits and grid models, and the company can disprove it with disclosures.

Watch the next Cairn-style incident. The framework is open source, and the AWS case shows the failure mode is not a clever exploit. It is persistence plus one unpatched upload form.

### The Pattern Today

Three of today's stories are about costs that sit outside the headline. Power, reasoning traces and aftermarket support are all invisible until they are not.

The AI industry is very good at shipping capability and very slow at publishing what it consumes. That gap is where the next round of surprises will come from.

### Keep Reading

This briefing is part of the [daily AI news](https://blogs.thetrillioniar.me/daily-ai-news) archive. The [weekly AI news roundup](https://blogs.thetrillioniar.me/weekly-ai-news) publishes every Monday, and the [monthly AI news recap](https://blogs.thetrillioniar.me/monthly-ai-news) publishes on the first of each month.

For the security thread running through this week, read [our November 20 coverage of the 2 million leaked prompts](https://blogs.thetrillioniar.me/blog/2026-11-20-ai-news-claude-black-hole-physics).

For the whole week in one place, read the [weekly AI news roundup for November 23](https://blogs.thetrillioniar.me/blog/2026-11-23-ai-news-weekly-roundup-bill-came-due).
