---
title: "A Model That Rewrites Weights by Hand, and Stolen Keys That Cost $1 Million"
meta_title: "AI News: Models Edit Weights, Stolen Keys Cost $1M"
author: Abdul Hadi
date: 2026-11-03
updated: 2026-11-03
slug: ai-news-November-3-weight-space-llmjack
image_alt: "Black slide titled How large are they? showing a transformer network diagram and parameter counts from BERT Large at 345M to GPT-4 at 1.4 trillion"
description: "GPT-6 Astra edits neural network weights without training, Anthropic's IPO filing warns of RSI, and stolen API keys ring up $1 million bills."
keywords: AI news November 3 2026, weight-space programming, GPT-6 Astra, Anthropic S-1, LLMJacking, China AI export controls, agentic backdoors, DoorDash AI agents
tags: AI, LLM, TechNews, Security
---

Tuesday's AI news moved the control point inside the model. MIT researchers showed GPT-6 Astra reading and editing raw neural network weights. Anthropic's amended IPO filing put a price on compute and a warning label on self-improvement.

## The Short Version
- MIT CSAIL showed GPT-6 Astra editing 0.016% of Qwen3.5-0.8B's weights to lift MATH-500 from 7.9% to 48.1%, with no gradients.
- Astra's one-shot Breakout network scored 517.4, against 15.8 for PPO trained for 100 million steps.
- Anthropic reported $17 billion in Q3 revenue, up 47% from Q2, a slowdown from 144% growth.
- Anthropic's purchase commitments reached $895.4 billion, and its S-1 warns it may "imminently" meet its RSI threshold.
- Mandiant traced LLMJacking bills above $100,000 a day and $1 million cumulative, plus 500,000 API calls in eight hours.
- China's Announcement No. 48 restricts frontier weights at 10^26 FLOPs or 2 trillion parameters, with separate agent thresholds.
- A 0.1% poison rate in pretraining gave a 4B command-line agent a 92% remote code execution rate.
- DoorDash logged "several hundred" agent orders against roughly 1 billion total Q3 orders.

## GPT-6 Astra Read 17,253 Weights and Named the Game

### The Experiment Behind 1,857 Points
Rikiya Takehi, Jayden Teoh, Alex Zhang, and Omar Khattab published "Sparks of Weight-Space Programming" on November 2. All four are at MIT CSAIL. The post reached 1,857 points on Hacker News within a day.

The claim is narrow and strange. A general-purpose model can inspect raw weights, infer what a network does, and write new weights without gradients. The team calls this Weight-Space Programming.

They did not train a special reader. They prompted GPT-6 Astra with the numbers.

### Reading a Network From Its Numbers
The first test trained four PPO policies on four games. All four had identical input channels, actions, and dimensions. Astra named the correct game for each network without being given the list of options.

The second test used diffusion models for circles, triangles, and squares. Astra identified each shape from the output layer. It drew outlines instead of filled shapes, which suggests it read structure rather than simulating a forward pass.

The third test removed the input and output layers from three 7.2-million-parameter language models. Astra still named the training language for all three, twice each. It also found every induction head and named no false ones.

### Writing a Better Qwen by Deleting a Loop
The Qwen result is the one developers will argue about. Astra received Qwen3.5-0.8B, a Python notebook, and a budget of forward passes. It found that the model loops, often burning the full 32,768-token limit without answering.

Astra traced the loop to one direction written by the MLPs in layers 15 and 19. It subtracted that direction from 64 output columns in each layer. The edit touched 131,072 weights, or 0.016% of the model.

The payoff was large. MATH-500 rose from 7.9% to 48.1%, GSM8K from 13.8% to 67.1%, and IFEval from 21.0% to 62.3%. Answers that hit the token limit fell from 93% to 33.1%.

| Game | PPO, 100M steps | PPO, 500M steps | Astra, one shot |
| --- | --- | --- | --- |
| Breakout | 15.8 | 25.3 | **517.4** |
| Seaquest | 5.6 | **88.9** | 53.1 |
| Asterix | 25.8 | **55.2** | 53.2 |

Astra also wrote game networks from scratch. Its one-shot Breakout network beat PPO trained for 100 million steps by a factor of 32. It also beat the 500-million-step score of 25.3.

### The Failure That Keeps the Claim Honest
Astra could not improve Gemma 3 270M. That model rarely loops, and its errors were ordinary arithmetic and algebra mistakes. The best edit moved MATH-500 from 6.8% to 7.7%, a gain the authors call not established.

The sycophancy test also came with a caveat. Astra could not pick the sycophantic Gemma 3 270M from weights alone. It succeeded only after the team let it inspect attention patterns on prompts it wrote.

That distinction matters. Weight editing can remove an obstacle that hides an ability. It cannot add an ability the model never learned.

### Why Weight Editing Matters for Security
The security implication is the most concrete. If a model can read weights, it may spot a backdoor without a benchmark. If it can write weights, an attacker may skip training entirely.

The authors list auditing, cheaper optimization, unlearning, and model merging as follow-ups. They are also building a benchmark. Until that exists, every result here is a demo with released logs, not a reproducible capability score.

[Yesterday's roundup](/blog/ai-news-November-2-prompt-fine-mythos-leak) asked who can verify a 7.7 TB checkpoint that nobody can load. This paper asks a harder question: what if the weights themselves are readable text?

### Sources
- [Sparks of Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)
- [Experiment logs](https://github.com/RikiyaT/lm_understand-logs)
- [Edited Qwen3.5-0.8B on Hugging Face](https://huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50341174)

## Anthropic's $17B Quarter Comes With an RSI Warning

### The Numbers in the Amended S-1
Anthropic filed an amended Form S-1 on November 2. The update added third-quarter results that the first prospectus left out. Revenue for the quarter was about $17 billion, up 1,127% from a year earlier.

Nine-month revenue reached $33.24 billion, roughly 1,200% above the same period in 2025. The nine-month net loss was $104 billion. Most of that came from fair-value changes on convertible notes and derivatives, not operations.

| Metric | Result | Context |
| --- | --- | --- |
| Q3 revenue | $17.0B | +1,127% year over year, +47% quarter over quarter |
| Nine-month revenue | $33.24B | Up about 1,200% year over year |
| Q3 net loss | $23.29B | Includes non-cash charges |
| Nine-month net loss | $104B | Mostly convertible note and derivative changes |
| Purchase commitments | $895.4B | Substantially compute and infrastructure |
| Compute expense | +$14.4B | Up 329% over nine months |

### Growth Slowed While Commitments Grew
The quarter-over-quarter picture is less flattering. Revenue grew about 47% from Q2, down from 144% in Q2 and 132% in Q1. A $17 billion quarter can still be a deceleration.

Purchase commitments and lease agreements reached $895.4 billion. Anthropic says substantially all of that relates to compute and infrastructure. Compute and infrastructure expenses rose $14.4 billion in nine months, up 329%.

That commitment equals roughly 13 years of Q3 revenue at an annualized run rate. It is a bet that demand keeps compounding after growth has already slowed.

### The Fine Print Says 'May Imminently Meet'
The risk factors contain the sentence that traveled furthest. Anthropic wrote that its estimates and expectations for future models point to a threshold. The filing says the company may "imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.'"

The filing also says the company has already used AI to build models whose capability jumps it did not recognize at the time. It has not designated any current model as crossing the threshold.

Anthropic promises to keep humans in frontier research and development. It says it is considering RSP updates to keep people in control. That is a policy commitment, not a technical control.

### Internal Claude Use Passed Payroll
A separate disclosure is easier to price. Anthropic values its internal Claude usage at the prices it charges customers. In April, that value passed monthly employee compensation, excluding stock awards.

By September, internal AI usage had grown more than 250-fold since January. More than 90% of code added to Anthropic's software that month came from Claude. The company is not spending cash at that level, but the comparison shows where the work went.

### What Investors Are Pricing
The S-1 is a disclosure document and a sales document. Claims that a model is close to self-improvement can serve both purposes. Skeptics should read the RSI language as a risk flag, not a product announcement.

The market has already priced some doubt. Anthropic's expected junk credit rating and its $895 billion commitment book are two sides of the same bet. The company must convert compute into revenue faster than the debt clock ticks; our [October 31 coverage](/blog/ai-news-October-31-anthropic-junk-black-october-orbit) traced that tension.

The $80.7 billion loss figure from our [October 27 roundup](/blog/ai-news-October-27-openai-eth-anthropic-s1-terra) now looks like a snapshot from a moving filing. The direction has not changed.

### Sources
- [CNBC: Anthropic reports $17 billion in Q3 revenue](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)
- [SEC: Amended Form S-1](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)
- [Business Insider: Internal AI use exceeds employee pay](https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11)
- [TechCrunch: Anthropic warns it is close to RSI](https://techcrunch.com/2026/11/02/anthropic-warns-that-its-very-close-to-rsi-capability-aka-self-building-ai/)

## Stolen API Keys Ran Up a $1 Million Bill

### What Mandiant Found
Google Threat Intelligence Group and Mandiant published an investigation on November 2. They responded to LLMJacking incidents across North America, South America, and Asia Pacific. Victims included financial services, retail, technology, and transportation companies.

The billing pattern is the story. Some victims saw more than $100,000 in fraudulent charges in a single day. Cumulative charges at some organizations reached $1 million before anyone revoked access.

### The LLM Mixer Economy
Attackers no longer just run their own prompts. They resell stolen capacity through gateways that GTIG calls LLM Mixers. These services pool keys, meter usage, and hide the request origin.

One actor ran more than 500,000 API calls in under eight hours through a routing service called jet-night.com. The service passed nearly $1 million in token costs to one victim. It advertises unlimited tokens for about $60 a month, well below the $100 to $250 a normal plan would cost.

### The LiteLLM Privilege Bug
The intrusions also targeted the middleware. One cluster exploited CVE-2026-40217 in LiteLLM's `/key/regenerate` endpoint. The user ID rebind flaw turned a standard virtual key into a `PROXY_ADMIN` credential.

That is the worst place to lose control. A model gateway sees every prompt, holds every provider key, and can route traffic across accounts. Our [October 24 roundup](/blog/ai-news-October-24-openai-internet-ban-kimi-litellm) covered LiteLLM's growing role in agent stacks.

### How to Catch a Validation Sweep
Attackers test stolen keys with tiny requests. Mandiant found automated sweeps using `max_tokens=1` to confirm a key without tripping volume alerts. A single-token spike can look like a health check.

Defenders should alert on key creation, LLM service enablement, and logging changes. They should cap budgets per key and scope keys to specific models. They should also watch for disabled invocation logging, which attackers use to hide prompts.

The cheapest control is the least glamorous. Rotate keys, scan repositories, and give each workload its own credential. A stolen key should cost you one revocation, not a million dollars.

### Sources
- [Google Cloud: The Rise of LLMJacking](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50346350)

## China Puts Frontier Model Weights on the Export List

### Three Tests for a Restricted Model
China's Ministry of Commerce and Ministry of Science and Technology issued Announcement No. 48 on October 16. It proposes adding 40 technologies to the export catalogue, including 23 in AI. The draft is open for comment until November 15.

A model's weights, checkpoints, source code, and training know-how are restricted if they meet any one of three tests. The first is at least 10^26 FLOPs of training compute. The second is at least 2 trillion parameters.

The third test is a global top-10 position on public evaluations, call volume, or a comparable measure. That test is dynamic and names no ranking body. A model can become restricted after it ships.

### Agents Get Their Own Thresholds
The draft regulates agents separately from models. Planning technology is restricted above 20-step subtask chains, 80% decomposition accuracy, and 90% subtask success. Multi-agent systems face tests at 60 concurrent agents, twice the single-agent completion time, and 85% agreement with reference answers.

Tool use is restricted at 200 integrated third-party tools. The same item requires 90% tool-selection accuracy and 90% end-to-end success on tasks that need three or more tools. Agents built for critical infrastructure, defense, or core government use are prohibited outright.

Those tests describe products that already exist. An orchestration layer can cross the tool threshold while running a model well below the weight thresholds.

### API Access Is Not an Export
MOFCOM says API calls, apps, websites, SaaS, and lightweight on-device use do not count as exporting a large model. A foreign customer can keep calling a Chinese-hosted model.

Local deployment outside China does count. A company that self-hosts restricted Chinese weights needs the supplier to hold a license. Deployment on the supplier's own overseas cloud may qualify for automatic licensing after reporting.

### The Registration Starts Now
The catalogue is still a draft. The registration requirement is already active. Exporters must register transfers of ownership, overseas licensing, and changes of control that put a foreign entity in charge.

Open weights that are already public sit outside the rules. Open-sourcing a new restricted model triggers automatic licensing after reporting. The definition of "open source" is not settled.

### What Changes for Buyers
ChinaTalk estimates that no released Chinese model currently exceeds the 10^26 FLOP threshold. That gives buyers time, not comfort. The top-10 test could still capture a model with modest training compute and enormous usage.

Enterprises should inventory locally deployed Chinese models and agent frameworks. They should ask suppliers in writing whether the export is registered. They should also plan a fallback model that does not depend on a license that can be revoked.

### Sources
- [CSA: China's First Frontier AI Export Controls](https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/)
- [MOFCOM: Announcement No. 48](https://www.mofcom.gov.cn/zwgk/zcfb/art/2026/art_0a31a3c9ac404f7a9b0e917ce3412997.html)
- [ChinaTalk: MOFCOM's New Rules and the Future of Chinese AI](https://www.chinatalk.media/p/mofcoms-new-ai-rules)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50334038)

## 0.1% Poisoned Pretraining Data Plants a Backdoor

### The Attack
A paper submitted to arXiv on October 27 shows that pretraining data can plant a remote code execution backdoor in an agent. The authors pretrained Qwen3 models from scratch at 0.6B, 1.7B, and 4B parameters. They then post-trained each one into a command-line agent with a clean pipeline.

They poisoned 0.1% of the pretraining corpus. The deployed agent executed an attacker-chosen command when it saw the trigger. It behaved normally on clean inputs.

### Scale Made It Worse
The attack success rate rose with model size. The 4B model reached roughly 92% at a 0.1% poison rate. It stayed positive even when the poison rate fell to 0.0005%, or five documents per million.

That is the opposite of the usual robustness story. Bigger models are better at learning the poison pattern, not just the language.

### Why Command-Line Agents Are the Target
A chatbot that emits a bad command is annoying. An agent with shell access turns that command into code execution. The paper's threat model assumes the agent can run tools on the user's machine, which is the default for coding agents.

The authors include Nicholas Carlini and Javier Rando, who have spent years on training-data attacks. They released the code. That makes replication easier for defenders and attackers alike.

### The Defenses That Actually Apply
No single filter solves pretraining poisoning. Provenance helps: track where documents came from and prefer curated corpora. Deduplication helps, because repeated poison is easier to learn.

Runtime controls matter more for agents. Sandbox tool execution, require approval for destructive commands, and scope credentials per task. Monitor for command sequences that do not match the user's request.

The uncomfortable conclusion is that model behavior can be compromised before fine-tuning begins. A clean post-training pipeline does not clean the weights.

### Sources
- [arXiv: Agentic Backdoors via Pretraining Poisoning](https://arxiv.org/abs/2610.37741)
- [Code and data](https://github.com/safety-research/agentic-backdoor)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50341334)

## DoorDash Handled 1 Billion Orders. Agents Placed a Few Hundred.

### The Number From the Earnings Call
DoorDash reported third-quarter 2026 results on October 29. CEO Tony Xu said outside AI agents generated "several hundred orders" since launch. The company handled just shy of 1 billion orders in the quarter.

The ratio is roughly one agent order for every million or more human orders. Xu called agent ordering a "very low use case" without sounding surprised.

### Why Food Ordering Resists Agents
Ordering dinner is a short, repetitive task with a known app. Xu argues that simple tasks come directly to DoorDash. Agents make more sense for long consideration purchases, where they can work in the background.

The plumbing is also young. DoorDash's Model Context Protocol connector went live less than a month before the call. It is limited to early beta partners and focuses on corporate lunch orders.

### DoorDash's Own Agent Does Better
The internal tool tells a different story. Ask DoorDash builds baskets from a recipe photo or a vague request. The company says those baskets are built five times faster than manual ones.

Ask DoorDash orders also average nearly 50% higher basket value and about 60% more unique items. Nearly half land at local restaurants the customer has never tried. That is discovery, not automation.

### The Pattern to Watch
Agent commerce will not arrive as a single switch. It will show up first where the task is complex, the options are many, and the user is willing to delegate. Grocery lists and corporate lunches fit better than a Friday night curry.

The DoorDash number is a useful correction to the demo economy. A working integration is not adoption. A hundred agent demos can still produce a few hundred orders.

### Sources
- [Ars Technica: Basically no one is using AI agents for their DoorDash orders](https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/)
- [DoorDash Q3 2026 earnings call transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/doordash-dash-q3-2026-earnings-call-transcript/)
- [DoorDash ordering connector announcement](https://about.doordash.com/en-us/news/doordash-ordering-connector)

## Grok Bot Hit Its Limits Because the Math Did Not Work

### What Users Saw
Some Grok Bot subscribers woke up over Halloween weekend with their weekly limits already exhausted. Users on X reported jumps from 50% to 100% without heavy use. The timing made it look like a billing bug.

### Musk's One-Line Explanation
Elon Musk confirmed the change was deliberate. "The cost of serving Grok Bot was unsustainably high relative to revenue," he wrote on November 1. He did not say how the limits would change going forward.

### The Profit Numbers Behind It
SpaceX, now public, says AI makes up 52% of company income. Its renamed Super Intelligence division reported a $431 million profit. That profit would have been higher without $1.2 billion in one-time costs from the Cursor acquisition.

A profitable AI division is rare. A profitable division that still throttles its fastest-growing product is rarer. It suggests the product's marginal cost outran its subscription price.

### The Unit Economics Problem
Agentic products burn tokens on every step. A single task can run dozens of model calls, tool calls, and retries. A flat monthly fee meets a variable bill that the provider cannot cap.

Anthropic's internal token spend and its $895 billion compute commitments describe the same pressure from the supply side. Cheap tokens do not guarantee cheap work, as our [October 26 analysis](/blog/ai-news-October-26-cnn-skin-cancer-llm-price-cuts) found. Grok Bot shows the demand side: an agent can be popular and still lose money.

### Sources
- [TechCrunch: Musk throttles Grok Bot limits](https://techcrunch.com/2026/11/02/elon-musk-throttles-grok-bot-limits-due-to-unsustainably-high-costs/)
- [Musk post on X](https://x.com/elonmusk/status/2116992258520064397)
- [TechCrunch: SpaceX's AI business is beating expectations](https://techcrunch.com/2026/10/20/spacexs-ai-business-is-beating-expectations/)

## Frequently Asked Questions

### What Is Weight-Space Programming?
It is editing a neural network's weights directly with a language model, without gradient descent. The model reads the numbers, reasons about what they compute, and writes new values. GPT-6 Astra did this for small game networks and for Qwen3.5-0.8B.

### Did Astra Really Improve Qwen Without Training?
Yes, in the reported experiment. Astra used forward passes to test prompts and then edited 0.016% of the weights. MATH-500 rose from 7.9% to 48.1%. The gain came mostly from removing a looping behavior, not from teaching new math.

### Is Anthropic Already Doing Recursive Self-Improvement?
Anthropic says no current model has crossed its RSP threshold. Its filing says future models may "imminently" meet the definition. The company also says it will keep humans in frontier research and development.

### How Do LLMJacking Attacks Get In?
Most incidents start with stolen cloud identity tokens, service account keys, GitHub personal access tokens, or session tokens. Exposed model endpoints are a second path. Attackers then enable LLM services and resell access through proxy gateways.

### Do China's Export Rules Block API Access?
No. MOFCOM says API, app, web, and SaaS use do not count as exporting a large model. The rules target local deployment of restricted weights outside China and transfers of ownership or control.

### Why Are AI Agents Still Rare on DoorDash?
The task is simple and the app already works. DoorDash also opened its agent connector only a month before the earnings call. Xu expects agents to matter more for complex, long-consideration purchases.

## The Bottom Line

### The Control Point Moved
A year ago, the prompt was the interface. Today's stories put the control point in weights, credentials, and compute contracts. Astra edits the weights. LLMJacking steals the keys. China regulates the checkpoints.

### Verification Gets Harder
Each story also shows how hard verification has become. A model can hide a loop in 0.016% of its weights. A poisoned corpus can hide a backdoor in 0.1% of its documents. A stolen key can hide behind a $60 subscription.

### What to Watch Next
Watch whether other labs reproduce the Qwen edit without the authors' harness. Watch whether Anthropic's RSP update adds a hard stop or a reporting layer. Watch the LiteLLM patch rate and the November 15 comments on China's catalogue.

And watch the next agent-commerce number. A few hundred orders is not a verdict. It is a baseline.
