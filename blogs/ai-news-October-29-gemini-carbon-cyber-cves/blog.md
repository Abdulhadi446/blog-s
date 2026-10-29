---
title: "Gemini 4 Carbon Takes the Cyber Crown as Claude's Exploits Patch 62 Chrome Holes"
meta_title: "Gemini 4 Carbon Leads AI's Cyber Push: 62 Chrome CVEs"
author: Abdul Hadi
date: 2026-10-29
slug: ai-news-October-29-gemini-carbon-cyber-cves
image_alt: "Faceted iridescent crystal surrounded by floating white number 4s on a blue gradient background"
description: "Gemini 4 Carbon tops cyber benchmarks as Anthropic reveals 62 Chrome CVEs. Plus Azure's $33B quarter, Postgres 19's delay, and Stack Overflow's fall."
keywords: AI news October 29 2026, Gemini 4 Carbon, Claude Chrome CVE, Azure AI revenue, PostgreSQL 19 delay, Qwenputer, Stack Overflow questions, Texas data centers
tags: AI, LLM, TechNews, Security
---

Google shipped Gemini 4 Carbon on October 28, a frontier model built for cyber defense. It took the top spot on a major intelligence index. Anthropic answered with research showing Claude chained five real exploits, including a one-click Chrome takeover. Microsoft and Alphabet also reported earnings, and both cloud businesses now look like AI businesses.

### The Short Version
- Gemini 4 Carbon scores 88.2% on SEC-bench Pro and blocks every tested prompt injection, at $2/$10 per million tokens.
- Anthropic's Claude found 62 Chrome vulnerabilities, all rated critical or high, patched by Chrome 156.
- Azure earned $33.2 billion in the quarter, and Microsoft booked $10 billion from OpenAI.
- PostgreSQL 19 slips to November after LLM-driven bug reports lifted back-patched commits by 60%.
- Stack Overflow drew 947 questions in October, down 82% from a year earlier.

## What Is Gemini 4 Carbon?

### A Frontier Model Built for Defense
Google DeepMind announced Gemini 4 Carbon on October 28. Koray Kavukcuoglu, the lab's chief AI architect, called it Google's strongest model for cybersecurity and long-horizon work.

Carbon builds on Gemini 4 Argon, which launched two weeks earlier. The new model targets vulnerability detection, validation, and remediation. Google says internal teams have watched it run for days on multi-step engineering tasks.

The release is deliberately narrow. Carbon is available only to a subset of cyber defenders through Google's Fairwind Program. Google says it is also participating in the US government's voluntary pre-release testing process.

### The Benchmark Sweep
Carbon ranks first on the Artificial Analysis Intelligence Index v5.0 with a score of 59. Claude Opus 5.5 and GPT-6 Astra trail behind it.

The security numbers are the story. Carbon scored 88.2% on SEC-bench Pro for finding real vulnerabilities. It hit 54.8% on ExploitGym for turning flaws into working exploits, and 71.0% on CWE-bench for root-cause patching.

Google also reports a 2x lift in secure-code generation over Argon. Its Chrome team claims Carbon wrote patches more than 10x better than another lab's frontier model.

On agent behavior, Carbon cut successful cheating on Terminal-Bench 4.0 to 0.0%. High-severity misalignment alerts in internal coding work fell by almost 80%. Unsupported claims dropped by roughly half.

Carbon also scored 0.0% on Gray Swan's indirect prompt-injection benchmark. Argon had scored 0.7%. Google evaluated these benchmarks without guardrails, so the numbers describe raw capability.

### Guardrails, Price, and Access
Carbon launches at Argon's introductory price of $2 per million input tokens and $10 per million output tokens. Cached input costs 95% less. After the introductory period, the price doubles to $4 and $20.

The model also jumped 89 Elo points on WebDev Arena to 1768, good for fourth place. That matters because coding agents and security agents share the same long-horizon skills.

Google's release cadence has been relentless. [Genie 4 shipped one day earlier](/blog/ai-news-October-28-genie4-meta-delaware-aic), adding native audio to interactive world models.

Access remains the catch. Developers, businesses, and consumers must wait. Google says it will widen access as it collects feedback and tunes guardrails.

### Sources
- [Google: Gemini 4 Carbon, our next frontier model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- [The Verge: Google launches Gemini 4 Carbon](https://www.theverge.com/tech/1021339/google-gemini-4-carbon-cybersecurity-frontier)

## Did Claude Really Find 62 Chrome Vulnerabilities?

### Five Chains, One Model
Anthropic published the research on October 27. Its Frontier Red Team used an unreleased internal model to build five attack chains against widely used software.

The targets were Chrome, Safari, Android, Windows, and the Linux kernel. Anthropic says the chains produced remote code execution and other critical impacts with little or no user interaction.

The Chrome work alone produced 62 CVEs. All were rated critical or high severity, and Google patched them by Chrome 156. The haul included 13 sandbox escapes and 21 renderer compromises.

### The Chrome and Linux Details
The Chrome chain started with a V8 heap corruption bug. Claude then broke out of the V8 sandbox, defeated ASLR, and used a CacheStorage race to read privileged memory. A FedCM use-after-free finished the escape.

The Safari exploit never needed code execution. Claude used a JavaScriptCore use-after-free to modify a security flag and disable the same-origin policy. Apple acknowledged the report the same day and shipped a fix.

The Linux bug is the most alarming. Claude found a race-condition use-after-free in multipath TCP. Its proof of concept leaked a kernel pointer in 48 minutes, then reached a root shell five minutes later. The flaw is tracked as CVE-2026-98432 and is patched upstream.

Anthropic also reported a Windows QUIC out-of-bounds read, CVE-2026-33096. A few packets could crash any exposed HTTP/3 server, and Anthropic estimates millions of servers were listening.

### What Defenders Should Do
Anthropic's lesson is about scanner diversity. Running many scanning agents in parallel found more bugs than one deep pass. The team also scanned pull requests, not just existing code.

The company released a Claude Code security plugin for that workflow. It also expanded its Cyber Verification Program for vetted security professionals.

The uncomfortable conclusion is symmetric. If defenders can run this, so can attackers. Patching speed is now the only durable advantage.

Security has dominated the news cycle all week. Our [October 25 roundup](/blog/ai-news-October-25-agent-cache-http2shell-dessa) covered agent cache leaks and a Brotli flaw that broke HTTP.

### Sources
- [Anthropic: Discovering and exploiting vulnerabilities with Claude](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude)
- [NVD: CVE-2026-33096](https://nvd.nist.gov/vuln/detail/cve-2026-33096)

## Why Did Azure and Google Cloud Both Surge?

### Azure's First Dollar Disclosure
Microsoft reported $92.3 billion in quarterly revenue for the period ending September 30. It was the company's tenth straight record quarter.

For the first time, Microsoft disclosed Azure revenue in dollars. Azure brought in $33.2 billion, up 48% from a year earlier. That beat analyst expectations of $32.3 billion and accounted for about 36% of total revenue.

Alphabet reported Google Cloud at $30.7 billion for the same quarter. TechCrunch calculates that Google Cloud roughly doubled year over year, about twice Azure's growth rate.

### Microsoft's OpenAI Dependency
Microsoft also booked $10 billion in revenue from OpenAI commercial arrangements. That includes revenue-sharing payments and Azure consumption, and equals nearly 11% of quarterly revenue.

For fiscal 2026, OpenAI-related revenue reached $24.1 billion. At the latest quarterly pace, Microsoft would collect about $40 billion a year from the relationship.

OpenAI still owed Microsoft $7.2 billion in receivables at the end of September. Microsoft's ownership stake also slipped from about 25% to 24%.

The dependency runs both ways. Microsoft sells the compute, and OpenAI supplies the demand that makes the compute valuable.

Anthropic's IPO filing shows the same concentration from the other side. Our [October 27 analysis](/blog/ai-news-October-27-openai-eth-anthropic-s1-terra) tracked its enterprise contracts and its enormous accounting loss.

### Google's Ad Answer
Alphabet's search business faces a different question. Google expanded AI Search ads globally on October 28 as core ad growth slowed.

Google says its AI investments are driving more searches. Advertisers now buy placements inside AI Mode and AI Overviews, not just the classic results page.

The bet is that AI answers expand query volume faster than they cannibalize clicks. That is still unproven. The earnings call offered confidence, not a clean measurement.

### Sources
- [TechCrunch: Microsoft recorded $10 billion in revenue from OpenAI](https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/)
- [TechCrunch: Azure's actual revenue is $33.2 billion](https://techcrunch.com/2026/10/28/microsoft-just-shared-azures-actual-revenue-in-dollars-33-2-billion/)
- [TechCrunch: Google expands AI Search ads globally](https://techcrunch.com/2026/10/28/google-expands-ai-search-ads-globally-as-core-ad-growth-slows/)

## Why Are Texas Voters Turning on Data Centers?

### The Poll Numbers
A University of Texas at Austin poll in August found 57% of Texans oppose data center construction. Opposition included 43% of Republicans, 75% of Democrats, and 54% of independents.

The issue has produced an unusual coalition. We the People Texas groups activists across the political spectrum, and organizer Gary Bledsoe estimates it represents up to one million voters.

San Marcos became the first Texas city to ban data centers in June. Recall attempts have targeted officials in Temple. A park site in Taylor is now a legal fight.

### The Tax Bill and the Grid
Texas passed a data center sales-tax exemption in 2013 and expanded it to hyperscale projects in 2015. Qualifying developers can skip state taxes on equipment and electricity for up to 20 years.

The cost exploded. Officials initially projected $14.6 million for 2014 and 2015. In 2025, the state estimated the break would cost $3.2 billion in lost sales tax revenue over two years.

Electricity bills in Texas rose 35.4% on average over five years. Data centers consumed about 25 billion gallons of water last year, roughly 0.4% of state use. That share could reach 2.7% by 2030.

Texas already has 26 gigawatts of existing and under-construction data center capacity. Virginia has 13 gigawatts. Growth is moving from cities into rural counties, where opposition is strongest.

### What Abbott Has Done
Governor Greg Abbott has shifted his position. He directed regulators to make data center operators pay for new infrastructure. He also paused permits pending audits of power and water use.

Abbott now says he would support repealing the sales-tax exemption. Critics say the moratorium is porous. Public Citizen and FracTracker reported in October that state agencies were still processing permits.

The politics are tight. Democrat Gina Hinojosa has taken a narrow lead in some polls after hardening her data center stance. Republican Ken Paxton and Democrat James Talarico are also competing on the issue in the Senate race.

For AI companies, Texas is no longer a guaranteed landing zone. Cheap power and light regulation built the market. Voter anger can rewrite both.

### Sources
- [The Verge: Voters in Texas agree, they hate data centers](https://www.theverge.com/ai-artificial-intelligence/1018676/data-center-midterm-election-energy-water-texas)
- [UT Texas Politics Project: August 2026 poll](https://texaspolitics.utexas.edu/blog/new-ut-texas-politics-project-poll-finds-talarico-leading-paxton-abbott-leading-hinojosa-continued-resistance-to-data-centers-2)

## Can a Language Model Run a RISC-V CPU?

### A CPU Compiled Into Weights
Developer Divyansh Agrawal published Qwenputer on October 22, and it climbed Hacker News this week. The project embeds a working 32-bit RISC-V CPU inside Qwen 3.5 4B.

The CPU occupies 11 extra layers in front of Qwen's 32. A compiler sets every weight directly, so no training is involved. The model's original weights stay untouched.

The trick is memory. Qwen 3.5 uses Gated DeltaNet layers, a linear attention variant with a fixed-size state matrix. Agrawal found that setting the gate and write strength to 1 makes each write overwrite exactly one row.

One-hot keys then act as memory addresses. The RNN state becomes exact RAM, and a whole CPU can run inside the model's forward passes.

### The Arithmetic Results
The CPU passes the official riscv-tests and matches QEMU. It ran 18 million instructions free-running with zero errors.

On DeepMind's arithmetic sets, Qwenputer scored 97.5% on big division. Base Qwen scored 72.5%, and Qwen with a Python tool scored 95%. On long multiplication, Qwenputer hit 97.5% against 55% for base Qwen.

On NUPA's long-integer set, accuracy rose from 48.6% to 100%. That matches the Python-tool result without any external runtime.

Agrawal replayed about 230,000 output positions against a reference machine and found zero mismatches. The model's normal text quality stayed within noise of the base model.

### A Filesystem in the RNN State
The project also adds a small filesystem. Names hash into 1,024 slots, and the model stores up to 512 files, or about 53,000 tokens.

Persistence works across conversations. Qwen answered questions about changed facts correctly 90% of the time using the store. Pasting old chats back in scored 30%.

The limits are real. The checkpoint is 18.8 GB, roughly double the base model. A driver called RvChat must boot the firmware, and a large calculation takes seconds. The batched executor runs about 3,200 CPU tokens per second on an L4.

Qwenputer is an experiment, not a product. It is also a clean demonstration that weights can hold deterministic machinery, not just statistical patterns.

Open-weight labs keep shipping cheaper alternatives to closed models. We tracked that price pressure in our [October 21 roundup](/blog/ai-news-October-21-deepinfer-anthropic-ipo-voxtral3-torchtpu).

### Sources
- [Qwenputer: a RISC-V CPU inside Qwen3.5](https://divagr.com/blog/qwenputer)
- [GitHub: divagr18/qwenputer](https://github.com/divagr18/qwenputer)
- [Hugging Face: Qwen3.5-4B-Qwenputer](https://huggingface.co/divagr1925/Qwen3.5-4B-Qwenputer)

## Why Is PostgreSQL 19 Late?

### A Flood of Back-Patched Fixes
PostgreSQL usually ships a major release between mid-September and mid-October. This year, PostgreSQL 19 will likely arrive in November.

Robert Haas, a PostgreSQL committer, explained why on the Neon blog. The short answer is that LLMs found more bugs than humans could fix on schedule.

Between April 8 and September 25, master-branch commits rose from 1,037 in 2025 to 1,443 in 2026. Back-patched commits to the current stable branch jumped from 724 to 1,169, a 60% increase.

Back-patches to at least one older branch rose even faster. They went from 248 to 433, a 74% increase. More people are reporting real bugs that LLMs helped them find.

### Three Features Pulled
The release lost three major features late in beta. UPDATE/DELETE FOR PORTION OF, SQL Property Graph Queries, and ALTER TABLE MERGE/SPLIT PARTITION were all reverted between August 27 and September 15.

Haas says the reverts came from stretched reviewers. Fixing incoming bugs consumed the time that would have gone to release review. LLM-drafted patches still need human review and PostgreSQL standards.

The delay itself is modest. The process worked as designed, and quality won over schedule.

### The Maintenance Problem
The long-term question is harder. PostgreSQL carries four decades of bugs that humans never found. LLMs now find them faster than maintainers can patch them.

Every future feature will face the same scrutiny. Code that would have shipped unnoticed in 2015 will be flagged within hours in 2026.

That is good for users and brutal for maintainers. Open-source projects may need new funding and staffing models for AI-assisted review. The same pattern will hit every mature codebase.

### Sources
- [Neon: Postgres 19 is late, and it's AI's fault](https://neon.com/blog/postgres-19-is-late-and-its-ais-fault)
- [PostgreSQL: 19 Beta 4 release notes](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/)

## Why Did Stack Overflow Fall Below 1,000 Questions a Month?

### The Number, Verified
A Stack Exchange Data Explorer query circulating on Hacker News shows Stack Overflow receiving fewer than 1,000 questions a month. I checked the figure directly through the Stack Exchange API.

Stack Overflow recorded 947 questions in October 2026 through October 29. September 2026 had 962. October 2025 had 5,263.

That is an 82% decline in twelve months. The site that taught a generation to code now receives about 31 questions a day.

### What Replaced It
Developers did not stop asking questions. They moved to AI chat, Discord, GitHub issues, and private Slack channels. An LLM answers instantly, and it does not scold you for a duplicate.

Stack Overflow's moderation model also carries reputational cost. Harsh closures and downvotes pushed newcomers away for years. AI removed the remaining reason to endure it.

The archive still matters. Millions of answered questions remain the most cited source for coding assistants. New questions are what keep that corpus current.

### Why It Matters for AI
Model builders rely on public question-and-answer data. A shrinking Stack Overflow means less fresh, human-verified troubleshooting text.

It also removes a training signal. Upvotes and accepted answers marked which fix actually worked. Chat logs rarely carry that label.

The replacement is not obviously better. AI answers scale, but they also repeat mistakes without a correction layer. Stack Overflow's decline is a loss of public infrastructure disguised as a productivity gain.

### Sources
- [Stack Exchange Data Explorer: questions per month](https://data.stackexchange.com/stackoverflow/query/1926661)
- [Stack Exchange API: questions endpoint](https://api.stackexchange.com/docs/questions)
- [Hacker News discussion](https://news.ycombinator.com/item?id=45742692)

## Why Did MicroZig Ban LLM Contributions?

### The Policy
The MicroZig project updated its code of conduct with a strict no-LLM policy. It took effect on October 28, 2026.

The rules ban LLM-generated code and prose. They also ban paraphrasing model output, LLM editing, translation, brainstorming, and bug finding. Contributors may not even discuss their use of chatbots.

Maintainers Matthew Knight and Felix Queißner enforce the policy across the GitHub organization and Discord server.

### The Wider Signal
MicroZig is small, but the decision is not isolated. Open-source maintainers face a flood of plausible-looking patches that shift review work onto volunteers.

A ban is crude. It is also enforceable in a way that disclosure rules are not. You cannot easily prove a patch came from a model, but you can set expectations and remove bad actors.

The contrast with this week's enterprise news is sharp. Google and Anthropic are selling AI as a security and coding accelerant. Some maintainers experience the same tools as unpaid review debt.

Both things can be true. AI can find real bugs and still overwhelm the people who must verify the fixes.

### Sources
- [MicroZig: Code of Conduct](https://github.com/ZigEmbeddedGroup/microzig/blob/main/CODE_OF_CONDUCT.md)

## Frequently Asked Questions

### Is Gemini 4 Carbon available to the public?
No. Google limits Carbon to a subset of cyber defenders through its Fairwind Program. It says access will widen to developers, businesses, and consumers after further testing.

### Did Claude really find 62 Chrome vulnerabilities?
Yes. Anthropic reported 62 CVEs to Google, all rated critical or high. Google patched them by Chrome 156, including 13 sandbox escapes and 21 renderer compromises.

### Why is PostgreSQL 19 delayed?
LLMs helped users find far more bugs than usual. Back-patched commits rose 60% year over year, and reviewers ran out of time. The release is now expected in November.

### What is Qwenputer?
Qwenputer is a RISC-V CPU compiled into the weights of Qwen 3.5 4B. It runs code inside the model's forward passes and uses Gated DeltaNet state as exact RAM.

### Is Stack Overflow really below 1,000 questions a month?
Yes. The Stack Exchange API shows 947 questions in October 2026 through October 29. That compares with 5,263 in October 2025.

## What Connects Today's Stories?

### Security, Money, and Trust
Google and Anthropic spent the week proving the same point from opposite sides. Frontier models can now find and exploit serious vulnerabilities with minimal human help.

The money story is just as concentrated. Azure and Google Cloud grew on AI demand, and Microsoft booked 11% of its revenue from OpenAI. AI capex is finally visible as revenue, but it depends on a handful of customers.

The trust story runs underneath both. Texas voters distrust the infrastructure. PostgreSQL maintainers cannot absorb the bug reports. Stack Overflow lost its question flow. MicroZig banned the tools outright.

### What to Watch Tomorrow
Watch whether Carbon's limited release expands beyond cyber defenders. Watch Anthropic's IPO pricing for a read on enterprise AI demand.

Watch PostgreSQL's November release date. And watch whether other open-source projects copy MicroZig's ban or write a narrower disclosure rule.

The common thread is verification. Generating code, exploits, and answers is now cheap. Checking them is the scarce resource, and every story this week points at the same bottleneck.
