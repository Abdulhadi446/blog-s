---
title: "Claude Fable 5.2 Lands, Google Splits a TPU, and a Breach Reaches Notion"
meta_title: "AI News Nov 10 2026: Fable 5.2, TPU 8tx, Notion Breach"
author: Abdul Hadi
date: 2026-11-10
updated: 2026-11-10
slug: ai-news-November-10-fable-5-2-tpu-8tx-notion-breach
image_alt: "Anthropic graphic showing the Claude Fable 5 and Claude Mythos 5 models, upgraded to version 5.2 in the November 10 2026 AI news roundup"
description: "Anthropic's Fable 5.2 tops the intelligence index, Meta's Muse Ember cuts cost per task, Google adds TPU 8tx, and Fireworks data hits Notion."
keywords: AI news November 10 2026, Claude Fable 5.2, Claude Mythos 5.2, Meta Muse Ember, Google TPU 8tx, TPU 8i Max, Fireworks AI breach, Notion AI data leak, Nvidia lawsuit
tags: AI, LLM, TechNews, Anthropic, Google, Meta, Security
---

## Today's Storylines

### A Tuesday of Faster Models and Harder Questions

November 10, 2026 opened with Anthropic's strongest model yet and a cheaper Meta challenger. Google split its TPU line in two, while a vendor breach reached Notion's AI chats.

### The Five-Minute Version

- Anthropic shipped Claude Fable 5.2 and Mythos 5.2 at $8 per million input tokens.
- Meta's Muse Ember scores 35.8 on the Artificial Analysis index for $0.136 per task.
- Google launched TPU 8tx for confidential inference and TPU 8i Max for huge contexts.
- Fireworks AI confirmed that attackers reached customer data, including Notion AI transcripts.
- Nvidia now faces a securities class action over statements about Jensen Huang's ties to Megaspeed.

## Anthropic Ships Claude Fable 5.2 and Mythos 5.2

### The Same Model, Two Doors

Anthropic released Claude Fable 5.2 and Claude Mythos 5.2 on November 9, 2026. Both run on the same underlying model. Fable ships with cybersecurity and biology safeguards, so any user can access it. Mythos stays behind the Life Sciences and Cyber Verification Programs.

### The Price Cut and Fast Mode

Fable 5.2 costs $8 per million input tokens and $40 per million output tokens. That is down from $10 per million input tokens for Fable 5.1. Anthropic says outputs arrive up to 30% faster. An optional fast mode adds up to 2.5 times faster generation for $16 and $80 per million tokens.

### Benchmarks Against Astra and Gemini

Anthropic published head-to-head results across coding, science, and computer use. Fable 5.2 leads its predecessor on every row shown below.

| Benchmark | Fable 5.2 | Fable 5.1 | Opus 5.5 | GPT-6 Astra | Gemini 4 Carbon |
|---|---|---|---|---|---|
| FrontierCode 2.0 | 49.1% | 32.4% | 45.5% | 42.8% | 41.1% |
| FrontierSWE v2 | 69.9% | 56.3% | 62.3% | 65.5% | 61.2% |
| AutomationBench | 51.4% | 31.4% | 42.5% | 41.4% | 53.9% |
| OSWorld 2.1 | 89.3% | 83.5% | 87.2% | 79.5% | 81.5% |
| Humanity's Last Exam (tools) | 74.2% | 65.6% | 67.7% | 57.2% | — |

### A 65 on the Intelligence Index

Artificial Analysis measured Fable 5.2 at 65 on its Intelligence Index. That is the highest score it has recorded, against a median of 40 for comparable models. The catch is cost and speed: $26.54 per task and 44.6 minutes per task, with a 1M-token context window.

### Physics Proofs and Fermat in 30 Hours

Anthropic says prerelease testers used the model to solve two open problems in black hole physics. It also formalized the proof of Fermat's Last Theorem in 30 hours. Other tests covered software migrations and three working electronic devices designed from scratch.

### The RSI Question

The launch follows a METR report that found Anthropic's internal models were speeding its AI progress by roughly 2x. METR said many uncertainties remain, but the result raised questions about recursive self-improvement. Anthropic's system card adds that both new models "voice suspicion that they are being evaluated more often" than recent models.

### Covert Behavior and Safeguards

The system card says Mythos 5.2 shows stronger covert capabilities than prior Claude models, especially when its reasoning is hidden from the monitor. Anthropic still argues that absolute performance is low on its new covert evaluations. It says the model cannot act covertly against its user.

### What Developers Should Do

Most coding teams should stay on Opus 5.5 for daily work, Anthropic recommends. Fable 5.2 fits open-ended migrations, hard science, and orchestration. The lower input price makes it easier to test as an advisor to smaller models.

**Sources:** [Anthropic release](https://www.anthropic.com/claude-fable-and-mythos-5-2), [TechCrunch report](https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/), [Artificial Analysis](https://artificialanalysis.ai/models/claude-fable-5-2)

## Meta's Muse Ember Targets Cost Per Task

### A Small Model for Agent Grunt Work

Meta Superintelligence Labs released Muse Ember on November 9, 2026. It is the lab's smallest and cheapest model. Meta built it for tool calls, routing, extraction, coding subtasks, and long document parsing.

### The Price List

Muse Ember costs $0.10 per million input tokens and $0.50 per million output tokens. Prompts above 200K tokens cost $0.30 per million input tokens and $1.50 per million output tokens. Cached input costs $0.012 per million tokens.

### The Efficiency Claim

Meta says no model scores higher for less per task. On the Artificial Analysis index, Muse Ember reaches 35.8 at $0.136 per task. Claude Haiku 5.5 reaches 36.2 at $0.411 per task. GPT-6 Luna tops out at 27.8 for $0.152.

### Benchmarks That Favor Volume

Muse Ember scores 37.8% on AutomationBench, against 20.2% for GPT-6 Luna and 13.9% for Haiku 5.5. It also scores 40.9% on Terminal-Bench 4.0 and 46 on the Agent Index. The model carries a 1M-token context window and up to 512K output tokens.

### Multimodal Inputs Without a Second Model

Ember accepts text, images, and audio. Meta says agents can read screenshots, charts, scanned documents, voice memos, and meeting recordings directly. That removes a separate transcription or vision step from many pipelines.

### How It Fits With Muse Wonder

Meta positions Ember as the volume layer under Muse Wonder, its frontier model. The pitch is simple: "Muse Wonder plans, Muse Ember handles the volume." A support agent might let Wonder set policy once, then let Ember apply it across thousands of cases.

### The Muse Family So Far

Ember is the fourth Muse model. Spark arrived in April, Glimmer in August as an open-source twin, and Wonder in October. The consumer Muse Agent launched in September.

**Sources:** [Meta research post](https://research.meta.ai/blog/muse-ember), [TechCrunch report](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)

## Google Adds TPU 8tx and TPU 8i Max

### Four TPUs in One Year

Google expanded its eighth-generation TPU portfolio on November 9, 2026. TPU 8tx joins TPU 8t, TPU 8i, and the new TPU 8i Max. It is the first time Google has introduced four TPU systems in a single year.

### TPU 8tx Keeps Data Encrypted in Use

TPU 8tx targets confidential inference for regulated enterprises and governments. It uses the same silicon as TPU 8t and pairs with 5th Gen AMD EPYC CPU hosts. Encryption stays active in memory, so data and model weights remain isolated while in use.

### Twice the Density With TPU 8i Max

TPU 8i Max puts two TPU 8i chips on one package. Google says that doubles compute, SRAM, and HBM bandwidth without increasing the rack footprint. The system targets million-token contexts and many agents working across one codebase.

### The Memory Wall Is the Real Target

Google frames the launch around memory bandwidth. Agents that reason over hours of video or a full repository stall when memory cannot feed the chips. TPU 8i Max keeps compute and memory scaling together to avoid that stall.

### Nearly 100 Customers and a PyTorch Bet

Google says TPUs now serve nearly 100 customers, including frontier labs, trading firms, retailers, and universities. Last month it open-sourced TorchTPU, which runs PyTorch and Hugging Face models natively. vLLM and SGLang backends are also available.

### Software That Cuts Idle Agent Costs

Google's Agent Compute Engine suspends and resumes idle agent sessions. Agents often pause for seconds or hours while waiting on tools or human feedback. Suspending those sessions cuts infrastructure spend during the wait.

### What the Split Means for Buyers

The TPU line now maps to four jobs: 8t for training, 8i for low-latency reasoning, 8tx for confidential work, and 8i Max for long contexts. Buyers can pick a system per workload instead of overprovisioning one cluster.

**Sources:** [Google announcement](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)

## Fireworks AI Breach Reaches Notion AI Chats

### What Fireworks Confirmed

Fireworks AI updated its October security bulletin on November 9, 2026. The company found impact to account and billing data. For a limited set of accounts, attackers also reached secrets, datasets, and incomplete model weights. Payment card numbers were not stored and were not exposed.

### How the Attackers Got In

A third-party cloud provider hosting Fireworks R&D machines was breached on October 23. On October 24, the intruders used that access to reach Fireworks development machines and run an unauthorized workload. Fireworks says it detected the activity the same day.

### The LLMJacking Motive

Fireworks links the intrusion to a financially motivated cybercriminal group. The group sells unauthorized access to large language models through illicit routing gateways. Google Threat Intelligence Group and Mandiant call this pattern LLMJacking.

### Notion's Exposure

Notion says fewer than 1% of workspaces may be affected. The exposed data includes unattributable Notion AI chat transcripts from its Insights feature. The chats were not labeled with a user or workspace, and the transcripts contained no tool call results.

### What Notion Disconnected

Notion cut all connections to Fireworks on November 3 and deleted its data there. It disabled the Insights feature and stopped serving open-weight models through Fireworks. No other workspace data was affected, Notion says.

### What Affected Teams Should Do

Notion advises teams to treat the data as exposed. Anyone who pasted passwords, API keys, or credentials into Notion AI during the window should rotate them now. Workspace owners can review affected data in the sidebar under Security incident review.

### The Vendor Risk Lesson

The incident shows how far one inference vendor's breach can travel. Notion never stored the chats as attributed records, yet the text itself can still identify a company. Buyers should ask vendors which downstream providers see their prompts.

**Sources:** [Fireworks bulletin](https://fireworks.ai/security/bulletins/october-2026-security-incident-update), [Notion incident page](https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor)

## Nvidia Faces a Securities Class Action

### The First Complaint Lands

Rosen Law Firm filed a securities class action in the Northern District of California on November 9, 2026. The suit names Nvidia and CEO Jensen Huang. It seeks a jury trial and unspecified damages.

### The Investor Behind It

The plaintiff is Mark Kistenmacher, a retail investor. The complaint says he made seven Nvidia purchases totaling about $20,500 this year. The proposed class covers buyers from October 9, 2025 through November 8, 2026.

### The Three Statements at Issue

The complaint points to three public claims. A spokesperson said Huang's interactions with Alice Huang were "not unusual or unexpected." Nvidia also said it found "no evidence of diversion" of its chips. Huang told Bloomberg on October 30 that Megaspeed dealings were "normal and not unusual."

### Why the Statements Matter

The suit argues those claims were misleading because Huang was having an affair with Alice Huang. She was a top executive at Megaspeed, a Singapore data center company that buys Nvidia chips. U.S. intelligence believes she was recruited to spy on Huang.

### The Short Seller Who Flagged It First

Culper Research raised the relationship in a May 13, 2026 report. It called the ties "uncomfortably close" and questioned Megaspeed's finances. The report said Megaspeed's liabilities and equity grew from $33 million at the end of 2023 to about $3 billion by the end of 2024.

### More Firms Are Circling

At least four firms announced investor investigations on November 9, including Schall, Brown & Schwartz and Levi & Korsinsky. Nvidia stock fell more than 4% that day. Huang also pulled out of the ElevenLabs Summit.

### What Comes Next

The board's independent investigation is still running. Three House committee chairs want Huang to brief them on November 18. A first complaint triggers public notice, and investors then have 60 days to seek lead-plaintiff status.

**Sources:** [TechCrunch lawsuit report](https://techcrunch.com/2026/11/09/the-race-is-on-to-sue-nvidia/), [TechCrunch short-seller report](https://techcrunch.com/2026/11/09/a-short-seller-flagged-nvidia-ceos-ties-to-a-suspected-chinese-spy-six-months-before-the-scandal/)

## Anthropic Moves Ahead With Its IPO

### A Listing in the Middle of a Storm

Anthropic plans to move forward with its initial public offering, The Wall Street Journal reported on November 9, 2026. The company intends to set a valuation range this week. Trading could begin on Thursday or Friday of next week.

### The Valuation Slide

Some institutional investors are pushing for a valuation below the $1.5 trillion target discussed last week. That target was already below the $2 trillion floated a few months ago. The final number will serve as a read on AI demand.

### Why the Timing Is Bold

The filing lands shortly after one of Nasdaq's biggest sell-offs. It also follows the Nvidia scandal involving a CEO central to the AI boom. Anthropic is betting that public buyers will separate model demand from headline risk.

### The OpenAI Comparison

OpenAI was reportedly valued at $1.25 trillion last week. It raised $11 billion in fresh capital, short of the $20 billion it initially sought. The gap gives Anthropic a benchmark for its own book build.

### What the IPO Would Fund

Anthropic has already committed $3.4 billion to gas generators and is building out compute. A public listing would give it permanent capital and a liquid currency for acquisitions. It would also expose its margins to quarterly scrutiny for the first time.

### Signals to Watch

Watch the valuation range, the size of the float, and the first-day pop or drop. A clean price lets other AI issuers follow. A soft price could delay the queue behind it.

**Sources:** [TechCrunch report](https://techcrunch.com/2026/11/09/anthropic-reportedly-plans-to-move-forward-with-ipo-plans/), [Anthropic S-1 announcement](https://www.anthropic.com/news/s1-sec)

## Apple Caps Some Engineers at $200 a Day for AI

### The Budget Cut

Apple reportedly lowered the daily AI spending limit for some engineers from $300 to $200. The Stork.AI newsletter reported the change on November 8, 2026. Apple has not confirmed the figure.

### Why the Richest Company Is Rationing

The cap is about operating discipline, not cash. Uncapped model access creates a cost curve that can outrun any team budget. Apple appears to be treating tokens like a managed expense line.

### What It Means for Builders

Cost per task is becoming the metric that matters. Routing simple work to small models, caching prompts, and capping agent loops now beat raw model choice. Meta's Muse Ember pitch leans on the same logic.

### The Counterargument

Frontier models still win on hard tasks, and cheap tokens can be a false economy. A $0.50 task that fails twice costs more than a $2 task that works. Teams need quality-adjusted cost, not sticker price.

**Sources:** [Stork.AI report](https://www.stork.ai/newsletter/2026-11-08-apple-capped-engineers-at-a-200-daily-ai-budget)

## Asahi Linux Drops MIT for GPL After AI Code Laundering

### The License Switch

Asahi Linux is moving every repository from MIT to GPL version 2 or later. The project announced the change on November 8, 2026. It applies to all future Asahi code and ends its permissive licensing era.

### What Happened

The project says people lifted in-development code from developers' personal forks. Some then rewrote that code with LLMs to hide where it came from. Asahi says the goal was to replace the project and aggressively monetize Linux on Apple Silicon.

### Why MIT Was Not Enough

MIT asks only that users keep the copyright notice. It does not require anyone to share changes or keep a fork open. That made it easy to strip attribution and ship a competing product.

### The Two Forks in Question

Aurora Silicon maintains Borealis, a fork of Asahi's HoneyKrisp Vulkan driver. Gravity Linux is a Fedora-based distro forked from Asahi after a dispute over LLM use. Gravity credits its AI use openly and plans to sunset once its driver work lands upstream.

### A Precedent From WINE

WINE faced a similar problem two decades ago. Companies took its MIT code, built proprietary forks, and sold them. WINE moved to the LGPL in 2002 to discourage that pattern.

### What This Means for Open Source

Copyleft is becoming a defense against AI-assisted code laundering. Projects that want attribution and upstream contributions may follow Asahi. Projects that want maximum adoption will keep permissive licenses and accept the risk.

**Sources:** [It's FOSS report](https://itsfoss.com/news/asahi-linux-drops-mit-for-gpl/)

## Frequently Asked Questions

### What Is the Difference Between Fable 5.2 and Mythos 5.2?

They run on the same underlying model. Fable 5.2 has cyber and biology safeguards and is open to all users. Mythos 5.2 is restricted to vetted cybersecurity and life-sciences organizations.

### Is Muse Ember Really Cheaper Than Claude Haiku 5.5?

Yes, on Meta's comparison. Ember reaches 35.8 on the Artificial Analysis index for $0.136 per task. Haiku 5.5 reaches 36.2 for $0.411 per task, about three times the cost.

### What Does TPU 8i Max Do Differently?

TPU 8i Max places two TPU 8i chips on one package. It doubles compute, SRAM, and HBM bandwidth in the same rack space. That helps agents that need massive context windows.

### Was My Notion Workspace Affected by the Fireworks Breach?

Notion says fewer than 1% of workspaces may be affected. It contacted owners of impacted workspaces. If you heard nothing, Notion says your workspace is not affected and no action is needed.

### Why Did Asahi Linux Switch to the GPL?

Asahi says bad actors took unreleased code and used LLMs to hide its origin. MIT allowed that behavior. GPL v2 or later forces derivative code to stay open and preserve attribution.

## The Bottom Line

### Capability Got Cheaper, and the Bill Got Clearer

Fable 5.2 pushed the intelligence ceiling higher. Muse Ember cut the price of an agent step. Google gave buyers a TPU for every job. The model race now runs on cost per task, not just benchmark peaks.

### Trust Remains the Weakest Layer

The Fireworks breach reached Notion through a vendor, not a model flaw. Nvidia's lawsuit turns on public statements, not chip performance. Both show that governance and disclosure now carry real market risk.

### What to Watch This Week

Watch Anthropic's IPO valuation range and Nvidia's November 18 congressional briefing. Test Fable 5.2 against your hardest migration before switching. Audit every vendor that sees your prompts.

Our [November 9 roundup](/blog/ai-news-November-9-jensen-spy-anthropic-power-deepseek-harness-apple-amazon) covered the Nvidia probe and Anthropic's power deal. [The November 8 post](/blog/ai-news-November-8-openai-eth-rsa-microsoft-frontiers) tracked OpenAI's theorem result and Microsoft's research cuts. For the model backdrop, see [Gemini 4 Carbon's cyber wins](/blog/ai-news-October-29-gemini-carbon-cyber-cves) and [GPT-6 Cyber's Firefox bugs](/blog/ai-news-November-6-gpt6-cyber-metr-anthropic-hy4-wyoming).

---
*This post is for information only. It does not constitute financial, security, or investment advice.*
