---
title: "Google Logs the First Fully Automated AI Attack as Windows Counts Your Coding Agents"
meta_title: "AI News Nov 17: Autonomous Hacks, MCP Flaws, $1.4T IPO"
author: Abdul Hadi
date: 2026-11-17
updated: 2026-11-18
slug: ai-news-November-17-autonomous-ai-attack-mcp-misbinding
image_alt: "Bar chart comparing claimed 95% confidence with measured coverage: most models 20-62%, GPT-6 Astra 94%, Claude Fable 5.2 99%"
description: "Google spots the first fully automated AI attack, Windows 11 counts your coding agents, and 12 models give one shared opinion. Today's AI news, decoded."
keywords: AI news November 17 2026, autonomous AI cyberattack, Google GTIG agentic threats, Windows 11 coding agent telemetry, MCP provider misbinding, JetBrains LLM bias study, weight-space programming, Anthropic IPO
tags: AI, LLM, TechNews, Security, Research, Agents
---

## Today's Storylines

### A Tuesday Where Agents Stopped Being Demos

Google says an attacker ran vulnerability discovery and exploitation without a human in the loop. Microsoft shipped a Windows component that counts which coding agents you launch. Two arXiv papers measured how badly models judge their own certainty.

### The Five-Minute Version

- Google Threat Intelligence Group documented the first fully automated vulnerability exploitation pipeline, built on multi-agent frameworks such as ARTEX, CAIRN, and PentAGI.
- LLMJacking cases reached $100,000 in fraudulent charges per day, and $1 million cumulative in the worst case.
- A reverse-engineering writeup found Windows 11 records which coding agents and developer tools you run, then uploads a bitmap to Microsoft.
- Optimizely served malware to visitors of 178 organisations, including Zoom, BBC, CNN, and GitLab.
- JetBrains asked 12 models for hot takes 1,200 times. 75% were attacks, and Python absorbed 299 of 312 takes.
- Researchers replicated weight-space programming: GPT-6 Astra wrote Breakout networks scoring 514, 550, and 307, against MIT's 517.
- SciResearch-Eval found most models' 95% intervals contain the truth in only 20-62% of cases.
- Anthropic lists on Thursday at an expected $1.4 trillion valuation, minting more than 4,000 staff millionaires.

## Google Says the First Fully Automated Attack Has Arrived

### What Google's Threat Team Found

Google Threat Intelligence Group published its quarterly AI threat tracker on November 16. The headline finding is narrow and serious. GTIG identified an exposed staging server running a multi-agent framework it calls `exploit_agent`.

The framework compares web application code before and after patch releases. It flags candidate flaws, drafts exploits, and executes them. No human approves a step.

[The full GTIG report](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold) says victim telemetry pointed at French media, entertainment, and education websites. Configuration comments were written in Russian.

Google did not attribute the activity to a named state group. [Politico's reporting, summarised by UNITED24](https://united24media.com/world/russian-speaking-hackers-launched-first-fully-automated-ai-cyberattack-google-says-24451), describes it as a possible first fully automated AI cyberattack.

### The Frameworks Doing the Work

GTIG observed four open-source offensive frameworks in live intrusions or active testing. Each trades stealth for speed.

| Framework | What it does | What GTIG saw |
|---|---|---|
| CAIRN | OODA-loop agents sharing a blackboard | Used against US aerospace targets |
| CyberStrikeAI | Go backend plus 100+ security tools | Experimentation observed |
| HexStrike AI | MCP harness, 150+ tools, 12+ sub-agents | Experimentation observed |
| PentAGI | Lowers the bar for entry-level operators | Custom builds used against Asian organisations |

The pattern is consistent. The frameworks find low-complexity flaws, generate single-use payloads, and adjust tactics from live execution feedback.

Barracuda has since tied a 44-hour cloud intrusion to ARTEX, covered in [our November 18 roundup](https://blogs.thetrillioniar.me/blog/ai-news-November-18-java4shell-patch-outages-microsoft).

This is the same exploit economics we covered when [the PHP `php2shell` flaws leaked before patches](https://blogs.thetrillioniar.me/blog/ai-news-November-5-provable-inference-php2shell). The difference is who is holding the tool now.

### The Money: LLMJacking at $1 Million

Stolen model access has become its own market. Mandiant handled incidents where attackers consumed victims' LLM quotas inside compromised cloud accounts.

Some single-day fraudulent bills passed $100,000. The worst cumulative case reached $1 million before remediation.

Attackers also sold that access onward. GTIG tracked "LLM Mixers", storefronts that route buyers through pools of stolen credentials. Advertised prices ran from $0.10 to $25 per million tokens.

One vendor, APIMart, applies a 5x surcharge once a prompt passes 100,000 tokens. That is cheaper than retail for frontier models, which is the whole business model.

### The Supply Chain Trick: A Settings File

The most reusable finding is not a zero-day. It is a configuration file.

In intrusions against cryptocurrency firms in North America and Europe, a cluster tracked as MIDNIGHT NEPTUNE modified `.claude/settings.json` inside victim repositories. Starting Claude Code then downloaded a backdoor named SOMBERMEME.

The actor also generated GitHub personal access tokens named after Microsoft Copilot to blend into normal developer activity. Recruiter profiles used AI-generated headshots carrying SynthID watermarks.

That is a cheap attack with a wide blast radius. Any tool that reads project-local config on startup inherits the same weakness.

### What Defenders Should Change

Three controls matter more after this report. Pin and review agent configuration files in code review. Scope cloud inference keys so a stolen key cannot scale. Watch for differential patching traffic against your own public endpoints.

Google's own mitigation advice is behavioural rulepacks plus its ARTEX hardening guide. The report is candid that detection is easier than prevention here, because autonomous execution leaves loud traces.

### Sources

- [Google GTIG: Agentic threat activity crosses a significant threshold](https://cloud.google.com/blog/topics/threat-intelligence/agentic-threat-activity-crosses-a-significant-threshold)
- [UNITED24: Russian-speaking hackers ran the first fully automated AI cyberattack](https://united24media.com/world/russian-speaking-hackers-launched-first-fully-automated-ai-cyberattack-google-says-24451)
- [Google GTIG: LLMJacking and monetising compromised cloud models](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models)

## Windows 11 Is Counting Your Coding Agents

### The Component and the Feature Flag

A reverse-engineering post by Xusheng published November 16 found coding-agent names inside `MissionControlAggregator.dll`. The component ships with Windows 11 and runs under the DiagTrack telemetry service.

The guard flag is called `CLICodingAgentUsage`, feature ID `62580080`. On the author's test VM, build `26200.9974`, the flag was already enabled without any manual opt-in.

[The writeup](https://xusheng.dev/posts/windows-coding-agent-telemetry/) documents the full path from string comparison to uploaded diagnostic event. It also includes reproduction steps.

### Four CLI Slots, Five Desktop Slots

The DLL checks executable names, not process behaviour. Four CLI slots cover `copilot.exe`, `claude.exe`, `codex.exe`, and `agy.exe`, plus extensionless variants on the WSL path.

Five desktop slots cover `github.exe`, `claude.exe`, `codex.exe`, `cursor.exe`, and `antigravity.exe`. A separate group tracks `python.exe`, `node.exe`, `gcc.exe`, `clang.exe`, `javac.exe`, and `code.exe`.

Some checks also verify the publisher. The Python slot expects the Python Software Foundation. The Node.js slot expects the Node.js Foundation.

The author tested it by copying `cmd.exe` to `codex.exe`. The rename alone set the Codex bit.

### What Actually Leaves the Machine

Collection collapses into a bitmap. Twelve broader tool categories, four CLI agents, and five desktop agents become bits in a `Segments.SubCohorts` event.

No prompt text, filenames, or source code appear in the report. The privacy problem is still real, because which agents a developer runs signals which vendor a company pays for.

With optional diagnostic data allowed, the report sat in DiagTrack's upload queue. A clean Windows 11 Home ARM64 install defaulted to "Include Optional", with `AllowTelemetry` set to `3`.

This is a smaller version of the same consent problem we wrote about when [Postman installed AI plugins without asking](https://blogs.thetrillioniar.me/blog/ai-news-November-4-postman-consent-ai-debt). Useful telemetry keeps arriving switched on.

### How to Turn It Off

Open Settings, then Privacy and security, then Diagnostics and feedback. Disable "Send optional diagnostic data".

You can also decline optional diagnostics during Windows setup. Enterprise fleets can set the telemetry policy at the device level.

Microsoft's [diagnostics and privacy guide](https://support.microsoft.com/en-us/windows/privacy/diagnostics-feedback-and-privacy-in-windows) documents the toggles. The company has not published a statement on the agent-specific bits.

### Sources

- [Xusheng: Windows 11 is collecting data on which coding agents you use](https://xusheng.dev/posts/windows-coding-agent-telemetry/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50524736)
- [Microsoft: Diagnostics, feedback, and privacy in Windows](https://support.microsoft.com/en-us/windows/privacy/diagnostics-feedback-and-privacy-in-windows)

## Optimizely Served Malware to 178 Organisations

### The Scale of the Injection

On November 16, malicious JavaScript reached visitors of 178 organisations through Optimizely Web. The list includes Zoom, the BBC, CNN, Salesforce, GitLab, IKEA, HSBC, and Ledger.

Report URI fetched 1,611 Optimizely snippets and found 188 infected. At 20:56 UTC that day, 169 were still live.

The attacker wrote into each customer's "Project JavaScript" field. The rest of the snippet stayed untouched, so the file still came from `cdn.optimizely.com` with a valid certificate.

### What the Payload Did

The injected loader pulled `track.js` from `1688360.cc`. The kit swapped crypto wallet addresses, skimmed card numbers, stole non-HttpOnly cookies, and captured screenshots.

On iOS 18.6 and earlier, it loaded the Coruna and DarkSword exploit chains in a hidden iframe. Devices on iOS 18.7.3 or iOS 26.3 and later were patched.

Attackers rebuilt the payload 26 times in one day. Verified wallet receipts reached about $7,040 before the funds were swept out on November 17.

### Why Content Security Policy Barely Helped

Report URI evaluated 256 affected hosts. Sixty-eight had no CSP at all.

Fifty had a policy that allowed both the payload and the data theft. Seventeen blocked exfiltration but not in-page address swapping.

Only 24, or 15%, blocked the payload outright. The dividing line was a restrictive `script-src`, not an allowlist entry for Optimizely.

The lesson generalises to every agent that loads third-party code. Trusting a vendor domain is not the same as trusting the code on it that day.

### Sources

- [Report URI: World's largest brands infected with malware via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50524767)
- [Optimizely status incident](https://status.optimizely.com/incidents/ftw0fh9wx43z)

## Twelve Models, 1,200 Hot Takes, One Shared Opinion

### The Experiment

JetBrains published the study on November 15. It asked 12 models from 10 labs for controversial programming-language opinions, 50 times each, in fresh conversations.

Every request returned. The whole dataset cost $7.68, about two-thirds of a cent per take.

The setup matters because it removes the system prompt. What is left is the model's default voice.

### The Numbers: 75% Attacks

Of 1,200 takes, 904 were attacks on a language. Only 291 defended anything.

Python took 312 takes, and 299 were attacks. Ten of the twelve models never said one positive thing about Python in 100 tries.

Rust drew 167 takes and 164 attacks. TypeScript drew 138 and 137. PHP drew 28 takes and 28 defences.

Go produced an exact tie at 118 attacks and 118 defences, almost all about `if err != nil`.

### The Homogeneity Problem

When told to pick a language at random, models picked a target. Gemini 4 Argon chose Python 35 times and attacked it all 35 times.

GPT-6.1 Sol and Gemini 4 Argon only ever named three languages. DeepSeek V4 Pro ranged widest with eight, then picked Rust 31 times and attacked it every time.

Repetition went beyond topic. Fifty-four answers reused an opening sentence the same model had already produced word for word. Qwen3.8 wrote "net negative" in 43 of its 100 answers.

Two labs produced one identical sentence about Java's checked exceptions. Claude Opus 5.5 wrote it seven times, GLM 5.3 three times.

### Cost, Speed, and Reasoning Effort

Mistral Large 4 spent a median of 3,063 reasoning tokens per take, at a median 32.1 seconds. GPT-6.1 Sol spent 108.

DeepSeek V4 Pro, served by a third-party host, spent a median of zero tokens and answered in 3.5 seconds. Its 100 takes cost $0.03, against $1.27 for GPT-6 Astra.

### What Builders Should Do With This

Asking three models for a second opinion buys less diversity than teams assume. The disagreement clusters around Go's error handling and little else.

That matters for evaluation design. A panel of models sharing training data will share blind spots, and a shared blind spot is invisible in agreement.

The practical fix is mechanical. Vary prompts, seed examples, and decoding settings before concluding that models disagree.

### Sources

- [JetBrains: AI models hate Python and love PHP](https://blog.jetbrains.com/ai/2026/11/ai-models-hate-python-and-love-php-we-asked-12-of-them-1-200-times/)

## Research Desk: Models Compile Programs Into Weights

### The Replication

A team ran a three-day sprint to test MIT's claim that GPT-6 Astra can write neural network weights directly. The results are on arXiv as [2611.21449](https://arxiv.org/abs/2611.21449).

Astra's Breakout networks scored 514, 550, and 307, against MIT's 517. They held up on two modified versions of the game.

Claude Opus 5.5 also wrote working networks. It frequently exhausted its output tokens before finishing.

### What Is Actually New

Earlier models could write a policy as code a generation before they could write it as weights. The interesting step is the translation between the two.

Two models independently decompiled Astra's Breakout network into Python. The decompiled code matched its actions in every tested state.

The result reads like a compiler, not a mind. The networks behave like hand-designed programs expressed in parameters.

### The Limits

On handwritten digit classification, Astra's networks averaged 50%. A simple baseline classifier reached 82%.

Reading weights is mostly reading the input layer. Astra could identify which game a network plays almost perfectly, but missed how a new game works.

Auditing worked better than expected, and shallower. Astra found a poisoned small language model in 10 of 10 runs, and a malicious adapter in 23 of 32. It never identified the trigger.

### Why It Connects to Last Week

This extends the weight-space work in [WeightBench and the weight-editing roundup](https://blogs.thetrillioniar.me/blog/ai-news-November-3-weight-space-llmjack). Benchmarks now exist for a capability that sounded like fiction in October.

The honest summary is in the paper's own conclusion. Models can read and write small networks today, which is a promising but early interpretability tool.

### Sources

- [Replicating and Extending Weight-Space Programming (arXiv)](https://arxiv.org/abs/2611.21449)

## Research Desk: 95% Confident, Often Wrong

### The Benchmark

SciResearch-Eval asks agents to measure a material's thermal properties. The agent designs its own experiments and reports each value with a 95% interval.

The simulator is sometimes under-resolved and sometimes missing physics. That is the trap.

The held-out split covers 93 tasks, 9 models, and 2,511 episodes. Scoring compares intervals against exact ground truth.

### The Calibration Gap

Most models handled the procedural traps. When physics went missing, they reported wrong values while stating 95% confidence.

Their intervals contained the truth in 20-62% of cases. GPT-6 Astra reached 94%, and Claude Fable 5.2 reached 99%.

Claude Opus 5.5 diagnosed the missing physics in only 35% of episodes, against 66% for Astra. Even when it noticed, its ranges often missed.

### Effort Buys Accuracy, Expensively

The correction is latent in the models. At maximum effort, Opus improved more than tenfold and stopped trailing Astra at default effort.

That recovery cost 13 to 31 times more reasoning. Older and open-weight models gained nothing from the extra effort.

Fable 5.2 was the most accurate model at default effort, with an interval score 1.9 times better than Astra's. It also wrote six times as many tokens.

### The Takeaway for Agent Builders

Confidence statements are cheap to generate and hard to trust. A number with a 95% label is not a calibrated number.

Build gates that check intervals against known physics before an agent acts. Otherwise the agent's certainty becomes your incident report.

### Sources

- [SciResearch-Eval (arXiv)](https://arxiv.org/abs/2611.21541)

## Research Desk: MCP Tool Names Are Not Identities

### The Attack Needs No Compromise

A new paper studies tool-provider misbinding in MCP-based agents. The attacker compromises nothing.

It runs its own MCP server and advertises tools with chosen metadata. The agent then routes a request to the attacker's tool instead of the legitimate one.

That is a different threat model from prompt injection. Nothing in the host, model, network, or legitimate server has to break.

### What Made It Work

The authors tested five LLM-based clients in a controlled MCP environment. Misbinding was driven by how signals combined.

The strongest failures came from exact name collision, a task-aligned description, and a compatible schema together. Authority-flavoured descriptions caused wrong-provider execution even without a name collision.

Different clients failed differently. Some selected the attacker's provider outright, some asked for clarification, and some resolved inconsistently between runs.

### Where This Fits

We covered a related MCP supply-chain problem in the [agent zero-click exploit roundup](https://blogs.thetrillioniar.me/blog/ai-news-september-21-plugin4shell-anthropic-100b). Agents inherit every trust decision their tools make.

For teams shipping agents, the paper points at provider identity as a first-class control. Verify signatures and origins, and pin server endpoints.

### Sources

- [When Tool Names Are Not Identities (arXiv)](https://arxiv.org/abs/2611.21577)

## Anthropic's $1.4 Trillion IPO Is Already Moving London

### The Listing

Anthropic lists on Thursday at an expected valuation of $1.4 trillion. That is the figure [The Guardian reported](https://www.theguardian.com/business/2026/nov/17/millionaire-factory-anthropic-ipo-set-to-fuel-ai-gold-rush-in-londons-high-end-property-market) on November 17.

More than 4,000 staff are expected to become millionaires as options vest. SaaStr estimated a minimum of $20 million per employee.

The company employs about 5,000 people worldwide, including more than 200 in the UK.

### The Numbers Behind the Hype

Anthropic's UK filings show £24.1 million spent on an average of 43 staff in 2024. That is £560,000 per person.

OpenAI's London staff averaged £2.3 million each last year, about 58 times the UK median full-time wage. Research engineer roles have advertised base salaries up to £630,000 before equity.

The macro picture is starker. UK GDP grew 0.7% in the third quarter, its fastest pace in two and a half years. Bloomberg analysis put roughly a quarter of this year's UK growth down to AI.

### The Caveat Worth Printing

Most of this wealth is on paper. Coutts describes founder clients as "paper rich, cash poor" until shares vest or sell.

Meanwhile, eight of ten properties in Mayfair, Belgravia, and Knightsbridge sold below asking price last month. The AI gold rush is arriving in a market that needs the money.

### Sources

- [The Guardian: Anthropic IPO and London's property market](https://www.theguardian.com/business/2026/nov/17/millionaire-factory-anthropic-ipo-set-to-fuel-ai-gold-rush-in-londons-high-end-property-market)

## FAQ

### Did Google really confirm the first fully automated AI cyberattack?

Google reported the first observed case of fully automated vulnerability discovery and exploitation with no human in the loop. Its GTIG report describes an `exploit_agent` framework that analysed patches, wrote exploits, and executed them. Google did not name the attacker as a state group.

### What data does Windows 11 collect about coding agents?

It records a bitmap of which agents and developer tools were used, in an event called `Segments.SubCohorts`. The report contains no prompts, filenames, or code. It is classified as optional diagnostic data and uploads by default in the US setup the researcher tested.

### Is the Optimizely compromise fixed?

Report URI observed all infected snippets cleaned by 23:11 UTC on November 16. The main payload domain was placed on clientHold on November 17 and no longer resolves. Affected sites should still rotate credentials and review project JavaScript.

### Do all AI models really give the same opinions?

Mostly, in the JetBrains test. Twelve models produced 904 attacks out of 1,200 takes, with Python, Rust, and TypeScript absorbing most of them. Fifty-four answers repeated an opening sentence the same model had already written verbatim.

### Should I trust a 95% interval from an AI agent?

Not without checking it. SciResearch-Eval found most models' intervals contained the true value in only 20-62% of flawed-simulator episodes, despite the stated 95% confidence.

## Keep Reading

### More AI News From This Week

- [Qwen4-Max landed at $1.50 per million tokens](https://blogs.thetrillioniar.me/blog/ai-news-November-16-qwen4-max-nvidia-return-hiring) as Nvidia's ex-CEO eyed a comeback.
- [Agents ported 800,000 lines of Rust](https://blogs.thetrillioniar.me/blog/ai-news-November-15-rust-port-meta-fine-lovable-leak) while Italy fined Meta €805 million.
- [Postman installed AI plugins without consent](https://blogs.thetrillioniar.me/blog/ai-news-November-4-postman-consent-ai-debt) and exposed API data.
- [PHP's php2shell flaws leaked before patches](https://blogs.thetrillioniar.me/blog/ai-news-November-5-provable-inference-php2shell) and drew hundreds of fake proof-of-concepts.
- [Weight-space programming first appeared last week](https://blogs.thetrillioniar.me/blog/ai-news-November-3-weight-space-llmjack) alongside $1 million LLM key thefts.
