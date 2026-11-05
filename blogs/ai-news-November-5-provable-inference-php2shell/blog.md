---
title: "Anthropic Proves LLM Outputs, OpenAI Ships Images 2.6, Kimi Drops 2.8T Weights"
meta_title: "AI News Nov 5 2026: Provable AI, Images 2.6, Kimi 3.1"
author: Abdul Hadi
date: 2026-11-05
updated: 2026-11-05
slug: ai-news-November-5-provable-inference-php2shell
image_alt: "Dark infographic titled November 5 2026 AI news with stat cards: 110 tokens per second for Anthropic FlashProve, animated GIF and SVG output for OpenAI Images 2.6, 2.8 trillion parameters for Kimi K3.1 Pro, and PHP2Shell risk across WordPress and Drupal sites"
description: "Anthropic makes LLM answers cryptographically verifiable, OpenAI ships Images 2.6, Kimi open-weights a 2.8T MoE, and AI turns old PHP crashes into root shells."
keywords: AI news November 5 2026, Anthropic FlashProve, OpenAI Images 2.6, Pierre Computer Company, Kimi K3.1 Pro, Ricursive Ripple 65B, PHP2Shell
tags: AI, LLM, TechNews, Security
---

Wednesday's AI news moved the proof layer, the image layer, and the weight layer at once. Anthropic published a system that cryptographically proves which model answered you. OpenAI shipped Images 2.6 and bought a git company. Kimi and Ricursive released new open weights. AI also turned a decade-old PHP crash into a root shell.

## The Short Version

### Six Numbers From Today
- Anthropic's FlashProve proves Llama 4 Maverick at 110 tokens per second on one H100, with 19 MB proofs and 6.5 MB commitments.
- OpenAI Images 2.6 is 50 percent faster, can emit native animated GIFs and SVG files, and prices a low-quality 1024x1024 image at $0.025.
- OpenAI agreed to acquire Pierre Computer Company, whose Code.Storage hosts git for agentic products such as Lovable and Bolt.
- Kimi K3.1 Pro ships with 2.8 trillion total parameters, 104 billion active, and a one-million-token context window.
- Ricursive's Ripple 65B preview is a dense 65-billion-parameter open-weight model aimed at agentic coding.
- The AI-assisted PHP2Shell audit turned a 2024 out-of-memory crash into remote code execution across WordPress and Drupal sites.

## Anthropic Makes LLM Outputs Cryptographically Verifiable

### The 110-Token-Per-Second Claim
Anthropic published FlashProve on November 2. The system uses zkSNARKs to prove that a specific committed model produced an answer. It works on Llama 4 Maverick, a 400-billion-parameter mixture-of-experts model, in 4-bit weight form.

The prover runs on a single H100. It reaches 110 tokens per second, with a proof of 18.78 MB per 1,024-token window. Each proof takes 17 seconds to check on a 24-thread CPU. The offline commitment phase takes 39 minutes and covers about 16 million requests.

Prior open-source provable-inference systems ran thousands of times slower. FlashProve's speed comes from zkSNARK machinery adapted for mixture-of-experts models. The prover's work scales with the experts that actually run, not all 400 billion parameters.

### What a Proof Buys You
The proof binds a response to a committed set of weights. A verifier learns nothing about the weights and needs no GPU. Four use cases anchor the post: pacing, tamper detection, text provenance, and model approval.

Pacing asks a provider to show hardware really served inference. Tamper detection catches a substituted or hijacked model. Text provenance checks that expensive or sensitive model calls happened as claimed. Model approval checks that only approved models were served.

This answers a problem our [November 4 roundup](/blog/ai-news-November-4-postman-consent-ai-debt) raised about trust in tool chains. Every integration you add around a model now has something to verify against. Anthropic met a public inference-verification goal from its Frontier Safety Roadmap and released code, Lean proofs, and a technical report under Apache 2.0.

### What It Does Not Prove
The proof covers an integer version of the model under greedy decoding. A floating-point or sampling implementation can differ at some position. It also stops at 1,024 context tokens and does not hide the model architecture.

Those limits matter for production. But they do not remove the progress. FlashProve moves provable inference from a science demonstration into something a single GPU can run.

### Sources
- [Anthropic: Progress on provable inference for large language models](https://www.anthropic.com/research/provable-inference)
- [FlashProve technical report](https://www.anthropic.com/document/flashprove-technical-report)
- [FlashProve code on GitHub](https://github.com/anthropics/FlashProve)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50368626)

## OpenAI Ships Images 2.6 With Native GIFs and SVG

### Native Animated GIF Output
OpenAI released Images 2.6 globally in ChatGPT and Codex across all tiers. The model now natively generates animated GIF files instead of a single frame. Early testers found frame consistency uneven, but the feature works at all.

GPT Image 2.6 also emits SVG files. The API creates a raster reference image and converts it to vector XML. That path is useful for icons and logos that need scaling.

### Faster, But Not Universally Cheaper
OpenAI says generation is about 50 percent faster. The per-token price matches Image 2.5, but token counts rose at low and medium quality. A 1024x1024 low-quality image now costs about $0.025 at 823 tokens, up from about $0.006 at 196 tokens. Medium quality costs about $0.044.

High-quality settings keep their previous token counts. So teams should benchmark their own prompt mix. Speed gains and SVG support may justify the higher low-quality cost for UI work.

### Community Reaction
Commenters report strong prompt adherence, especially on conditional grids and counting tasks. Others found artifacting in animated frames and lower fidelity than Image 2.5 in some comparisons. Early API users already rolled some workflows back to Image 2.5.

Codex itself still calls gpt-image-2, so developer tooling lags the web app. Watch for an update before standardizing on 2.6.

### Sources
- [Introducing Images 2.6](https://openai.com/index/introducing-images-2-6/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50372945)

## OpenAI Buys Pierre to Own Git at Agent Scale

### What Pierre Built
OpenAI agreed to acquire Pierre Computer Company. Pierre built git infrastructure for agent-scale workloads. Its products include Code.Storage, a diffs library, and a file-tree viewer. Customers listed on its site include Lovable, Poke, Anything, Bolt, Amp, and Parahelp.

Pierre was founded by Jacob Thornton and Mark Otto, original Bootstrap contributors. Terms were not disclosed. The deal follows OpenAI's earlier post on scaling git internally.

### Why a Model Lab Wants Git Hosting
Agentic coding products generate many repositories and artifacts. GitHub already strains under that traffic. Owning git storage gives OpenAI control over the surface where agents write code.

That mirrors Anthropic's separate work on redesigning source control. The infrastructure under agents is becoming a competitive moat, not a commodity. Our [October 27 coverage](/blog/ai-news-October-27-security-and-bubbles) flagged rising concern about concentration in the developer stack.

### What Happens to Pierre's Open Source
Pierre extracted high-quality open-source libraries from its enterprise service. Developers in the thread worry those updates will slow after the acquisition. That is a fair risk, but it is not yet confirmed.

### Sources
- [OpenAI: OpenAI to acquire Pierre Computer Company](https://openai.com/index/openai-to-acquire-pierre/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50366863)
- [Pierre Computer Company](https://pierre.computer/)

## Kimi K3.1 Pro Lands as a 2.8T Open-Weight MoE

### The Specs That Matter
Moonshot AI released Kimi K3.1 Pro open weights on Hugging Face. It is a 2.8-trillion-parameter mixture-of-experts model with 104 billion active parameters. It has 896 experts and selects 16 per token, plus two shared experts. The context window is one million tokens.

It is natively multimodal through a 401-million-parameter MoonViT-V2 vision encoder. Weights use MXFP4 with MXFP8 activations from quantization-aware training. Deployment recipes exist for vLLM, SGLang, and TokenSpeed. The API is OpenAI and Anthropic compatible.

### Kimi's Benchmark Position
On Terminal-Bench 4.0, Kimi scored 65.7 against 66.4 for Claude Opus 5.5. On HLE-Full it scored 51.1 against 59.8 for Opus 5.5. On DeepSWE v1.1 it scored 75.5. On GDPval-AA v2.1 it reached 1846 Elo against 1866 for Opus 5.5.

Those gaps are small for an open model. The release shows Chinese labs remain competitive on agentic coding even while US export controls tighten. The license is custom, so read it before redistributing.

### What Developers Get
They get a frontier-scale open model with long context and a practical serving path. Memory and compute requirements are still large for 104 billion active parameters. But the recipe availability shortens the gap between download and serving.

### Sources
- [Kimi K3.1 Pro on Hugging Face](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- [Kimi K3.1 Pro technical blog](https://www.kimi.ai/blog/kimi-k3-1-pro)

## Ricursive Ships Ripple-65B as a US Open-Weight Coder

### The 65-Billion-Parameter Preview
Ricursive published Ripple-65B Preview, a dense 65-billion-parameter open-weight model. The company calls it the top US open-weight model for agentic coding. The preview scores 80.5 on Terminal-Bench 2.1 according to community readers.

A dense 65-billion model fits on 96 GB of memory at lower precision. That is within reach of workstation and mini-cluster users. It competes for the niche between Qwen's small models and trillion-parameter frontier systems.

### The HN Skepticism
Commenters pointed out that the announcement omits direct comparisons to Qwen 3.8 and other leaders. Terminal-Bench 2.1 is an older metric. Several noted that 80.5 barely beats the next US contender by 0.42 points.

Those criticisms are valid as methodology complaints. They do not invalidate the release. A new US lab with open weights and a fast follow-up is still useful.

### What to Watch
Watch whether a smaller dense variant or a quantized build follows. That would move the model from benchmark news to everyday local hardware. Also watch whether the benchmark sheet gets a direct Qwen comparison.

### Sources
- [Ricursive: Ripple-65B Preview](https://www.ricursive.com/ripple)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50369925)

## AI Turns a 2024 PHP Bug Into a Root Shell

### How an Out-of-Memory Error Became RCE
IEEE Spectrum reported on PHP2Shell. The bug started as a 2024 out-of-memory error in PHP. Researchers at Calif, with an audit sponsored by OpenAI, used AI tools to turn it into remote code execution in two weeks.

The exploit affected sites running WordPress, Drupal, and many other PHP stacks. That list includes NASA, Wikipedia, and the White House. The PHP Foundation released a patch before mass exploitation.

### Why the Fix Took Two Months
A team of four engineers spent two months building the patch. The asymmetry between finding and fixing bugs drove that timeline. AI helps attackers find precise memory layouts faster than human reasoning allows.

Suman Jana of Columbia University noted that fixing still requires closing every path and preserving behavior. Matthew Green of Johns Hopkins warned that funding will follow only after a worse incident.

### Formal Verification as the Counterweight
Jana also pointed to formal verification tooling from Anthropic released on October 22. The idea is simple. An LLM writes a patch, another LLM writes a proof, and a formal checker validates it. Only the checker must be trusted.

That ties today's Anthropic item to today's PHP item. Provable inference and verified patches share the same thesis. Put proofs around the risky parts and let machines do the painful reasoning.

### Sources
- [IEEE Spectrum: The PHP2Shell Vulnerability Heralds Cybersecurity Hell](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)
- [The PHP Foundation security release](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/)
- [Calif: php2shell](https://calif.io/php2shell/)

## Frequently Asked Questions

### What Is Provable Inference?
Provable inference is a cryptographic proof that a specific model produced a response. It needs no model weights from the verifier and runs on a CPU. FlashProve implements it for a 400-billion-parameter mixture-of-experts model at 110 tokens per second.

### Is OpenAI Images 2.6 Cheaper Than 2.5?
Not at low quality. Token counts rose from 196 to 823 for a low-quality 1024x1024 image. Speed improved, SVG export is new, and animated GIF output works natively. Benchmark your own prompts before switching.

### What Is Kimi K3.1 Pro?
It is Moonshot AI's 2.8-trillion-parameter open-weight mixture-of-experts model. It activates 104 billion parameters per token and supports a one-million-token context. Deployment recipes cover vLLM, SGLang, and TokenSpeed.

### Why Did OpenAI Buy Pierre?
OpenAI needs git infrastructure that scales with agent traffic. Pierre's Code.Storage already hosts repositories for agent-first products. The purchase also brings Thornton and Otto, who built Bootstrap.

### What Is PHP2Shell?
PHP2Shell is a critical remote-code-execution vulnerability built on an old PHP out-of-memory bug. AI-assisted analysis turned a benign crash into a shell. WordPress, Drupal, and many other PHP stacks were exposed until patched.

## The Bottom Line

### Verification Becomes the Feature
Pierre, Kimi, FlashProve, and Images 2.6 all point one way. The value is shifting from the model to the guarantees around it. Provable inference, verified patches, and owned git infrastructure put boundaries around what agents can do and claim.

### The Legacy Stack Is Now the Target
PHP2Shell shows the other side. AI lowers the cost of finding flaws in 40 years of accumulated code. That raises the return on verification and on patch discipline. Update your software when the update lands.

### What to Watch Next
Watch whether FlashProve inspires a standard verifier interface for model providers. Watch whether Images 2.6's SVG output earns its higher low-quality token cost. Watch Kimi's adoption in local serving recipes. And watch whether anyone adopts formal verification for security patches before the next zero-day.

Our [November 3 roundup](/blog/ai-news-November-3-weight-space-llmjack) noted weight-space programming. Today's FlashProve makes that direction practical for auditors, not just researchers.
