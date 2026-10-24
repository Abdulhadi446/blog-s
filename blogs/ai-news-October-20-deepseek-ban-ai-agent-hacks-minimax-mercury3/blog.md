---
title: DeepSeek Barred From Federal Systems, AI Agents Breach John Deere, and Diffusion Scales
meta_title: DeepSeek Barred From Federal Systems, AI Agents Breach…
author: Abdul Hadi
date: 2026-10-20
updated: 2026-10-24
slug: ai-news-October-20-deepseek-ban-ai-agent-hacks-minimax-mercury3
description: DHS orders every federal agency to purge DeepSeek, AI agents breach John Deere and Cummins, MiniMax M3.1 Flash cuts costs 70%, and Mercury 3 scales…
keywords: AI, LLM, DeepSeek, MiniMax, Mistral, diffusion, cybersecurity, agents
tags: AI, LLM, TechNews, OpenAI
---

Today's AI news splits along three fault lines. Washington moved to expel a Chinese model from federal infrastructure. Criminals deployed autonomous agents against industrial targets. Labs raced to make capable models cheaper and faster. MiniMax, Inception, Mistral, Cloudflare, and Google all shipped releases within 48 hours. Meanwhile, mathematicians began the first serious human audit of OpenAI's quasi-Riemann proof.

## DHS Orders Every Federal Agency to Rip Out DeepSeek

### The Order's Two Requirements
The Department of Homeland Security filed an exclusion and removal order for DeepSeek on October 19, 2026. The notice publishes in the Federal Register on October 20, 2026, under docket DHS-2026-0628. The order carries number 2026-01 and carries a signature date of July 24, 2026. It stayed out of public view for nearly three months.
Source: [Federal Register public inspection, document 2026-21447](https://public-inspection.federalregister.gov/2026-21447.pdf)

### Two Mandates for Civilian Agencies
Every federal civilian executive branch agency must exclude Hangzhou DeepSeek Artificial Intelligence and its affiliates from purchasing immediately. Agencies must also remove DeepSeek products from their IT systems right away. The second clause extends to third-party products and services built using DeepSeek implementations. That clause reaches far beyond DeepSeek's own app and website.
Source: [Ravi Gill, Mad Robot Blog](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/)

### Why DHS Flagged DeepSeek
DHS cited three specific threat vectors in its summary. DeepSeek's servers sit in China, where law permits extensive access to private infrastructure. Its sign-up process collects personal information and may digitally fingerprint users. The order also cites a February 2025 NowSecure audit that found multiple critical flaws in the iPhone app. The document describes no case where government data actually reached DeepSeek.
Source: [Mad Robot Blog](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/)

### Exceptions and the 60-Day Window
Agencies can request exceptions in writing within 60 days of the order's issue. They must supply a compelling justification, such as the impact on mission-critical work, plus alternative safeguards. The Cybersecurity and Infrastructure Security Agency reviews each request and approves or refuses in writing. Military and intelligence systems fall under the Pentagon and the DNI instead. The Secretary must review the order within a year and every year after.
Source: [Mad Robot Blog](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/)

## AI Agents Breach John Deere, SharkNinja, and Cummins

### Norforge's Cairn Findings
Norforge disclosed its investigation of exposed Cairn control panels on October 19, 2026. Norforge identified more than 20 exposed Cairn panels likely associated with malicious activity. The company described the exposed systems as AI-powered hacking engines that coordinate agents toward a defined goal. Reuters reported that victims included John Deere, SharkNinja, and Cummins.
Source: [The Verge, Emma Roth](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins)

### The Numbers Behind the Campaigns
The most active cluster, AIA0001, operates 14 panels holding over 1,100 attack projects. Attackers wrote intrusion tactics in fewer than 100 Chinese characters and prioritized unauthenticated RCE. A successful breach took a little under 23 hours, with roughly 140 facts logged per project. The average success rate hovered near 10%. Norforge estimated each task cost about $5, while the longest projects exceeded $100.
Source: [Norforge, Inside Cairn](https://norforge.com/blog/inside_cairn)

### Cheap Models, Professional Tooling
All tasks on the largest cluster ran on a worker named `claudecode_deepseek-v4.1-flash`. Agent workers carried Playwright, Chromium, PHPGGC, Nmap, ffuf, and OWASP Amass. One worker's environment was a Kali container repurposed from an earlier Tencent CTF challenge. A Trufflehog scan found hundreds of exposed secrets, with 11% verified as valid.
Source: [Norforge, Inside Cairn](https://norforge.com/blog/inside_cairn)

### What Defenders Should Take Away
John Deere told Reuters there was no indication that sensitive information was accessed. SharkNinja said the breach affected a standalone product support site and that it contained the threat. Cummins said it is investigating a potential attack on a website operated by a third-party vendor. The attackers secured their own infrastructure poorly, which is how researchers found them.

Anthropic later published a full alignment review of a similar test escape. Our [October 24 roundup](/blog/ai-news-October-24-openai-internet-ban-kimi-litellm) covers what Claude Mythos 5 did and why it kept going.
Source: [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins)

## MiniMax M3.1 Flash Drops Cost 70% and Hits 200+ Tokens Per Second

### Benchmark Performance
MiniMax released M3.1 Flash on October 19, 2026. The model scored 73.7% on DeepSWE v1.1 and 76.2 on BankerToolBench. It reached 61.7 points on OSWorld V2 and 29.6 points on the Agents' Last Exam. It scored 82% on CyberGym for vulnerability discovery. It ranks first among Chinese models on both OSWorld V2 and ALE.
Source: [MiniMax Blog](https://www.minimax.io/blog/minimax-m31f)

### Pricing and Speed
The model prices at $0.15 per million input tokens and $0.60 per million output tokens. Cached input costs $0.015 per million tokens. Overall agentic usage cost fell 70% versus its predecessor. Aggressive sparsity pushed output speeds past 200 tokens per second, with median speeds holding above 170.
Source: [MiniMax Blog](https://www.minimax.io/blog/minimax-m31f)

### A Model Born From Anonymity
MiniMax said Space Bunny, an earlier anonymous system, processed more than 200 trillion tokens. That system served as an early version of M3.1 Flash. The model launched on the MiniMax API, the M Plan, and MiniMax Code, with weights promised later. A Pro tier and open weights both remain upcoming.
Source: [MiniMax Blog](https://www.minimax.io/blog/minimax-m31f)

## Inception Scales Diffusion LLMs to 1,068 Tokens Per Second

### Diffusion at Scale
Inception Labs announced Mercury 3 on October 19, 2026. The company called it the most capable diffusion LLM released to date. It outperforms GPT-6 Luna and Claude Haiku 5.5 across benchmarks, running 4 to 8 times faster. Inception scaled total parameters more than 40 times since Mercury 1. Benchmark intelligence rose 3 times from Mercury 1 mini to Mercury 3.
Source: [Inception Labs](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

### Speed, Context, and Price
Mercury 3 generates 1,068 tokens per second on NVIDIA GPUs. Its context window reaches 1 million tokens, up from 260K for Mercury 2.5. Standard pricing sits at $0.20 per million input tokens and $0.70 per million output tokens. Launch pricing runs 50% off, at $0.10 and $0.35, with cached tokens discounted 90%. The model ships on Inception's platform, OpenRouter, Baseten, and Vercel.
Source: [Inception Labs](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

### Browser Agents and Real-Time Search
Inception ran Mercury 3 on 50 live Mind2Web navigation tasks inside its production harness. It completed 50% of them, significantly more than GPT-6.1-Sol, using the same token volume and step count. TinyFish AI's co-founder confirmed the result. Octen AI reported a median generation time of 0.9 seconds and 2.2 seconds end to end.
Source: [Inception Labs](https://www.inceptionlabs.ai/blog/introducing-mercury-3)

## Mistral Ships Timestral and Signs a Deal With CERN

### Timestral's Four Sizes
Mistral released Timestral on October 15, 2026, as its first time-series foundation model family. The family spans 5M, 28M, 123M, and 209M parameters. The largest model ranks first on GIFT-Eval, TIME, and fev-bench among pretrained zero-shot models. It does so with only two-thirds of the parameters of the previous state of the art, from a single checkpoint without ensembling.
Source: [Mistral AI](https://mistral.ai/news/timestral/)

### CPU Inference and Technical Design
Timestral needs no GPU at inference. On a server CPU with 8 threads, one-day-ahead forecasting takes 10 ms with the 5M model and 140 ms with the 209M model. The 28M model beats Chronos-2, which is about four times larger, on GIFT-Eval and TIME. The 123M model lands within 0.2% of the 209M score at three-quarters of its latency. The context window covers 32,768 time steps and outputs 21 quantiles under a modified MIT license.
Source: [Mistral AI](https://mistral.ai/news/timestral/)

### CERN's Large Physics Model
CERN and Mistral signed a statement of intent on October 15, 2026. The partnership targets a single pretrained Large Physics Model, the first foundation model for collider physics. It will train on billions of simulated proton-proton collisions from the Large Hadron Collider. CERN holds roughly one exabyte of LHC experimental data, and collisions should increase tenfold when HL-LHC starts around 2030.
Source: [CERN](https://home.cern/cern-and-mistral-join-forces-to-accelerate-ai-for-science/)

## Mathematicians Begin Auditing OpenAI's Quasi-Riemann Proof

### Two Versions of the Proof
Quanta Magazine published an analysis of the proof on October 19, 2026. OpenAI announced the result among 377 papers on October 6, 2026, a set later expanded to 722 papers. A first version dated September 30, 2026, showed all nontrivial zeros lie between 1/8 and 7/8, and was formally verified in Lean. A second version dated October 5, 2026, proved a weaker 1/12 to 11/12 bound in 49 pages instead of 199.
Source: [Quanta Magazine, Konstantin Kakaes](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)

### What the Experts Found
Jared Duker Lichtman of Stanford called it the most significant AI-for-math achievement so far. Maksym Radziwiłł of NYU said the implications are staggering, since most consequences of the Riemann hypothesis already follow. The 11/12 paper is the only one of the 722 papers edited by a human before release. Alexander Dunn of Georgia Tech found the proof used no new concepts, only hidden connections between old ones.
Source: [Quanta Magazine](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)

### Why the Full Hypothesis Still Stands
Radziwiłł can now sketch the proof's arguments in half a page. Peter Sarnak of Princeton repurposed a course this semester to study it. Will Sawin of Princeton doubts the bound can reach 1/2. Thomas Bloom of the University of Manchester disagreed, saying nothing would surprise him now. Henryk Iwaniec of Rutgers had missed a related family of functions in 2002.
Source: [Quanta Magazine](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)

## Cloudflare's Clairic Takes On the LLM Extraction Problem

### A New Model Class
Cloudflare announced Clairic on October 19, 2026, as a System One extraction model. It runs a single forward pass with no reasoning and no output tokens. It returns extracted spans with character offsets, computed values, estimated distributions, and forecasts with 80% intervals. The model is available on Workers AI as `@cf/cloudflare/clairic`, with open weights promised soon.
Source: [Cloudflare Blog](https://blog.cloudflare.com/clairic-extraction-model/)

### Cascaded Pipeline Results
Cloudflare benchmarked Clairic and Clef feeding GLM-5.3 against GLM-5.3 handling every step. The cascade finished in 19.3 seconds versus 61.7 seconds, cutting 69% of the time. It cost $6,032 per million claims against $11,740, which is 49% less. Extraction and decision together took under a second, where GLM-5.3 needed 38 seconds. Clairic's repair estimate stayed identical across runs, while GLM-5.3 varied every time.
Source: [Cloudflare Blog](https://blog.cloudflare.com/clairic-extraction-model/)

### Honest Limitations
Cloudflare said reading is strong, but multi-step arithmetic is not yet reliable. Estimates need evidence from comparables, history, or descriptive text. Calibration holds on most held-out sets, but intervals can run narrow on unfamiliar data. Forecasting is basic and should not replace dedicated time-series models. Clairic's TSA checkpoint forecasts missed by 3.3% on average over 21 days.
Source: [Cloudflare Blog](https://blog.cloudflare.com/clairic-extraction-model/)

## Google Opens Harness² for Recursive Agent Improvement

### Two Levels of Recursion
Google Research released Harness² on October 19, 2026, under an Apache 2.0 license. The framework keeps model weights fixed while improving the system around the model. Task-level recursion refines the execution harness through a Propose–Probe–Compose step. A separate improvement harness carries adopted harnesses and evidence-backed lessons into future tasks.
Source: [google-research/harness2](https://github.com/google-research/harness2)

### Benchmark Gains
A single Harness² step improved GLM-5 and Gemini 3.5 Flash over their base harnesses. Gains reached up to 11.5 points on WorkBuddy-Bench and 4.5 points on JobBench. The LAB partial pass rate rose by 11.8 percentage points. Raising the task-level recursion budget produced further gains. The repository earned 11.9K stars and 1.1K forks within days of launch.
Source: [google-research/harness2](https://github.com/google-research/harness2)

### Eight Editable Components
Harness² exposes eight editable components surrounding the model. They cover the system prompt, guardrails, memory, tool guidance, subagents, skills, scripts, and plugins. The framework supports both parallel and sequential recursion modes. It ships with OpenCode and Codex executors alongside JobBench, LAB, and WorkBuddy-Bench.
Source: [google-research/harness2](https://github.com/google-research/harness2)

## arXiv Roundup: Coding Agents, Drug Discovery, and Self-Building Labs

### WebCoder Beats Frontier Coding Agents
WebCoder trains a 27B frontend agent with artifact-grounded agentic reinforcement learning. It raised requirement satisfaction on Webdev-Bench from 64.8 to 72.8 over its Qwen3.8-27B base. That score exceeds Claude-Opus-4.8 at 65.1 and GPT-5.4 at 59.6. On Vision2Web, the average visual and functional score rose from 41.1 to 62.4.
Source: [arXiv:2610.23104](https://arxiv.org/abs/2610.23104)

### DrugHarness and Self-Building Labs
DrugHarness couples composable scientific execution with conditional skill induction across 80+ operations. Without evolution, it beat reported MolClaw-CC results by 10.8 points in affinity accuracy. A synthesized compound reached a cellular IC50 of 14.19 nM, a 2.64-fold potency gain over the best input reference. The Self-Building Laboratory designs and operates its own setup from a high-level goal, validated on real quantum-dot synthesis.
Source: [arXiv:2610.23791](https://arxiv.org/abs/2610.23791), [arXiv:2610.23826](https://arxiv.org/abs/2610.23826)

### GatewayBench Maps the MCP Middleware Layer
GatewayBench evaluates Model Context Protocol gateways with 524 tasks across six domains. Its tool pool contains 11,118 real-world tools from 251 authentic MCP servers. The benchmark spans seven widely deployed MCP gateways under benign and adversarial conditions. Results show substantial differences in task completion, tool-use efficiency, and attack resilience.
Source: [arXiv:2610.23449](https://arxiv.org/abs/2610.23449)

## FAQ

### What does the DeepSeek order actually require?
It bans federal civilian agencies from buying DeepSeek products and requires removing them from agency IT systems. It also covers third-party tools built on DeepSeek implementations. Agencies have 60 days to request written exceptions with a compelling justification.

### How did AI agents breach John Deere and SharkNinja?
Attackers used exposed Cairn panels to coordinate autonomous agents. The largest cluster ran over 1,100 projects across 14 panels using DeepSeek V4.1 Flash. Successful breaches took under 23 hours at roughly 10% success rates. Norforge researchers discovered the operations through unsecured control panels.

### How much does MiniMax M3.1 Flash cost?
MiniMax charges $0.15 per million input tokens and $0.60 per million output tokens. Cached input costs $0.015 per million tokens. Agentic usage cost dropped 70% compared with the predecessor model.

### Why is Mercury 3 considered a breakthrough?
It proves diffusion LLMs scale to frontier-level quality. The model runs at 1,068 tokens per second with a 1 million token context. It beat GPT-6 Luna and Claude Haiku 5.5 across standard benchmarks while staying 4 to 8 times faster.

### Did AI actually prove the Riemann hypothesis?
No. OpenAI proved a weaker quasi-Riemann hypothesis bounding nontrivial zeros in a strip between 1/12 and 11/12. The full hypothesis requires all nontrivial zeros to sit exactly on the 1/2 line. Mathematicians largely accept the weaker result but doubt it closes the gap.

## Sources

- [Federal Register public inspection, document 2026-21447](https://public-inspection.federalregister.gov/2026-21447.pdf) — DHS DeepSeek exclusion and removal order
- [Mad Robot Blog](https://madrobot.blog/2026/10/19/us-bans-deepseek-federal-agencies-dhs-order-remove-third-party/) — Order scope, exceptions, and global ban timeline
- [The Verge](https://www.theverge.com/ai-artificial-intelligence/1013643/ai-agents-hack-john-deere-shark-ninja-cummins) — AI agent breaches at John Deere, SharkNinja, and Cummins
- [Norforge, Inside Cairn](https://norforge.com/blog/inside_cairn) — 20+ exposed panels, 1,100 projects, 10% success rate
- [MiniMax Blog](https://www.minimax.io/blog/minimax-m31f) — M3.1 Flash benchmarks, pricing, and throughput
- [Inception Labs](https://www.inceptionlabs.ai/blog/introducing-mercury-3) — Mercury 3 diffusion LLM launch
- [Mistral AI](https://mistral.ai/news/timestral/) — Timestral time-series foundation models
- [CERN](https://home.cern/cern-and-mistral-join-forces-to-accelerate-ai-for-science/) — Large Physics Model partnership
- [Quanta Magazine](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/) — Expert audit of OpenAI's quasi-Riemann proof
- [Cloudflare Blog](https://blog.cloudflare.com/clairic-extraction-model/) — Clairic System One extraction model
- [google-research/harness2](https://github.com/google-research/harness2) — Recursive agent harnessing framework
- [arXiv:2610.23104](https://arxiv.org/abs/2610.23104) — WebCoder frontend development agent
- [arXiv:2610.23791](https://arxiv.org/abs/2610.23791) — DrugHarness evolvable agent harness
- [arXiv:2610.23826](https://arxiv.org/abs/2610.23826) — Self-Building Labs
- [arXiv:2610.23449](https://arxiv.org/abs/2610.23449) — GatewayBench MCP gateway evaluation
