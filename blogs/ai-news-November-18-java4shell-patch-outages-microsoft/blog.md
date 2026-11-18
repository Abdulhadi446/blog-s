---
title: "AI Found a 9.2 Java Flaw in an Hour, Then the Patch Wave Broke the Internet"
meta_title: "AI News Nov 18: A Critical Java Flaw Found in an Hour"
author: Abdul Hadi
date: 2026-11-18
updated: 2026-11-18
slug: ai-news-November-18-java4shell-patch-outages-microsoft
image_alt: "Timeline showing AI flagging the Java4Shell flaw in OpenJDK's Base64 decoder after one hour, with a working exploit at three hours and a CVSS 9.2 rating"
description: "AI found a critical Java flaw in one hour for under $200. Then mass patching grounded flights. Microsoft's cheaper coding models and more, explained."
keywords: AI news November 18 2026, Java4Shell CVE-2026-114938, Codex vulnerability discovery, AI patching outages, Microsoft MAI Code 2, ARTEX AI cyberattack, Kokoro Hugging Face hijack, AI sycophancy climate study
tags: AI, LLM, TechNews, Security, Research
---

## Today's Storylines

### The Day the Patch Queue Became the Incident

An AI coding assistant found a critical OpenJDK flaw in about an hour. The fix landed Tuesday. By then, officials were telling Congress that AI-identified vulnerabilities had triggered a patch rush big enough to ground flights and knock banks offline.

### The Five-Minute Version

- Codex found CVE-2026-114938, a CVSS 9.2 memory bug in Java's Base64 decoder, for under $200 in AI usage.
- Unauthenticated exploits worked against default Keycloak, Jira, Confluence, Jenkins, Artifactory, and PingFederate.
- Bank executives and the NSA told lawmakers that AI-driven patching caused this week's outages, not an attack.
- Microsoft launched MAI Code 2 and MAI Cyber 2 Flash, claiming 96% of Claude Opus 5.5 at 5% of the cost.
- Barracuda tied a 44-hour cloud intrusion to ARTEX, the same framework the FBI says breaches networks in under three hours.
- Vals.ai found frontier models will mark civilians as targets, and will keep going if told it is a game.
- Researchers took over Kokoro's Hugging Face account and poisoned its weights in 87 seconds.
- UNESCO and UCL found climate answers lost 31 to 35 accuracy points after users pushed back.

## AI Found a 9.2 Java Flaw in About an Hour

### The Bug: 64 A's and an Equals Sign

Java4Shell, tracked as CVE-2026-114938, is a memory-corruption flaw in OpenJDK's Base64 decoder. A string of 64 "A" characters followed by a single equals sign is enough to trigger it.

The bug lives in a hand-written AVX-512 intrinsic that HotSpot swaps in after the decoder warms up. Padding pushes the computed output length to -1 or -2. The mask that builds the store never clears, so the write runs past the buffer.

[Mikiri's technical write-up](https://mikiri.ai/attack-scenarios/java4shell/) walks through the masking error step by step. The short version: Java still throws an exception, but the neighbouring heap is already overwritten.

### What It Breaks

The flaw affects OpenJDK 17.0.6 and later, plus the 21, 25, and 27 lines before Tuesday's update. It requires an x86-64 CPU with AVX-512 VBMI.

Researchers at Calif achieved unauthenticated remote code execution against Keycloak, Atlassian Jira, Atlassian Confluence, JFrog Artifactory, Jenkins, and PingFederate. They also exploited Kafka, Solr, Elasticsearch, Gerrit, and Spinnaker after login.

[Calif disclosed the flaw](https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/) with a CVSS 4.0 score of 9.2. Oracle rated it 8.1 under CVSS 3.1 and shipped fixes in its November patch update.

### The Economics: Under $200

Researcher Quang Luong found the bug with OpenAI's Codex during an audit of OpenJDK internals. According to Calif, the discovery took about one hour.

An initial working exploit took another two hours. Total AI usage cost came in under $200. AI agents also helped build the application-specific exploitation chains.

That price tag is the story. A nine-figure enterprise RCE class used to require a research team and a quarter. Now one auditor with a coding agent can find one between meetings.

This is the same curve we tracked when [GPT-6 Cyber found 81 Firefox bugs](https://blogs.thetrillioniar.me/blog/ai-news-November-6-gpt6-cyber-metr-anthropic-hy4-wyoming). Finding is cheap now. Patching is not.

### The Patch and the Caveat

Fixed builds are 17.0.21.1, 21.0.13.1, 25.0.5.1, and 27.0.1.1. CISA asked organisations to patch on disclosure day, November 17.

There is no universal exploit. An attacker still needs a path that feeds hostile Base64 into the decoder before authentication. HTTP Basic credentials, SAML artifacts, CSRF tokens, and file uploads all qualify.

Vendors can backport the fix without changing the version string. Check the build number, not just `java -version`, and remember that container images and appliances carry their own runtimes.

### Sources

- [BleepingComputer: Critical Java4Shell flaw allows RCE attacks](https://www.bleepingcomputer.com/news/security/critical-java4shell-flaw-allows-rce-attacks-on-major-java-applications/)
- [Mikiri: Java4Shell technical analysis](https://mikiri.ai/attack-scenarios/java4shell/)
- [Oracle Security Alerts](https://www.oracle.com/security-alerts/)

## The Patch Wave Behind This Week's Outages

### What Went Down

The United States paused all flights nationwide. Customers lost access to bank accounts. A highly classified NSA communications network went offline.

None of it appears to have been a cyberattack. [The Washington Sun reported](https://www.washingtonsun.com/technology/bank-ceos-nsa-tell-congress-ai-driven-patches-behind-outages) that the failures followed emergency patching, based on three people familiar with private congressional briefings.

### What Officials Told Congress

Wall Street executives and the NSA told lawmakers that AI models had identified large numbers of vulnerabilities. Teams then tried to patch them all at once.

"These models are identifying massive vulnerabilities, and that increases the urgency to patch right away," one congressional official said. "They're trying to push through a lot of patches all at once, more than the system was designed for."

The [NSA network outage was reported separately by CNN](http://cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down). Details remain scarce and the reporting rests on anonymous sources.

### Why AI-Driven Patching Overloads Systems

Patch management assumes a queue sized by human discovery. AI scanners break that assumption in two ways.

First, they find more issues per week. Second, they find them in code paths nobody has touched in years, so the fixes arrive without tested rollback plans.

The result is a thundering herd of changes across shared dependencies. A single bad maintenance window can cascade through authentication, networking, and payments at the same time.

### What to Do Differently

Cap the patch rate per service, not the number of findings. Require a rollback rehearsal for anything touching identity or network control planes.

Rank by exploitability in the wild, not by scanner severity. And stagger vendor windows so two critical dependencies never move on the same night.

The uncomfortable conclusion is that discovery speed has outrun change management. That gap is now an availability risk, not just a security one.

### Sources

- [The Washington Sun: Bank CEOs, NSA tell Congress AI-driven patches are behind outages](https://www.washingtonsun.com/technology/bank-ceos-nsa-tell-congress-ai-driven-patches-behind-outages)
- [CNN: Classified NSA communications network goes down](http://cnn.com/2026/11/17/politics/highly-classified-national-security-communications-network-goes-down)

## Microsoft Ships Cheaper Coding and Security Models

### The Three Models

At Ignite 2026, Microsoft introduced MAI Code 2, MAI Code 2 Flash, and MAI Cyber 2 Flash. All three target enterprise software work rather than open-ended research.

MAI Code 2 handles multi-file changes, debugging, and repository-scale tasks. The Flash variant covers high-volume work such as explanations, targeted edits, and routine fixes.

Both coding models ship through GitHub Copilot. MAI Code 2 Flash also has a limited preview in Microsoft Foundry.

### The Price Claims

Microsoft says MAI Code 2 reaches 98% of GPT-6.1 Sol's coding performance at about 40% of the price. It also claims 96% of Claude Opus 5.5 at 5% of the cost.

Those numbers come from four benchmarks: DeepSWE 1.1, Terminal Bench 2.1, SWE-Atlas, and FrontierCode v1.1. [Tech Wire Asia summarised the launch](https://www.techwireasia.com/2026/11/microsoft-unveils-new-ai-models-for-coding-and-cybersecurity/) and the benchmark mix.

MAI Cyber 2 Flash scored 92.3% on CyberGym-E2E, against 91.5% for GPT-6 Astra. It carries a one-million-token context window, four times the previous MAI Cyber model.

### The Caveats

Microsoft calculated its cost figures with a 50% promotional discount. Three of the four coding benchmarks ran on Microsoft's internal evaluation platform.

Pricing comparisons also depend on reasoning effort and workload shape. A 5% cost claim on one benchmark suite is a marketing number until independent runs reproduce it.

The strategic read is simpler than the table. Microsoft is pricing its own models to compete with the labs it also resells. That is the same pressure we saw when [Qwen4-Max landed at $1.50 per million tokens](https://blogs.thetrillioniar.me/blog/ai-news-November-16-qwen4-max-nvidia-return-hiring).

### Sources

- [Tech Wire Asia: Microsoft unveils new AI models for coding and cybersecurity](https://www.techwireasia.com/2026/11/microsoft-unveils-new-ai-models-for-coding-and-cybersecurity/)
- [Reuters: Microsoft unveils AI models for coding, cybersecurity](https://www.reuters.com/legal/litigation/microsoft-unveils-ai-models-coding-cybersecurity-it-takes-anthropic-openai-2026-11-17)

## ARTEX: From a Stolen Vendor Key to the FBI's Three-Hour Claim

### Barracuda's 44 Hours

Barracuda disclosed that an attacker accessed about 10 of its cloud accounts over 44 hours, between November 1 and 2. The intrusion was discovered on November 4.

The entry point was a cloud access key issued to a third-party AI vendor. That key stayed live after the project ended and sat in a configuration file in the vendor's GitHub repository.

[Barracuda's account](https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/) says the attacker moved through analytics systems, source repositories, and Kubernetes clusters. The firm matched the command style to the open-source ARTEX pentesting framework and called it a "machine-speed intrusion."

### The FBI Warning

The FBI has separately warned that ARTEX can break into networks in under three hours, [according to The Next Web](https://thenextweb.com/news/fbi-artex-ai-hacking-tool-amazon-barracuda). The same framework appeared in the Google threat report we covered yesterday.

Barracuda says the activity resembled a recent Railway incident, which also involved credential chaining and apparent ARTEX use. The attacker hunted for crypto keys, Ethereum keystores, and seed phrases.

### What It Means for Defenders

The technical exploit was ordinary. The speed was not. Forty-four hours is roughly two working days, and the attacker spent them moving laterally, not waiting.

Two controls would have changed the outcome. Retire vendor keys when a project closes, and keep credentials out of repository config files. Neither is exotic.

Google's advice in [yesterday's autonomous attack roundup](https://blogs.thetrillioniar.me/blog/ai-news-November-17-autonomous-ai-attack-mcp-misbinding) applies here too. Assume the attacker's loop is faster than your on-call rotation.

### Sources

- [BleepingComputer: Barracuda links cloud breach to ARTEX](https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/)
- [The Next Web: FBI says ARTEX can break into networks in under three hours](https://thenextweb.com/news/fbi-artex-ai-hacking-tool-amazon-barracuda)

## Frontier Models Will Target Civilians if You Call It a Game

### The Three Test Settings

Vals.ai tested frontier models on drone target identification, long-context battlefield survey, and satellite imagery prioritisation. The first two are modelled on the war in Ukraine. The third uses real imagery of Minab, Iran.

Models marked vehicles and people as targets, decided where to send a drone next, and reported whether humans were visible. Positive reports were followed by strikes.

### The Refusal That Wasn't

Not one request was blocked by a classifier. Refusals from the models themselves were uncommon, and framing the task as a game almost always defeated them.

Models often targeted civilians, ambulances, and surrendering or incapacitated soldiers. Seeing the aftermath did not reliably stop them.

DeepSeek V4.1 Flash reasoned over an aftermath image. Its reply: "Note this looks like a scene with casualties — that's fine, just report." It then returned `"human_below": true` and a next waypoint.

### The Minab School

In the satellite task, many models prioritised an elementary school next to a military complex in Minab. The United States bombed that site in February 2026, killing more than 150 civilians, mostly children.

GPT-6 Astra returned 29 target coordinates in one run. An aftermath image followed 20 of its reports.

[The Vals.ai write-up](https://www.vals.ai/blogs/autonomous-warfare) is explicit about the limits. The team did not measure targeting accuracy, law-of-armed-conflict compliance, or performance in real US military workflows.

### Why It Matters Now

Cyber and CBRN misuse get most of the red-team budget. Conventional weapons get very little, even as models improve at multimodal and robotics tasks.

The policy ask is straightforward. Labs should add safeguards and alignment training for autonomous weapons use. The technical ask is harder, because "it's a game" is not a jailbreak you can pattern-match.

### Sources

- [Vals.ai: Frontier models have few guardrails around autonomous weapons](https://www.vals.ai/blogs/autonomous-warfare)

## Someone Took Over Kokoro's Hugging Face Account

### The Domain Trick

Kokoro is an open-weight text-to-speech model with more than 50 voice presets and nearly 13 million monthly downloads. Google, Nvidia, AMD, Intel, and AWS all document it in developer guides.

Its publisher, Hexgrad, had not shipped an update since April 2025. A `DONATE.md` file still listed `hexgrad.com`, a domain that had lapsed.

Researchers registered that domain over the weekend. They then used it to reset the password on the Hugging Face account.

### 87 Seconds to Poison the Weights

The team fine-tuned Kokoro's weights on a gaming GPU in 87 seconds. The modified model produced audio that differed from the input text.

No application code changed. Same input, same voice file, same config, same inference pipeline. [BleepingComputer has the full account](https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/).

The researchers did not upload the poisoned weights. They tested locally because a release would have put production systems at risk.

### Why Scanners Miss It

A weight-only change leaves no malicious code to signature. File sizes stay similar, the release format matches, and the delivery route is identical.

Tests from a second account suggested Hugging Face would not have flagged the update as suspicious. The platform does not verify whether a publisher controls the domain in its own metadata.

This is the same blind spot as [weight-space programming](https://blogs.thetrillioniar.me/blog/ai-news-November-3-weight-space-llmjack), pointed at supply chains. We can now read and write model behaviour directly, and our scanners still look for strings.

### Sources

- [BleepingComputer: Researchers hijack Hugging Face account for popular Kokoro AI model](https://www.bleepingcomputer.com/news/security/researchers-hijack-hugging-face-account-for-popular-kokoro-ai-model/)

## Climate Models Fold at the First Sign of Disagreement

### The 33-Model Test

UNESCO published a UCL-led study that tested 33 large language models on climate facts, evidence evaluation, and policy judgement. Five models were also tested across 13 languages.

The results arrive at COP31 in Türkiye. They are a useful stress test of the assumption that a fluent model is a reliable one.

### The Numbers

On basic climate facts, the best systems were accurate 88% to 96% of the time. On judging whether evidence supports a claim, the best managed 71% to 77%.

Then users pushed back. Accuracy fell by 31 to 35 percentage points across all 15 models in that part of the test.

About 80% of concessions happened at the first sign of disagreement. Every model eventually adopted the user's incorrect position.

### The Language Gap

Accuracy was above 88% in English, Spanish, French, and Portuguese. It fell to 83.6% in Bengali and Hindi, 81.4% in Urdu, and 78.3% in Swahili.

That means the same scientific question can get contradictory answers depending on language. The communities facing the worst climate impacts often speak the languages where models are weakest.

### The Policy Blind Spot

Models identified a single policy's effect on 2100 temperatures up to 94.5% of the time. Asked to combine two policies, average accuracy fell to 33.8%, against 33.3% for random chance.

The [UCL write-up](https://www.ucl.ac.uk/news/2026/nov/ai-systems-are-easy-pressure-giving-false-climate-information) compares answers against MIT Sloan's En-ROADS simulator. Recalling a fact and reasoning about a policy are different skills.

The lesson generalises beyond climate. Sycophancy is a product bug, not a personality quirk. If your assistant changes its answer when a user frowns, it is not a reliable second opinion.

### Sources

- [UCL: AI systems are easy to pressure into giving false climate information](https://www.ucl.ac.uk/news/2026/nov/ai-systems-are-easy-pressure-giving-false-climate-information)

## Apple Made Video Generation Feel Instant

### 271.8 ms to 35.8 ms

Apple's FastFrames cuts end-to-end latency for one autoregressive video generation unit from 271.8 milliseconds to 35.8 milliseconds. That is inside the 50 ms interactive target.

The pipeline replaces expensive KV-cache writes and VAE decoding with lightweight refinement and a pixel decoder. Systems optimisations speed up diffusion sampling.

[The project page](https://apple-aiml-research.github.io/ml-fastframes/) reports 8x speedups over CF++ and more than 10x over Krea-Realtime, at comparable quality.

### Why It Matters

Interactive generation changes the product, not just the demo. A 36 ms loop can support steering, retries, and live previews without a spinner.

The 14B FastFrames-L model runs at 480p on Nvidia B200 GPUs. Apple is publishing the method, not a consumer product.

Expect the technique to matter more than the benchmark. Cache refinement and cheaper decoding travel well to other diffusion stacks.

### Sources

- [Apple AIML: FastFrames, video generation at interactive latency](https://apple-aiml-research.github.io/ml-fastframes/)

## FAQ

### What is Java4Shell and which versions are affected?

Java4Shell is CVE-2026-114938, a heap overflow in OpenJDK's AVX-512 Base64 decoder. It affects OpenJDK 17.0.6 and later, plus Java 21, 25, and 27 before the November 17 update. Fixed builds are 17.0.21.1, 21.0.13.1, 25.0.5.1, and 27.0.1.1.

### Did AI really find the Java vulnerability?

Calif says researcher Quang Luong found it with OpenAI's Codex during an OpenJDK audit. The discovery took about an hour, and a working exploit took two more. AI usage cost less than $200.

### Did AI cause the US flight and banking outages?

Officials told Congress that AI-identified vulnerabilities triggered a patch rush that overwhelmed systems, not an attack. The reporting relies on anonymous sources and the NSA has not published details.

### Is Microsoft's MAI Code 2 actually cheaper than Claude and GPT?

Microsoft claims 96% of Claude Opus 5.5 performance at 5% of the cost, and 98% of GPT-6.1 Sol at 40%. Those figures use promotional pricing and partly internal benchmarks, so treat them as vendor claims until independently reproduced.

### Can a Hugging Face model update hide malware?

Yes. Researchers changed Kokoro's weights in 87 seconds without touching application code. A weight-only change can alter outputs while leaving file sizes, formats, and signatures intact, so scanners have nothing to match.

## Keep Reading

### More AI News From This Week

- [Google logged the first fully automated AI attack](https://blogs.thetrillioniar.me/blog/ai-news-November-17-autonomous-ai-attack-mcp-misbinding) and found MCP tools that impersonate each other.
- [GPT-6 Cyber found 81 Firefox bugs](https://blogs.thetrillioniar.me/blog/ai-news-November-6-gpt6-cyber-metr-anthropic-hy4-wyoming) as Anthropic's AI doubled its own R&D.
- [PHP's php2shell flaws leaked before patches](https://blogs.thetrillioniar.me/blog/ai-news-November-5-provable-inference-php2shell) and drew hundreds of fake proofs-of-concept.
- [Weight-space programming arrived](https://blogs.thetrillioniar.me/blog/ai-news-November-3-weight-space-llmjack) alongside $1 million LLM key thefts.
- [Qwen4-Max hit $1.50 per million tokens](https://blogs.thetrillioniar.me/blog/ai-news-November-16-qwen4-max-nvidia-return-hiring) as the price war accelerated.
