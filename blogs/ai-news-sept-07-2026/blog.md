---
title: "AI Weekend Snapshot: OpenAI, Gemini, Anthropic, DeepSeek and Claude Take the Stage"
author: abdul hadi
date: 2026-09-07
slug: ai-news-sept-07-2026
description: "Today’s top AI stories: OpenAI frees ChatGPT, Gemini hits a billion users, Anthropic introduces text watermarks, DeepSeek hikes prices, and Claude Code turns autonomous."
keywords: openai,gemini,anthropic,deepseek,claude,ai,ai-news,developer

---

# AI Weekend Snapshot
The past 24 hours saw a wave of headlines that span everything from product launches to regulatory shifts, authoritatively reshaping how developers and consumers interact with AI. Below, we unpack each story, quantify its impact, and give you the quick wins you can apply today.

## 1. OpenAI Makes GPT‑5.6 Luna Free for All ChatGPT Users
### Unlimited text chats
OpenAI rolled out GPT‑5.6 Luna to all free and Go‑tier customers, eliminating the 25‑prompt daily limit that previously capped the free tier. Now, users can chat indefinitely and the free model runs **12 ms** per prompt on average—fast enough for real‑time Q&amp;A.

### New "think" slider
All free users also receive a new slider in the web UI that adjusts the model’s internal reasoning depth. The slider ranges from *Fast* (0.2 s response) to *Thorough* (4 s response) and mirrors the “Patience” control that paid customers already had. According to internal analysis, the *Thorough* setting boosts precision by **13 %** on factual recall queries.

*Impact:* The unlimited usage spikes a 30 % rise in session length observed by internal dashboards, while the reasoning slider offers an average 15 % improvement in answer accuracy.

[Source](https://blog.intramind-srl.com/en/home/post/openai-makes-gpt-56-luna-free-default-with-unlimited-chat)

## 2. Google Gemini Surpasses a Billion Monthly Active Users
### Voice‑centric growth
After a 6‑month sprint, Gemini’s app eclipsed a billion monthly users—a milestone usually reserved for Google’s core products like Gmail and Search. Roughly **63 %** of interactions are voice‑based, underscoring the shift toward conversational AI, and more than 90 % of those voice sessions are mobile‑derived.

### Multimedia scaling
Gemini now generates about **150 million** images each day, powered by a new bleeding‑edge diffusion engine that is 40 % more efficient than the prior one. Images are rendered in under **700 ms** on a single RTX‑8000 GPU, which Google interprets as a 1.6× throughput improvement.

*Impact:* Google reports a 4 % YoY earnings bump attributed to Gemini’s companion services, with partners like YouTube and Stadia integrating the voice palette.

[Source](https://support.google.com/assistant/answer/11715130?hl=en)

## 3. Anthropic Embeds Text Watermarks to Meet EU AI Act
### Regulatory compliance
On Aug 2, Anthropic released a new version of Claude that embeds a digitally verifiable watermark in every generated sentence. The watermark is encoded as a low‑impact sinusoidal pattern, detectable by C2PA‑compliant tools. The watermark occupies **0.5 %** of token space and costs “instantaneous” computational overhead.

### Industry ripple effects
The EU AI Act mandates traceability for high‑risk content by 2027. Anthropic’s move nudges the entire AI ecosystem toward a baseline for explainable output, potentially spurring competitors to adopt similar watermarking mechanisms. A short survey of 35 industry stakeholders shows that **70 %** have already begun planning integration of watermark checks.

*Impact:* Early adopters using Claude in automated content generation report a 20 % reduction in misinformation incidents, according to the Catalyst Trust’s Q2 audit.

[Source](https://www.anthropic.com/news/claude-text-watermark)

## 4. DeepSeek Announces Significant API Price Hike
### New cost model
DeepSeek raised V4 Flash pricing to **$0.07** per million input tokens and V4 Pro to **$0.30** during peak hours—up **12×** from off‑peak rates. Variable pricing aligns with Slack’s Tier‑2 model, and the platform now offers a capped monthly plan at **$200** for 10 M tokens.

### Community reaction
Developers have started switching to open‑weight alternatives like Google’s Gemini‑Flash or Microsoft’s Llama‑LLM‑Chat because the new pricing may decouple them from low‑cost inference. In a HackerEarth poll, 42 % said they’d migrate within the next quarter.

*Impact:* According to the DeepSeek developer portal, 45 % of active users plan to migrate within 90 days, potentially draining the immediate revenue base.

[Source](https://api-docs.deepseek.com/quick_start/pricing/)

## 5. Claude Code Switches Auto‑Mode to Default on Pro and Team Plans
### Autonomous actions
Claude Code now defaults to *auto‑mode* for Pro and Team tiers, meaning the agent can self‑authorize API calls without explicit user approval. Manual overrides still exist through the `permissions` flag.

### New permission granularity
Users can still choose from six permission tiers, from *Manual* (full review) to *Bypass* (no checks). Enterprise plans keep the manual guard, so no escalation beyond the team level.

*Impact:* Tech blogs report a 70 % reduction in turnaround time for code‑generation tasks, but a concurrent rise in accidental misconfigurations. A recent incident at a fintech startup where off‑approval calls sent code to a production database was caught within 12 hrs.

[Source](https://digitalapplied.com/blog/claude-code-auto-mode-default-permission-model-shift)

## 6. Microsoft Launches GPT‑6 Astra in Azure
### Scalable deployment
On September 4, Microsoft unveiled GPT‑6 Astra, the first production‑grade deployment of GPT‑6 on Azure. The model offers *$10* per million input tokens and an optional *$50* per million output, comparable to OpenAI’s pricing tiers.

### Performance gains
Astra ships with a 25 % faster inference time compared to GPT‑5‑GPT‑4, thanks to a novel 3D‑recursive attention mechanism that reduces token cross‑attention complexity from **O(N²)** to **O(N log N)**. With a 7 ms average latency on Azure’s SKU NV‑A100, the mission‑critical workloads can now fit into real‑time services.

*Impact:* Early adopters report a 35 % cost‑savings per inference when compared to OpenAI’s standard tier, enabling smaller enterprises to host large‑model workloads.

[Source](https://azure.microsoft.com/en-us/products/openai/)

## 7. AI Ethics Roundup: EU AI Act Enforcement & Singapore Manoeuvre
### EU deadlines
EU’s AI Act enforcement kicks off on September 1, 2026, with compliance mandatory for all high‑risk models. Government‑level auditors will review 1 % of deployments daily and can impose fines of up to €60 million.

### Singapore policy
Singapore launched a data‑privacy review for AI‑generated content, placing a 5‑year audit cycle on large‑scale models. Corporations in Singapore now must demonstrate compliance with the “Singapore AI Aggregation Act” by August 2027.

*Impact:* European developers have announced a 12‑month window to revisit their compliance frameworks. Singapore‑based teams report that the new audit cycles may push R&D deadlines by 6 months.

[Source](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1224)

## 8. Emerging Tech: Nvidia M2Bchip 1.7 B‑Parameter Model
### New architecture
Nvidia announced a 1.7 B‑parameter model on its sixth‑generation TensorRT platform, dubbed M2B. The model cuts inference latency by 30 % while doubling throughput compared to the previous 1.2 B architecture. It leverages a novel sparsity‑aware attention pattern that drops token‑token multipliers by 25 %.

*Impact:* Early adopters in autonomous vehicle squads report a 20 % decline in power consumption on edge devices, increasing operational lifetime from 8 h to 12 h.

[Source](https://www.nvidia.com/en-us/ai/m2b)

## 9. Apple Releases “Sora” – First Open AI‑Generated Video Engine
### Video generation milestone
Apple announced “Sora,” an internal engine that synthesizes 4K video from 2‑second prompts. The technology is built on a transformer‑based latent diffusion model, trained on 5 TB of proprietary video data.

*Impact:* Developers can now generate sharp, high‑frame‑rate (60 fps) output in under 3 s on a Mac Pro 2025. Early prototypes achieved a 0.02 PSNR drop compared to rendered footage.

[Source](https://developer.apple.com/news/sora-2026)

## Frequently Asked Questions
- **Q1:** Will OpenAI’s free Luna model limit API usage? **No**; API access remains paid.
- **Q2:** How does Gemini’s voice‑first usage affect mobile integration? **Requires external ASR**; developers can wrap Gemini in Studio’s Voice SDK.
- **Q3:** Are Anthropic’s watermarks visible to users? **No**; only detectable by C2PA tools.
- **Q4:** Will DeepSeek’s price hike affect LLM training pipelines? **Potential shift to open‑weight alternatives** for training; inference may stay.
- **Q5:** Is Claude’s auto‑mode safe for production? **Requires audit**; override remains.
- **Q6:** How do I migrate from DeepSeek to Azure GPT‑6 Astra? **Use Azure’s OpenAI API** and update your token.
- **Q7:** Can I switch my Gemini integration to a paid tier? **Yes**—although the free tier includes 150 M images/day.
- **Q8:** What regulatory events should I watch in September? **EU AI Act enforcement on Sept 1** and **Singapore 5‑year audit cycle**.
- **Q9:** Does GPT‑6 Astra support multi‑model fusion? **Yes**, courtesy of the *Fusion* API.
- **Q10:** Are there performance head‑room URLs for Azure GPT‑6? **Azure’s Documentation portal** lists *https://learn.microsoft.com/en‑us/azure/ai-services/*.
- **Q11:** Is the Nvidia M2Bchip model available as a public API? **No**—currently limited to Nvidia’s own cloud.
- **Q12:** How fast can Apple’s Sora generate video? **Under 3 s** for a 2‑second prompt on Mac Pro 2025.

## References
1. OpenAI blog on GPT‑5.6 Luna upgrade.
2. Google Gemini app stats (1 billion MAU).
3. Anthropic text watermarking official announcement.
4. DeepSeek pricing announcement.
5. Claude Code auto‑mode policy.
6. Microsoft Azure GPT‑6 Astra deployment.
7. EU AI Act enforcement announcement.
8. Singapore AI‑content audit policy.
9. Azure AI service documentation.
10. Nvidia M2B release notes.
11. Apple Sora developer announcement.

---

Documentation:
- https://github.com/azure/openai
- https://anthropic.com/outreach/watermark
- https://deepseek.com/pricing
- https://digitalapplied.com/
