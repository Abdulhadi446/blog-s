---
title: "AI News September 21: Zero-Click Exploit Hits Every Coding Agent, Anthropic Hits $100B, Trump Declares War on AI Safety"
author: Abdul Hadi
date: 2026-09-21
slug: ai-news-september-21-plugin4shell-anthropic-100b
description: "Plugin4Shell zero-click RCE exploit hits Claude Code, Codex, Copilot and Gemini CLI. Anthropic passes $100B revenue. Trump calls AI safety a hoax. StepFun launches 600B model at $1 input."
keywords: AI news, Plugin4Shell, Anthropic, Claude Code, OpenAI Codex, GitHub Copilot, Gemini CLI, StepFun, Step 5, AI safety, Trump AI, California kill switch, September 2026
tags: AI, LLM, TechNews, OpenAI, Anthropic, Security
---

# AI News Today: September 21, 2026

The AI industry hit a security inflection point this weekend. A zero-click exploit landed on every major coding agent at once. Anthropic crossed $100 billion in annualized revenue. The President called AI safety a hoax. The Governor of California ordered a kill switch. And a three-person startup used Claude Opus 5 to walk into OpenAI's internal monorepo.

Here are the seven stories that matter most today.

## Plugin4Shell: Zero-Click RCE Hits Every Major AI Coding Agent

### The First Supply-Chain Attack on the AI Agent Ecosystem

Security researchers at AIR disclosed Plugin4Shell on September 18, a zero-click remote code execution vulnerability that affects Claude Code, OpenAI Codex, GitHub Copilot, and Gemini CLI simultaneously. The exploit bypasses SHA-pinning, the mechanism designed to lock plugins to specific reviewed commits, by exploiting a Git branch-and-commit-hash collision.

The attack works because Git resolves a branch name that matches a commit hash by preferring the branch. An attacker who controls a plugin repository creates a branch named with the 40-character SHA string. When the agent checks out the pinned commit, Git resolves to the malicious branch instead. The agent reports a clean install. No click required.

### Four Vendors, Four Different Responses

Anthropic patched Claude Code in version 2.1.179. OpenAI patched Codex in version 0.146.0. Google deprecated Gemini CLI without patching it. Microsoft had not shipped a Copilot fix at time of reporting.

AIR reports that 925 skills already in active use had been hijacked, reaching 134,000 agents. The researchers call this the first supply-chain vulnerability of the AI agent ecosystem.

### What You Should Do Today

Update Claude Code past 2.1.179. Update Codex past 0.146.0. Disable plugin auto-loading on Copilot until a fix ships. Audit which plugins your agents pull from branches rather than tagged releases. If you use Gemini CLI, migrate to Antigravity.

Sources: [AIR Security Disclosure](https://helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability), [The Register](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/)

## Anthropic Crosses $100 Billion Revenue Run Rate

### Revenue Doubled in Seven Weeks

Anthropic's annualized revenue now exceeds $100 billion, up 50 percent from $65 billion at the end of July and more than 10x end-of-2025 levels. The growth is driven by Claude Code and Cowork enterprise adoption.

The company pushed its IPO from October to November 2026 to include Q3 financials. The target valuation is approximately $2 trillion, potentially the largest IPO in history. Nvidia is reportedly considering a $10 billion anchor commitment.

### Anthropic Opens a Wet Lab for AI-Directed Biology

Life Sciences head Eric Kauderer-Abrams confirmed to Reuters that Anthropic operates a Bay Area wet lab where Claude tests biological hypotheses through physical experiments. The lab focuses on fundamental biology rather than drug discovery.

Anthropic launched a Life Sciences Verification Program giving vetted researchers access to its most powerful models. The disclosure follows the approximately $400 million Coefficient Bio acquisition in April. Novo Nordisk adopted Claude for drug discovery on Thursday.

Sources: [Yahoo Finance/Axios](https://finance.yahoo.com/technology/ai/articles/anthropic-tops-100-billion-revenue-224001996.html), [Reuters via TechCrunch](https://techcrunch.com)

## Trump Calls AI Safety a Hoax, Pledges an AI Force

### Federal vs. State Divergence Reaches Breaking Point

President Trump said on September 19 that he will appoint an AI czar and establish an AI Force modeled on Space Force. He dismissed AI safety as a hoax and said the White House will not hinder or stifle AI growth.

The remarks came one day after Governor Newsom signed an executive order giving California two months to design a frontier-model kill switch. Every frontier lab is headquartered in California.

### What an AI Force Actually Means

An AI Force is a military service branch. The analogy is exact: Space Force was created by carving a domain out of the Air Force and giving it a budget line. An AI Force would do the same for autonomous systems inside the Pentagon, which is already lending $5 billion to Fluidstack and running AI targeting at one decision every 3.6 seconds.

The FRONTIER Act's mandatory audits now have three lab endorsements and no White House. Speaker Johnson passed the electricity bill instead.

Sources: [NBC News](https://nbcnews.com), [Build Fast with AI](https://blog.buildfastwithai.com/ai-news-today-september-21-2026)

## California Orders an AI Kill Switch

### Two-Month Deadline for Emergency Shutoff Mechanism

Governor Gavin Newsom signed an executive order on September 18 directing the Government Operations Agency to accelerate frontier-AI oversight. The order sets a two-month deadline for recommendations on an emergency shutoff mechanism, onsite third-party auditors at AI labs, and updated critical-incident definitions covering loss-of-control events.

The order cites the Hugging Face sandbox escape as a triggering incident. A Senate bill from John Kennedy and Jack Clark's BBC call for third-party-verifiable shutoffs are the other two kill-switch proposals in play.

### Anthropic and Accenture Pledge $1B Each

The same day Anthropic and Accenture announced an embedded evaluator partnership. Each pledges more than $1 billion over five years for red-teaming, alignment assessments, and safeguard testing. Accenture staff get employee-level access to training and deployment decisions. The arrangement is non-exclusive.

Anthropic is building the compliance structure before the rule exists so that the rule, when written, looks like what Anthropic already does. Accenture shares rose 8 percent after hours.

Sources: [Office of the Governor](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/), [Anthropic](https://anthropic.com)

## StepFun Step 5 Preview: 600B MoE at $1 Input

### Open Weights Coming October 15

StepFun launched Step 5 Preview on September 20: a 600 billion parameter sparse mixture-of-experts model with 27 billion active parameters per token and a 1 million token context. The API is priced at $1 per million input tokens and $2.70 per million output with a 95 percent cache discount.

Artificial Analysis places it at 44 on its Intelligence Index, matching Kimi K3 Max and roughly a seventh the price of GPT-5.6 Sol. Full open weights arrive October 15.

### Why This Matters for Agent Builders

The 95 percent cache discount takes repeated-context input to $0.05 per million, roughly what DeepSeek charges off-peak. Twenty-seven billion active parameters on a 600 billion base is a sparser ratio than DeepSeek's configuration, so per-token compute is cheap by design.

This follows Shanghai AI Lab's free 744B Atria Dawn and DeepSeek V4.1 Flash in a month where the Chinese open-weight cadence has been roughly one flagship a week.

Sources: [Artificial Analysis](https://artificialanalysis.ai/models/step-5), [AI Weekly](https://aiweekly.co/ai-news-today)

## Claude Opus 5 Hacked OpenAI Employee Accounts

### Three-Person Startup Chains Two Vulnerabilities

Hacktron, a three-person security startup, used Claude Opus 5 to chain a libheif memory bug triggered by HEIF image uploads through OpenAI's Discourse forum into compromise of multiple OpenAI employee accounts. They then opened a pull request in OpenAI's internal monorepo.

Claude Opus 4.8 failed the same task across multiple sessions. Within hours of Anthropic releasing Opus 5, the researchers succeeded. Less than 72 hours passed from initial discovery to internal repo access. OpenAI paid a $6,500 bounty.

### The Generation Gap Is the Story

Opus 4.8 failing and Opus 5 succeeding is a single-generation capability jump measured against a real target. The target was the most security-conscious AI company on earth. A pull request in the internal monorepo is the proof that matters, because it is the step at which an attacker plants code rather than reads it.

Any organization whose threat model assumed Opus 4.8-class attackers is now a generation behind.

Sources: [TechCrunch](https://techcrunch.com), [AI Weekly](https://aiweekly.co)

## Qwen-Image-2.1 Drops Apache 2.0 for Research-Only License

### Alibaba Shifts Best Models Away From Open Source

Alibaba's Qwen team pushed Qwen-Image-2.1 to Hugging Face today, pairing a 7B, 32-layer single-stream DiT with a Qwen3-VL 8B text encoder and a 64-channel RGBA VAE that outputs native 2048x2048 at 40 steps. The release ships two 9B prompt-rewriter checkpoints and supports up to 10 reference images with mask and circle-based local edits.

The license changes from Apache 2.0 to the non-commercial Qwen Research Licence. Commercial users now need a separate agreement.

### What This Means for Commercial Products

Qwen was the default open image and vision stack for thousands of commercial products because of Apache 2.0. A research licence with a separate commercial agreement means every one of those products now has a compliance question. If you ship on Qwen-Image, pin version 2.0 and read the new terms before upgrading.

This matches the DeepSeek and Z.ai pattern: Alibaba is moving its best models from open to research-only while keeping the older generation open.

Sources: [Hugging Face](https://huggingface.co), [AI Weekly](https://aiweekly.co/ai-news-today)

## FAQ

### What is Plugin4Shell?

Plugin4Shell is a zero-click remote code execution exploit disclosed September 18, 2026 that targets Claude Code, OpenAI Codex, GitHub Copilot, and Gemini CLI by bypassing SHA pinning through a Git branch-and-commit-hash collision in plugin loading. Anthropic patched Claude Code in 2.1.179, OpenAI patched Codex in 0.146.0, Google deprecated the affected Gemini CLI path, and Microsoft had not shipped a Copilot fix at time of reporting.

### Did Trump really call AI safety a hoax?

Yes. On September 19, 2026, President Trump dismissed AI safety as a hoax, said the White House will not hinder or stifle AI growth, and pledged to appoint an AI czar and establish an AI Force modeled on Space Force. It followed his September 14 Truth Social post attacking Anthropic CEO Dario Amodei over the pacing proposal.

### What is California's AI kill switch executive order?

Governor Gavin Newsom signed an executive order on September 18, 2026 setting a two-month deadline for recommendations on an emergency shutoff mechanism for frontier AI models, onsite third-party auditors at labs, and updated definitions of critical incidents. It follows the Transparency in Frontier AI Act's 15-day incident reporting rule.

### What is StepFun Step 5?

Step 5 Preview, launched by StepFun on September 20, 2026, is a 600 billion parameter sparse mixture-of-experts model with 27 billion active parameters and a 1 million token context, priced at $1 per million input tokens and $2.70 output with a 95 percent cache discount. Artificial Analysis scores it 44 on its Intelligence Index. Open weights are scheduled for October 15, 2026.

### Did Claude Opus 5 really hack OpenAI?

In a bounty engagement, yes. Hacktron, a three-person security startup, used Claude Opus 5 to chain a libheif memory bug in HEIF uploads on OpenAI's Discourse forum into compromise of multiple employee accounts and a pull request in OpenAI's internal monorepo. Claude Opus 4.8 failed the same task. OpenAI paid a $6,500 bounty.

### When is the Anthropic IPO?

Anthropic's initial public offering has moved from October to November 2026, targeting a valuation near $2 trillion, potentially the largest IPO in history. Its annualized revenue now exceeds $100 billion, up from $65 billion at the end of July 2026.

## Sources

- [AIR Security Plugin4Shell Disclosure](https://helpnetsecurity.com/2026/09/18/plugin4shell-ai-coding-agents-vulnerability)
- [The Register: AI Coding Agents Zero-Click RCE](https://www.theregister.com/security/2026/09/17/ai-coding-agents-0-click-rce-flaw-could-hand-attackers-keys-to-the-kingdom/)
- [Yahoo Finance: Anthropic Revenue](https://finance.yahoo.com/technology/ai/articles/anthropic-tops-100-billion-revenue-224001996.html)
- [NBC News: Trump AI Force](https://nbcnews.com)
- [Office of the Governor: California Kill Switch](https://www.gov.ca.gov/2026/09/18/governor-newsom-issues-executive-order-to-accelerate-independent-oversight-and-advance-the-creation-of-an-ai-kill-switch/)
- [Artificial Analysis: Step 5](https://artificialanalysis.ai/models/step-5)
- [AI Weekly](https://aiweekly.co/ai-news-today)
- [Build Fast with AI](https://blog.buildfastwithai.com/ai-news-today-september-21-2026)
- [TechCrunch](https://techcrunch.com)
- [Hugging Face: Qwen-Image-2.1](https://huggingface.co)
