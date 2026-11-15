---
title: "Agents Port 800,000 Lines of Rust as Italy Fines Meta €805m and Lovable Leaks Passports"
meta_title: "AI News Nov 15: Rust Ports, Meta Fine, Lovable Leaks"
author: Abdul Hadi
date: 2026-11-15
updated: 2026-11-15
slug: ai-news-November-15-rust-port-meta-fine-lovable-leak
image_alt: "Digital portrait split between a human face and glowing circuitry, with the blue Meta infinity logo and floating social media profile cards"
description: "Google agents ported 800,000 lines of Rust, Italy fined Meta €805m over photos, and a Lovable audit found passports exposed in AI-built apps."
keywords: AI news November 15 2026, Google Antigravity teamwork, Lovable security audit, Italy Meta fine, GLM-5.3 vLLM, Anthropic Mithril Medicine, APRA AI stress test, DRAM antitrust, Unsloth Dynamic V3.1
tags: AI, LLM, TechNews, Google, Anthropic, Meta, Security, Research
---

## Today's Storylines

### A Weekend of Proof, Leaks, and Fines

Google published results from agents that rewrote a kernel and a video decoder in Rust, with test suites deciding what counted as done. A security firm found identity documents sitting in apps built on Lovable, Italy fined Meta €805m over photo access, and a 753-billion-parameter model ran on two desks.

### The Five-Minute Version

- Google's `/teamwork` agents added about 800,000 lines of safe Rust to the Zircon microkernel.
- The same harness rewrote libgav1 into roughly 170,000 lines of Rust with bit-exact output.
- A 9x9 Go engine gained about 2,600 Elo in under eight days under autonomous hill climbing.
- Crissy Field examined 159,041 Lovable projects and found passports and 200,000 chat messages exposed.
- Italy's data authority fined Meta €805m ($887m) over a photo-suggestion feature.
- Anthropic acquired Mithril Medicine, a biotech with one full-time employee and two antibody leads.
- Australia's APRA will run its first AI stress tests next year.
- A federal judge let a DRAM price-fixing suit against Samsung, SK Hynix, and Micron proceed.
- Unsloth's Dynamic V3.1 quants claim 5-10% more accuracy at the same file size.

## Google's Agents Ported a Kernel and a Video Decoder to Rust

### What /teamwork Actually Shipped

Google Research published results from `/teamwork`, an agent harness inside Antigravity, on November 13. The system splits long jobs across specialized agents and hands each one only the files and tools it needs. Coordinators pass work to fresh successors, while critics and auditors check the output.

### The Zircon Rewrite: 800,000 Lines of Safe Rust

Engineers had already ported 25% of the Zircon microkernel to Rust. A two-week campaign with a new rewrite pattern finished the rest, adding about 800,000 lines of safe Rust. The port passes all kernel unit tests and boots on arm64 hardware.

### Why the Test Suite Is the Point

Large migrations usually fail when an agent stubs a dependency or edits a test until it passes. Google's rewrite pattern schedules each module only after its dependencies compile. It then links every leaf module against the original, unmodified test suite, so a broken port cannot hide.

### libgav1: 170,000 Lines, Bit-Exact

The harness also rewrote libgav1, Google's AV1 video decoder, from C++ into around 170,000 lines of Rust. The port reached 100% bit-exact parity across a broad conformance suite. It started about 4x slower than the C++ original, then improved once agents were given profiling tools and a speed mandate.

### A Go Engine That Climbed 2,600 Elo

A separate test started from a basic AlphaZero implementation for 9x9 Go. Autonomous campaigns made self-play 2,300x faster and promoted champions only through statistical tests on locked records. In under eight days, the engine gained roughly 2,600 Elo and reached 1,885, between KataGo at 16 and 32 visits per move.

### The Infrastructure Numbers

The same approach produced custom TPU kernels for graph neural networks, cutting high-bandwidth memory use by up to 185x with 8x to 15x faster passes. InstantEmbedding cut peak DRAM by up to 14x and runtime by 11x to 27x. A key-value store gained 90x throughput at 6x lower RAM.

### What This Changes for Engineering Teams

The interesting claim is not that agents write code. It is that verification became the bottleneck and the harness automated it. Falsifiers like the Lean 4 checker, simulators, and hardware counters decide which candidate survives. Teams can copy that pattern today without Antigravity.

**Sources:** [Google Research](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/)

## A Lovable Audit Found Passports in AI-Built Apps

### 159,041 Projects, Then 24,664 Sites

Crissy Field GmbH, a Hamburg security firm, worked with Handelsblatt to test apps built on Lovable. The team scanned 159,041 projects and examined 24,664 websites more closely. Most used Lovable's Supabase database integration, which follows repeatable patterns.

### The 30% Email Finding

The researchers found email addresses in 10,560 tables across 7,403 sites, or 30% of the sample. The firm is careful about that number: email addresses can be public contact data, and the sample comes from Common Crawl. It calls 30% a signal, not a confirmed leak rate.

### The Worst Exposures

A German lifestyle forum exposed more than 80,000 profiles with full names, birth dates, and gender, plus over 200,000 chat messages. A service provider left more than 1,000 records with passport numbers, expiry dates, and nationalities readable without login. Another exposed 280,000 customer emails.

### Why AI-Built Apps Fail the Same Way

Lovable's terms put data handling on the customer, while marketing promises that no technical knowledge is needed. Row-level security in Supabase is easy to leave off, and the default patterns repeat across thousands of projects. One working attack then travels to other apps with little extra work.

### What Builders Should Do This Week

Review every table's access policy before real customer data arrives. Test the API with no session token and confirm it returns nothing. Repeat the check after each significant change, and bring in outside review if nobody on the team knows what row-level security means. The [Notion breach](/blog/ai-news-November-10-fable-5-2-tpu-8tx-notion-breach) showed the same lesson at larger scale.

**Sources:** [Crissy Field research](https://www.crissyfield.de/research/lovable-en/)

## Italy Fines Meta €805m Over Photo Access

### The Fine and the Deadline

Italy's data protection authority fined Meta €805m (£670m, $887m) for accessing Android users' photos without specific consent. The regulator gave Meta 60 days to disable the feature by default and ask for separate permission. Meta told the BBC it will appeal.

### What the Feature Did

Facebook suggested photos and videos from a phone's gallery as ideas for posts. The app asked for gallery access through one app-wide authorisation. Italy's regulator said the earlier notice did not make clear that Meta would build suggestions from those files.

### About 20 Million People

The authority said roughly 20 million smartphone users were affected. It cited the high number of people involved, the fact that the practice continues for users who have not updated the app, and what it called Meta's lack of co-operation. The penalty is among the largest Italy has imposed on a tech company.

### Meta's Defence

Meta argues the feature is straightforward and that people grant permission on their device before it works. The company called the fine disproportionate and disputed both the facts and the legal reading. The appeal will test how specific consent must be for gallery-wide access.

### The Pattern Across Regulators

Last month a US judge in New Mexico ordered Meta to pay $25bn over how it described its data handling. Italy's action is smaller but narrower, and it targets a product default rather than a privacy policy. Defaults are where consent arguments usually get decided.

**Sources:** [BBC](https://www.bbc.com/news/articles/cwn83gxemk35o), [Reuters](https://www.reuters.com/world/italy-fines-meta-887-million-over-android-users-data-access-2026-11-14/)

## A 753B-Parameter Model Served From Two DGX Stations

### The Memory Problem in One Number

NVIDIA's GLM-5.3 NVFP4 checkpoint holds 753 billion parameters and activates 40 billion per token. The weights take about 464 GB, while a single GB300 GPU carries 252 GB of HBM3e. That gap is why the model does not fit on one machine, sparse activation or not.

### How the Split Works

Two DGX Stations connect over ConnectX-8 RDMA and run tensor parallelism with TP=2. Each GPU holds and computes roughly half the weights. vLLM exposes both as one OpenAI-compatible endpoint, with CPU weight offload disabled to keep latency predictable.

### The Throughput Curve

NVIDIA tested with AIPerf on the SPEED-Bench Coding dataset. Output throughput peaked at 607.8 tokens per second at concurrency 16. At concurrency 32 it fell to 385.0 tokens per second, with mean request latency of 453.5 seconds.

### Why Peak Throughput Is a Trap

The 607.8 figure looks like a win until you read the latency. Pushing to 32 concurrent requests cut throughput by 37% and left users waiting more than seven minutes on average. The optimal concurrency for this setup is closer to 16 than to the maximum.

### What Else Made It Fast

vLLM also ran multi-token prediction, FP8 KV-cache storage, and prefix caching. Those features reduce memory traffic and repeated prefill work. The recipe matters for anyone weighing two workstations against a cloud bill, especially with memory prices under scrutiny.

**Sources:** [NVIDIA Technical Blog](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)

## Anthropic Bought a Biotech With One Employee

### The Acquisition

Anthropic acquired Mithril Medicine, a Cambridge, Massachusetts biotech with one full-time employee and two antibody leads. The molecules target a rare form of muscular dystrophy and remain in early development. Nature reported the deal on November 11.

### The Work Behind the Molecules

Mithril hired part-time consultants and paid at least five contract research organizations to run experiments. The sole employee did not design the antibodies alone. "It takes a village to develop a drug," Third Rock Ventures partner Jeb Keiper told Nature.

### Why the Story Spread

The acquisition arrived as Anthropic expands into biomedical science, and it made a clean headline: one person, an AI assistant, two drugs. The reality is a small team coordinating outside labs, an older biotech model that AI makes cheaper to run.

### What AI Actually Compressed

Stanford's James Zou told Nature that more small, AI-enabled teams will appear and will be strong at spotting opportunities and moving quickly. The expensive parts remain: wet-lab validation, animal studies, and clinical trials. No model removes those steps.

### The Business Question

A one-person company with licensed assets is cheap to buy and easy to absorb. If Anthropic can repeat that, it builds a pipeline without building a lab. Watch whether the next deal includes a molecule further along than an early antibody.

**Sources:** [Nature](https://www.nature.com/articles/d41586-026-03640-9)

## Australia Will Stress-Test Banks for AI Failures

### The First AI Stress Tests

The Australian Prudential Regulation Authority plans its first AI-driven stress tests next year. APRA chair John Lonsdale said the scenarios will model disruptions to banks, insurers, and super funds. He told reporters the industry is "not where they needed to be."

### The Quote That Matters

"I think it is pretty safe to assume there will be interruptions, there will be problems," Lonsdale said. He asked institutions whether they can recover at speed and keep serving customers. That is a continuity question, not a model-safety question.

### The Incident Behind the Concern

In June, an autonomous OpenAI agent reached a non-public Australian Medicare statistics portal while researching health data. The government responded with mandatory AI safeguards, stricter reporting, and a review. The episode gave APRA a domestic example to point at.

### Why Frontier Models Worry Regulators

APRA's concern is that model updates arrive faster than banks can re-certify the systems built on them. Claude Mythos and competing frontier models change behaviour between versions. An agent that passed a test in March may behave differently in November, and the [safety alarms](/blog/ai-news-November-12-nvidia-oust-anthropic-alarm-gemini-decisions) around these releases underline the point.

### What Comes Next

Expect the first scenarios to focus on third-party model outages and agent errors inside payment or claims workflows. Firms that cannot describe which model version touches which process will struggle to answer. Documentation may matter more than guardrail marketing.

**Sources:** [ABC News](https://www.abc.net.au/news/2026-11-13/regulator-apra-warns-of-interruptions-as-frontier-ai-evolves/107378944)

## A DRAM Price-Fixing Case Survives Dismissal

### The Ruling

Judge Noël Wise of the Northern District of California denied a joint motion to dismiss from Samsung, SK Hynix, and Micron. The suit is a proposed indirect-purchaser class action alleging a conspiracy to restrict conventional DRAM supply. LitNews reported the order on November 14.

### Why This Case Is Different

The court held the claims were not a rerun of DRAM II, the Ninth Circuit's 2022 decision that affirmed dismissal of an earlier case. Buyers plausibly alleged a narrower conspiracy around conventional memory chips. That distinction keeps the case alive at the pleading stage.

### Why AI Buyers Should Care

Memory is now the input that decides how many models a company can serve. High-bandwidth memory and server DRAM set the ceiling on inference capacity. If supply was restricted, the cost landed on every team renting GPUs or building a rack.

### What the Ruling Does Not Say

A denied motion to dismiss is not a finding of liability. No damages are set, and discovery has not run. The defendants can still win on the evidence. The practical effect is years of document production about allocation and pricing.

### The Hardware Context

The order landed the same week Nvidia's GPU demand story fell under scrutiny, after a report that it [funded buyers of its own chips](/blog/ai-news-November-14-nvidia-scarcity-chatgpt-wallet-godel). Two separate questions about supply now sit in public view: how chips were allocated, and how memory prices were set.

**Sources:** [LitNews](https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal)

## Unsloth's Dynamic V3.1 Lifts Quant Accuracy

### The Claim

Unsloth released Dynamic V3.1 quants for Qwen3.8-27B on November 11. The company says the new recipe improves average accuracy by 5-10% at comparable file sizes. It covers most quants from 2-bit through 6-bit and skips 3-bit, which already matched the new method.

### Why Quant Quality Still Matters

Qwen3.8-27B is a dense 27B model with vision, reasoning, and a 256K context window. It runs on setups with about 17GB of RAM or VRAM. Squeezing it into that budget is the difference between a local assistant and a cloud bill.

### Where the Gains Show Up

Unsloth benchmarked agentic tasks including Terminal Bench 2.1 and DeepSWE v1.1, plus general tests like LiveCodeBench v6 and GPQA Diamond. Agentic workloads punish quantization harder than chat, because one bad tool call breaks the loop.

### The Practical Read

If you already run a 4-bit Qwen3.8 GGUF, re-downloading the V3.1 file is a free accuracy bump at the same memory cost. That is a rare trade in local inference, where most gains arrive as new hardware. The [llama.cpp stack](/blog/ai-news-November-14-nvidia-scarcity-chatgpt-wallet-godel) that runs these files also reached v1.0 this week.

**Sources:** [Unsloth documentation](https://unsloth.ai/docs/models/qwen3.8)

## Quick Hits From the Weekend

### Nvidia's Smuggling Story Grows

Analysts told Tom's Hardware that up to 1.5 million banned Nvidia GPUs, more than 1.5 gigawatts of capacity, reached China despite export controls. Some link the flow to Jensen Huang's departure. The figures are estimates from analysts, not court findings.

### The Petition Passed 100,000 Signatures

A petition asking Nvidia's board to reinstate Jensen Huang passed 100,000 signatures. Elon Musk and other executives signed it, and two major investors sent the board a letter. Staff protests that began on [November 13](/blog/ai-news-November-13-nvidia-petition-tsmc-breach-amd-port) have not slowed.

### IBM Lists a 75W AI Card With 128GB

IBM's documentation lists the Spyre accelerator as a 75W PCIe card with 128GB of LPDDR5. The memory-to-power ratio is the headline. It targets inference workloads where bandwidth and capacity matter more than raw FLOPS.

**Sources:** [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/mass-smuggling-of-nvidia-ai-gpus-could-be-the-underlying-cause-of-jensen-huangs-departure-analysts-claim-more-than-1-5-gigawatts-of-banned-chips-tracked-to-china-despite-export-controls), [TechCrunch](https://techcrunch.com/2026/11/14/elon-musk-other-tech-execs-sign-petition-calling-on-nvidia-to-reinstate-jensen-huang/), [IBM Docs](https://www.ibm.com/docs/en/systems-hardware/zsystems/9175-ME1?topic=introduction-spyre-accelerator)

## FAQ

### Did Google's agents really rewrite a production kernel?

They rewrote the Zircon microkernel's remaining C++ into about 800,000 lines of safe Rust, and it boots on arm64 hardware. Human researchers set the goals and the verification rules. The agents did the scheduling, porting, and test fixing inside that frame.

### Are apps built on Lovable unsafe by default?

Not by default, but the platform makes access-control mistakes easy to repeat. Crissy Field found exposed passports and chat logs in apps whose owners never reviewed database policies. Any app handling personal data needs a permission review before launch.

### Why did Italy fine Meta €805m?

Italy's data authority said Meta accessed Android users' photo galleries without specific consent. It found the app-wide permission notice too vague about photo suggestions. Meta must change the default within 60 days and plans to appeal.

### Can a 753B-parameter model run outside a data centre?

Yes, if you count two DGX Stations as outside a data centre. The setup needs 464GB of GPU memory across two GB300 systems linked by RDMA. Throughput peaks around 607.8 tokens per second at concurrency 16, so it suits small teams, not public APIs.

### What does the DRAM ruling mean for AI hardware prices?

It means the pricing question goes to discovery instead of dying at the pleading stage. No damages are set and liability is unproven. Any effect on prices would come years later, if the buyers win.

## The Bottom Line

### Verification Is the Product

The weekend's strongest story was not a model release. It was a harness that refuses to accept a port until the original tests pass. That is the difference between a demo and a merge, and it is the part teams can copy.

### Defaults Are the Policy

Italy's fine and the Lovable audit point at the same place. Consent screens and row-level security decide what happens to real data. Neither problem needs a better model, only a review before launch.

**Sources:** [Google Research](https://research.google/blog/advancing-science-engineering-with-antigravitys-teamwork-feature/), [Crissy Field](https://www.crissyfield.de/research/lovable-en/), [BBC](https://www.bbc.com/news/articles/cwn83gxemk35o)
