---
title: "AI Agents Conquer Minecraft and ML Engineering: October 19 Roundup"
author: Abdul Hadi
date: 2026-10-19
slug: ai-news-October-19-agentic-ai-updates
description: "Gemini 4 Argon agents beat Minecraft, MLExpert boosts ML engineering medal rates, and Anthropic launches Claude Haiku 5.5."
keywords: AI, LLM, Gemini, Anthropic, MLExpert, Minecraft, agents
tags: AI, LLM, TechNews, OpenAI
---

Today's AI news centers on autonomous agents and smarter, cheaper models. A team of Gemini 4 Argon agents defeated Minecraft's Ender Dragon without human help. Anthropic shipped Claude Haiku 5.5 for high-volume, cost-sensitive work.

## Gemini 4 Argon Agents Beat Minecraft

### The Minecraft Challenge
Four Gemini 4 Argon agents entered a sandboxed Minecraft survival world. Their goal was to defeat the Ender Dragon. Each agent controlled a player through the open-source Mineflayer library. The agents coordinated using in-game chat and shared memory. No human assigned roles or wrote game logic.
Source: [arXiv:2610.22319](https://arxiv.org/abs/2610.22319)

### The Numbers Behind the Win
The agent team wrote 2,783 programs during the run. They defeated the dragon in 27 hours and 14 minutes. Along the way, the agents died 605 times. The run started from a randomly generated world on Easy difficulty. This marks the first end-to-end autonomous completion of Minecraft by AI agents.
Source: [arXiv:2610.22319](https://arxiv.org/abs/2610.22319)

### Why It Matters
The agents kept a coherent plan across thousands of dependent steps for more than a day. They used only the standard Mineflayer library. No pre-scouted seeds or human-written game tools were involved. Long-horizon coding and multi-agent coordination matter for real-world software engineering.
Source: [arXiv:2610.22319](https://arxiv.org/abs/2610.22319)

## MLExpert Raises ML Engineering Medal Rate

### A 35B MoE Agent
Researchers introduced MLExpert, a 35-billion-parameter Mixture-of-Experts agentic model. It targets autonomous machine learning engineering. The team built the Kaggle-MLE Factory to create executable tasks. Hierarchical agentic supervised fine-tuning transfers coding skills to MLE tasks. Windowed Interaction RL treats multi-turn decisions as execution windows with shared rewards.
Source: [arXiv:2610.22344](https://arxiv.org/abs/2610.22344)

### Medal Rate Gains
On MLE-Bench Lite, MLExpert lifted the base model's average medal rate from 37.9% to 72.7%. This performance matches larger frontier models such as Kimi-K3 and GLM-5.3. The post-training method selects useful supervision from long experiment trajectories. Asynchronous collection supports policy updates before a trajectory ends.
Source: [arXiv:2610.22344](https://arxiv.org/abs/2610.22344)

### Generalization Beyond MLE
MLExpert also improved results on NatureBench Lite. It helped with agent scaffold optimization and algorithm optimization. The learned optimization capability generalizes to other tasks. This points toward AI-for-AI pathways and recursive self-improvement.
Source: [arXiv:2610.22344](https://arxiv.org/abs/2610.22344)

## Anthropic Launches Claude Haiku 5.5

### Fast, Cheap, Capable
Anthropic introduced Claude Haiku 5.5 on October 7, 2026. It is the fastest, cheapest, and most capable small model yet. The model targets high-volume, cost-sensitive work. Developers can deploy it for large-scale inference without high costs.
Source: [Anthropic Newsroom](https://www.anthropic.com/news)

### Enterprise Cost Focus
Haiku 5.5 serves teams that need many model calls at low latency. Small models reduce the cost per token. This helps production applications with tight budgets. Anthropic continues to expand its small-model lineup alongside Sonnet and Opus.
Source: [Anthropic Newsroom](https://www.anthropic.com/news)

## Claude Sonnet 5.5 and Opus 5.5 Roll Out

### Sonnet 5.5 Speed and Price
Claude Sonnet 5.5 launched on September 28, 2026. It runs 30% faster than Sonnet 5. It costs up to 30% less for most work. The upgrade improves throughput for everyday tasks.
Source: [Anthropic Newsroom](https://www.anthropic.com/news)

### Opus 5.5 Efficiency
Claude Opus 5.5 arrived on September 22, 2026. It performs at the level of Claude Fable 5.1 on most work. It costs 40% less to run than Opus 5. The model balances high capability with lower operating expense.
Source: [Anthropic Newsroom](https://www.anthropic.com/news)

## DeepSeek Adds Web Search API

### V4.1 Flash Update
DeepSeek updated V4.1 Flash to the V4.1-Flash-1017 version. Project development capability improved significantly. The model completes tasks at lower cost and higher speed. This strengthens DeepSeek's position in the open-weight model space.
Source: [DeepSeek](https://deepseek.com)

### Search and Fetch Pricing
DeepSeek added API support for web search and scraping. The search and fetch service costs $0.75 per 1,000 successful requests. Developers can now ground models in live web data. This enables research agents that browse and cite sources.
Source: [Hacker News](https://news.ycombinator.com/)

## FAQ

### What did the Gemini 4 Argon agents achieve?
They autonomously defeated Minecraft's Ender Dragon. The team wrote 2,783 programs and won in 27 hours and 14 minutes. The agents died 605 times during the run.

### How much did MLExpert improve the medal rate?
MLExpert raised the average MLE-Bench Lite medal rate from 37.9% to 72.7%. This matches larger models like Kimi-K3 and GLM-5.3.

### What is Claude Haiku 5.5?
It is Anthropic's fastest, cheapest, most capable small model. It launched on October 7, 2026, for high-volume, cost-sensitive work.

### How much does DeepSeek web search cost?
DeepSeek charges $0.75 per 1,000 successful search and fetch requests. The API launched alongside the V4.1-Flash-1017 update.

### When did Claude Sonnet 5.5 launch?
Sonnet 5.5 launched on September 28, 2026. It runs 30% faster and costs up to 30% less than Sonnet 5.

## Sources

- arXiv:2610.22319 — A team of Gemini 4 Argon agents beats Minecraft
- arXiv:2610.22344 — MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
- Anthropic Newsroom — Claude Haiku 5.5, Sonnet 5.5, Opus 5.5 announcements
- DeepSeek — V4.1-Flash-1017 and web search API
- Hacker News — DeepSeek search and fetch pricing
