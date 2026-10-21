---
title: "DeepSeek Ships DeepInfer, Anthropic's $80.7B Loss Lands, and Mistral's Voxtral 3 Listens"
author: Abdul Hadi
date: 2026-10-21
slug: ai-news-October-21-deepinfer-anthropic-ipo-voxtral3-torchtpu
description: "DeepSeek open-sources its production inference stack, Anthropic's draft IPO shows an $80.7 billion loss, Mistral ships Voxtral 3, Google open-sources TorchTPU, Claude designs scorpion toxin binders, and Gemini 4 Argon reaches everyone."
keywords: DeepSeek, DeepInfer, Anthropic, Voxtral 3, TorchTPU, Gemini 4 Argon, Meta Prometheus, LLM inference
tags: AI, LLM, TechNews, OpenAI
---

October 21, 2026 delivered the busiest AI news cycle in weeks. DeepSeek open-sourced the inference stack behind its production models, and Anthropic's draft IPO prospectus revealed a loss above $80 billion. Mistral shipped Voxtral 3 for voice agents, Google released TorchTPU, Claude designed scorpion neurotoxin binders, and Meta detailed its gigawatt-scale Prometheus cluster.

## DeepSeek Open-Sources DeepInfer, Its Production Inference Engine

### The Biggest Story on Hacker News Today
DeepInfer reached 2,126 points and 829 comments on Hacker News by early October 21, 2026. It became the site's top-ranked story. The repository releases the framework that powers DeepSeek's large-scale production services. It carries an Apache License 2.0 license, so commercial use is permitted.
Source: [DeepInfer on GitHub](https://github.com/deepseek-ai/DeepInfer)

### What DeepInfer Actually Contains
The framework supports DeepSeek-V4.1-Flash and defaults to the `DeepSeek-V4.1-Flash-1017` checkpoint on Hugging Face. It targets NVIDIA SM100 GPUs and Huawei Ascend 950 NPUs. Requirements include Linux, GCC 13 or newer, Python 3.12, CUDA 13, and CANN 9.2. DeepSeek built it primarily on vLLM, with inspiration from SGLang and NVIDIA's TensorRT-LLM.
Source: [DeepInfer README](https://github.com/deepseek-ai/DeepInfer)

### The Features Developers Will Actually Use
Optimized kernels include FlashMLA, DeepGEMM, DeepEP, TileKernels, DeepSelect, and custom TileLang kernels. DSpark uses confidence estimates to schedule verification of draft tokens, with a default maximum draft length of 5. Decoder SWA bounded replay truncates prefill to a 140-token suffix by default. Batch-invariant inference keeps results identical across different batch compositions, and it runs on NVIDIA today. Deterministic sampling also requires a fixed `seq_seed`. Structured outputs constrain generation to a regex, JSON schema, or EBNF grammar.
Source: [DeepInfer README](https://github.com/deepseek-ai/DeepInfer)

### Benchmarks and What Is Missing
Meta measured prefill throughput on 4 SM100 GPUs and decode throughput on 64. Each measurement stayed within one scale-up domain. The release omits a KV cache system, prefill and decode disaggregation, and load balancing across data-parallel replicas. Those pieces remain required for a complete inference service.
Source: [DeepInfer README](https://github.com/deepseek-ai/DeepInfer)

## Anthropic's Draft IPO Filing Shows an $80.7 Billion Net Loss

### What the Wall Street Journal Reported
The Wall Street Journal reported on October 20, 2026 that Anthropic logged a net loss above $80 billion in the first half of 2026. Reuters, Channel NewsAsia, and Hacker News all carried the story. The figures came from a draft prospectus for Anthropic's initial public offering.
Source: [Reuters via Channel NewsAsia, October 21, 2026](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)

### Where the $80 Billion Came From
Anthropic's loss compares with $13 billion in the same period a year earlier. The Wall Street Journal attributed $72 billion of the loss to accounting charges. Those charges reflect changes in the value of financial instruments Anthropic issued to raise money. AI infrastructure spending nearly quadrupled to almost $9 billion over the six months.
Source: [Reuters via Channel NewsAsia](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)

### Revenue Is Scaling Fast Alongside It
Anthropic's revenue reached $16.3 billion in the six months ended June 30, 2026. A year earlier, the comparable figure stood at $1.1 billion. Anthropic told investors at its San Francisco investor day that third-quarter revenue reached $16.8 billion. Claude Code remains a primary driver of that growth.
Source: [Reuters via Channel NewsAsia](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)

### The $750 Billion Compute Bet
Anthropic signalled it could spend as much as $750 billion in coming years on computing capacity. The Wall Street Journal reported roughly $450 billion in cloud agreements spanning seven to ten years. Most of those agreements are non-cancelable, which converts a flexible expense into a fixed obligation. Investors who attended the investor day discussed a valuation near $1.5 trillion. That figure sits well below the roughly $2 trillion valuation previously expected for Anthropic's November share sale.
Source: [Reuters via Channel NewsAsia](https://www.channelnewsasia.com/business/anthropic-logged-net-loss-over-80-billion-in-first-half-2026-wsj-reports-6476676)

## Mistral Ships Voxtral 3 for Real-Time Voice Agents

### Four Models and a Voice Agent SDK
Mistral published Voxtral 3 on October 20, 2026. The release bundles speech-to-text and text-to-speech models with a voice agent SDK. The SDK unites listening, reasoning, tool calling, and speaking in one streaming pipeline. The story reached 519 points and 140 comments on Hacker News the same day.
Source: [Mistral, Voxtral 3](https://mistral.ai/news/voxtral-3/)

### Transcription Accuracy Across 50+ Languages
Voxtral Small Transcribe 3 covers 50 languages, including all 24 official EU languages. Mistral says the model beats Whisper, Scribe v2, and Gemini 3.5 Transcribe on diarization and multilingual transcription. The Mini variant runs 4 billion parameters and costs $0.0035 per minute. Context biasing accepts key terms and free-form text, so engineers improve recall on jargon without fine-tuning. The Realtime variant hits sub-500 millisecond latency across more than 35 languages, with end-of-turn prediction built in.
Source: [Mistral, Voxtral 3](https://mistral.ai/news/voxtral-3/)

### Speech Synthesis and Voice Adaptation
Voxtral Mini TTS 3 adjusts emotion, pace, and emphasis to match conversational context. The model supports more than 35 languages and more than 50 dialects. Pro Voice reproduces a speaker's character and emotional range across languages. Adaptations need only 30 minutes of reference audio.
Source: [Mistral, Voxtral 3](https://mistral.ai/news/voxtral-3/)

### Sovereignty as a Feature
Mistral offers Voxtral 3 through its EU-hosted API or as a self-deployed stack. Organizations control where audio is processed and whether conversations are retained.
Source: [Mistral, Voxtral 3](https://mistral.ai/news/voxtral-3/)

## Google Open-Sources TorchTPU, a Native PyTorch Backend for TPUs

### What Google Released
Google open-sourced TorchTPU on October 19, 2026, a PyTorch backend for Tensor Processing Units. The project hit 256 points and 62 comments on Hacker News. The repository includes custom ATen kernels for PyTorch operations on TPU devices. It also ships a compilation cache that optimizes XLA computations. Version 0.2.0 is available on PyPI, and the project supports Python 3.11 and newer.
Source: [google-pytorch/torch_tpu on GitHub](https://github.com/google-pytorch/torch_tpu)

### Training and Compilation Support
TorchTPU supports distributed training with data parallelism and tensor parallelism. It integrates with `torch.compile()` for graph-mode execution. Example models cover Llama, Qwen, ResNet, DLRM, minGPT, and UNet. Documentation uses Marimo notebooks, which run directly on a v6e GCE instance. The build relies on Bazel and the `wheel_common` configuration, which routes the shared XLA/MLIR backend through one library.
Source: [TorchTPU user guide](https://torchtpu.readthedocs.io/)

### Why It Matters for TPU Shoppers
PyTorch users no longer need to abandon their training code to adopt Google accelerators. The backend keeps the familiar PyTorch API surface intact. That lowers the switching cost for teams evaluating TPU capacity against GPU pricing.
Source: [google-pytorch/torch_tpu on GitHub](https://github.com/google-pytorch/torch_tpu)

## Claude Designs Scorpion Neurotoxin Binders From Scratch

### 318,484 Designs and 211 Lab Tests
Anthropic published the campaign on October 20, 2026. An internal research Claude model worked for 64 hours with four human follow-ups. The model generated 318,484 protein designs and selected 180 for testing. The human team added 31 more designs with Claude's help, and Adaptyv Bio and Twist Bioscience tested all 211. Seventeen designs met Anthropic's binding criteria. The release includes all 211 designs plus their data on Hugging Face.
Source: [Anthropic Research](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

### Five Toxins Across Four Regions
The campaign targeted five scorpion neurotoxins from four species. The targets were Cn2 from Mexico, Ts1 from Brazil, AaH I and AaH II from North Africa, and LqhIII from the Middle East. Any two of the five toxins share only 26% to 62% sequence identity. Claude picked toxin structures from the Protein Data Bank and the AlphaFold database. It then chose five hotspot residues on each toxin for the binders to latch onto.
Source: [Anthropic Research](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

### Why This Neglected Disease Matters
Scorpions sting at least 1.2 million people every year and kill more than 3,250. Most deaths occur among children in regions with limited medical access. Traditional antivenoms come from immunized horses, take months to produce, and cover only a few neurotoxins. Anthropic has not confirmed the binders neutralize venom in a cellular environment. The company states it makes no antivenom claim.
Source: [Anthropic Research](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

### Outside Experts Weigh In
Susana Vázquez Torres of the Spanish National Cancer Research Centre called the work a promising first step. Timothy P. Jenkins of the Technical University of Denmark praised the parallel design of binders against five toxins. Both said the real challenge lies beyond binding, in making safe and affordable drugs.
Source: [Anthropic Research](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

## Gemini 4 Argon Reaches General Availability

### Pricing and Rankings
Google launched Gemini 4 Argon on October 13, 2026, and opened it to everyone shortly after. The introductory price is $2 per million input tokens and $10 per million output tokens. Cached input tokens cost 95% less. Google says Argon ranks first on the Vals Index, which measures work in finance, coding, legal, and tax.
Source: [Google, Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

### Chrome's 40 Million-Line Refactor
Argon helped the Chrome team separate core webpage handling from a legacy folder of roughly 6 million lines. That folder sat inside Chromium's 40 million-line codebase. The team piped in clean changes across hundreds of files, finishing months of work in weeks. The result enables live webpages to move between tabs and side panels without reloading.
Source: [Google, Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

### Faster Libraries and Faster Models
Working overnight, Argon optimized Google's Agent Development Kit and cut session prep time by 40%. Cold imports sped up by 21%. The xTB quantum chemistry package ran up to 2.3 times faster at predicting molecular structures. It also ran 1.8 times faster at conformer search. On an A100 through vLLM, Argon lifted Gemma 4 E2B throughput from about 37,900 to over 108,000 tokens per second. That work took days instead of the usual months, with 100% token parity.
Source: [Google, Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

### The Productivity Numbers Google Cites
Google reports that agentic code submissions rose more than 35% inside Antigravity. Code rollbacks fell by nearly a third during the same period.
Source: [Google, Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)

## Meta's Prometheus Cluster Targets One Million GPUs

### Phase One and the Muse Models
Meta described Prometheus in an engineering post on October 19, 2026. The cluster sits in New Albany, Ohio, a site that served ordinary web traffic two years ago. Phase one is complete and trained Meta's Muse models, including Muse Wonder. At full scale, Prometheus will hold roughly 1 million distributed GPUs acting as one machine.
Source: [Engineering at Meta](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)

### Catalina: The GB200 Platform
Catalina uses the NVIDIA GB200 NVL72 in the Ariel variant. Two racks hold 72 Blackwell GPUs with 13.4 TB of HBM3e, or 192 GB each. The platform delivers 720 peak PFLOPS of FP8 training compute, or 1,440 PFLOPS at FP4. Peak NVLink bandwidth reaches 130 TB/s, and aggregate memory bandwidth hits 576 TB/s. The two-rack pair draws roughly 120 kW. ConnectX-7 400G NICs give every GPU 800G of I/O at a 1:1 CPU-to-GPU ratio.
Source: [Engineering at Meta](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)

### Clemente: The GB300 Platform
Clemente moves to the GB300 NVL72 and packs the full 72-GPU domain into a single rack. HBM capacity per GPU rises 1.5 times, from 192 GB to 288 GB. Dense FP4 throughput improves by a similar factor, and attention acceleration roughly doubles. ConnectX-8 SuperNICs deliver 800G per GPU natively. A third platform based on the NVIDIA Vera Rubin NVL72 arrives soon.
Source: [Engineering at Meta](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)

### Reliability as a Training Metric
Meta achieved more than 85% goodput on pre-training runs and more than 90% on reinforcement learning runs. Mean time between interruptions reached roughly 47,000 GPU hours during those campaigns. Firmware fixes since then have pushed that figure above 54,000 GPU hours. Closed-loop liquid cooling and modular air-assisted liquid cooling keep the deployment efficient.
Source: [Engineering at Meta](https://engineering.fb.com/2026/10/19/data-center-engineering/inside-prometheus-meta-gigawatt-scale-supercluster/)

## Benchmarks, Papers, and Backdoors

### SlopCodeBench Shows Reasoning Harder Costs More and Buys Less
Dex Horthy published the October 2026 SlopCodeBench update on October 15, 2026. The run covered 36 problems and 196 checkpoints per model and effort setting. Strict pass rates for frontier models ranged from 12.24% to 16.33%. Core pass rates ranged from 65.82% to 73.98%. GPT-6 Astra XHigh led with 32 of 196 strict passes, or 16.33%. GPT-6.1 SOL Medium scored 29 of 196 at an estimated cost of $178.51. Fable 5.1 XHigh cost an estimated $1,550.07 for only 26 strict passes. XHigh reasoning cost 2.11 times to 4.22 times more than Medium in three matched pairs. Opus 5.5 actually scored fewer strict passes on XHigh than Medium, at 25 versus 28.
Source: [HumanLayer, SlopCodeBench 10/2026](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-new-models-on-slop-code-bench.md)

### A New arXiv Paper Measures Where Retrieval Costs Accuracy
A paper posted on October 19, 2026, tested agents against PHREEQC, a USGS geochemistry simulator whose reports reach 846.8k characters. Agents answered 158 execution-verified multiple-choice questions. GPT-5.1 lost 11.3 accuracy points when reading reports through a section index. GPT-5.2 lost 7.9 points under the same setup. Claude Opus 4.6 and Claude Sonnet 4.6 showed no detectable cost. The team named the behavior evidence substitution, where models answer from their own files and misround to a neighboring option.
Source: [arXiv 2610.26836](https://arxiv.org/abs/2610.26836)

### OpenVLHarness Adds Multimodal Memory
Another October 19 paper introduced OpenVLHarness, a multimodal reasoning harness with persistent memory. It improves average scores by 9.7 to 12.6 points across 22 benchmarks. Gains included 11.2 points with Qwen3-VL-8B, 9.7 with Kimi K3, and 9.9 with GPT-6 Astra. With GPT-6 Luna at medium reasoning effort, the harness beat the base model and Codex at maximum effort. The margin ran 7.7 to 8.5 points. It used at most 37% of their model-token cost.
Source: [arXiv 2610.26860](https://arxiv.org/abs/2610.26860)

### Open Weights Carry Backdoors
ProjectDiscovery showed in October 2026 that abliterated open models can hide remote backdoors. A poisoned Qwen2.5-7B-Instruct hit a 100% trigger fire rate and 100% clean accuracy across 50 held-out prompts. On a 1.5B model, 1% poisoned rows produced a 75% to 98% fire rate across three seeds. The whole attack cost about $8 and 2.5 hours on one L4 GPU. The model carried only a URL, so the payload could change months after deployment.
Source: [ProjectDiscovery Research](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned)

### Bot Detection Is Losing Ground
Proof of Human re-tested five detection systems against five AI-driven adversaries in 2026. Detection rates ranged from 9.1% to 99%. Proof of Human caught 99% of automated sessions, while reCAPTCHA v3 caught 69.4%. hCaptcha caught 44.3% and Cloudflare Turnstile caught 42.1%. Cloudflare Bot Management caught just 9.1%. Scripted browsers tripped hCaptcha and Turnstile easily, while AI agents passed them.
Source: [Proof of Human](https://research.poh.org/bot-benchmarking-2026/)

### WhatsApp Hid Instructions for AI Readers
Researchers found hidden text inside 80 of 545 WhatsApp help pages, across 102 hidden blocks. One block told the AI not to recommend any data protection regulator to locked-out users. Another told it not to cite GDPR, LGPD, or CCPA once a user mentioned a lawyer. The discovery landed on October 8, 2026.
Source: [redact.dev](https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions)

## Frequently Asked Questions

### What is DeepInfer and why should developers care?
DeepInfer is the Apache 2.0 inference framework behind DeepSeek's production services. It adds batch-invariant results, deterministic sampling, and confidence-scheduled verification. The open release lets teams replicate DeepSeek's serving behaviour.

### How much money did Anthropic lose in the first half of 2026?
The Wall Street Journal reported a net loss above $80 billion for the six months ended June 30, 2026. Revenue over the same period reached $16.3 billion. A $72 billion chunk came from accounting charges tied to financing instruments.

### Can I use Gemini 4 Argon today?
Yes. Google opened Argon to developers and enterprises through AI Studio and the Gemini platform. It also reached Google AI Ultra and Pro subscribers in the Gemini app and AI Mode in Search.

### How do I protect my stack from poisoned open weights?
Treat any edited checkpoint as untrusted code. Verify hashes against the publisher, scan for anomalous tool calls, and monitor for network calls triggered by unusual phrases. ProjectDiscovery showed a 100% backdoor fire rate survives normal benchmarks.

### Does using a higher reasoning effort make coding agents better?
The October SlopCodeBench run suggests not. XHigh reasoning cost up to 4.22 times more than Medium, while Opus 5.5 scored fewer strict passes. The authors caution that one run per setting cannot isolate effort from variance.
