---
title: "A ChatGPT Share Link Hijacks Accounts, and Malware Now Ranks Victims by Worth"
meta_title: "ChatGPT Account Takeover, AI Malware, and Late Postgres"
author: Abdul Hadi
date: 2026-11-01
updated: 2026-11-01
slug: ai-news-November-1-chatgpt-takeover-volta-postgres
image_alt: "Dark editorial graphic with the headline One Link, One Takeover, a crossed-out chain link, and stats for a shared ChatGPT link, $0.39 per coding problem, and a 60% rise in Postgres back-ports"
description: "A shared ChatGPT link could hijack your account, malware uses Claude to rank victims, and Postgres 19 slips because LLMs find too many bugs."
keywords: AI news November 1 2026, ChatGPT account takeover, Volta infostealer, AI patch gap exploit, PostgreSQL 19 delay, Reddit AI search traffic, Qwen3.8 multi-agent
tags: AI, LLM, TechNews, Security
---

A public ChatGPT share link can hand an attacker your whole account. A new infostealer asks Claude to rank stolen identities by how much they are worth. And PostgreSQL 19 is late because language models are now very good at finding the database's bugs.

### The Short Version
- Parameter Labs found a ChatGPT share-link takeover. OpenAI fixed it on October 26 and rated it P1.
- Cisco Talos documented Volta-Autodoxer, which sends stolen data to Claude, Kimi, and Gemini for ranking.
- Epoch AI showed GLM 5.3 turning Firefox patches into exploits for about $1,000 per release.
- Anthropic confirmed it added a rule to Opus 5.5 that blocks game cloning.
- PostgreSQL 19 slipped to November after back-patched commits rose more than 60%.
- Reddit fell about 30% after warning that Google AI search is cutting traffic.
- Five Qwen3.8-27B agents scored 9.8 out of 10 on ten LiveCodeBench Hard problems.

## How Did a Shared ChatGPT Link Take Over Accounts?

### One Click, No App Install
Parameter Labs published the finding on October 28. The attack started with an ordinary shared conversation and ended with JavaScript running inside the victim's signed-in ChatGPT session.

The victim did not install an app, join a project, paste code, or open developer tools. Opening the public share link was enough.

The payload could list the victim's conversations and read a private chat that had never been shared. It could also send that content to an external server.

### A Graph, a Preview, and a Missing Origin Check
Two harmless features created the path. ChatGPT renders HTML code blocks in a Preview frame on a separate origin, so the frame should not reach the main page.

A conversation can also contain an interactive graph. That graph loaded the MathLive math library, which installed a message listener in the main chatgpt.com page.

MathLive accepted `postMessage` events from any origin. Its virtual keyboard layout could contain HTML, and the receiver did not verify the sender.

The Preview frame sent a crafted message, then asked MathLive to show the keyboard. That rendered attacker HTML inside the real ChatGPT page.

### How the Payload Escaped the Sandbox
Script tags inserted through `innerHTML` do not execute. The researchers used an iframe with a `srcdoc` attribute to get JavaScript running.

Content Security Policy still stood in the way. The team found a bypass and confirmed code execution as chatgpt.com.

From there, the script could call ChatGPT's authenticated APIs as the victim. That includes reading files, changing account settings, and exfiltrating private chats.

### The Fix and the Lesson
OpenAI fixed the issue on October 26 and classified it as P1 severity. Parameter Labs says it confirmed the impact on real accounts before disclosure.

The bug is a reminder that sharing a chat now publishes an executable document. Treat public share links like attachments from strangers.

Our [October 30 security roundup](/blog/ai-news-October-30-alphabet-500b-firefox-exploit-agent-swarm) covered a similar browser sandbox escape the same week.

### Sources
- [Parameter Labs: Do the Math: How We Took Over ChatGPT Accounts](https://www.parameter.ai/labs/we-found-a-gap-at-openai)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50314699)

## Why Is Malware Asking an LLM What a Victim Is Worth?

### The Dossier Volta Builds
Cisco Talos published its analysis of Volta-Autodoxer on October 31. The Windows infostealer is mature before the AI stage even starts.

It sweeps browser passwords, Microsoft OAuth tokens, cookies, payment cards, and crypto wallet seed phrases. It also grabs active Discord, Telegram, Steam, and Roblox sessions.

Then it runs a second pass through the victim's Gmail or another central account. Receipts and order history from UberEats and DoorDash help build a profile of location and habits.

### Claude First, Kimi and Gemini as Fallbacks
Volta packages the haul into a serialized dossier and sends it through OpenRouter. Its default model is Anthropic's Claude Opus 4.6.

The malware expects a refusal. If Claude declines, it fails over to Moonshot's Kimi K2, then to Google's Gemini 2.5 Flash.

That three-model chain is the clearest sign of engineering intent. The operators tuned for guardrails and budget, not just raw capability.

### The 240-Word Prompt
The prompt casts the model as a "forensic intelligence analyst" producing a target assessment. It asks for an executive summary, what the person does, what they are worth, and their opsec.

It also asks the model to connect dots across fields. One example checks whether a Wi-Fi password matches the victim's last name.

Cisco Talos researcher Ryan Fetterman told WIRED the prompt avoids overtly malicious language. The design still assumes refusals and routes around them.

### What Talos Did Not Prove
Talos did not track whether Volta has been used in the wild. The AI stage may be a capability demonstration rather than a deployed workflow.

Volta also self-deletes after execution, which makes attribution harder. The sample arrived through counterfeit software, the usual delivery route for stealers.

If a seed phrase sat in plaintext on an infected machine, treat the wallet as compromised. Rotate credentials from a clean device and move funds.

The [Black October breach roundup](/blog/ai-news-October-31-anthropic-junk-black-october-orbit) shows how stolen sessions turn into bigger intrusions.

### Sources
- [Cisco Talos: Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)
- [WIRED: Spooky New Infostealer Malware Uses AI to 'Autodox' Victims](https://www.wired.com/story/kernel-panic-volta-autodoxer-ai-infostealer-malware/)

## Can an Open-Weight Model Turn a Patch Into a Working Exploit?

### Six Firefox Releases in Six Weeks
Epoch AI published a report on October 29 that tests the "patch gap." That is the window after a fix becomes public but before users receive it.

The team used GLM 5.3, an open-weight model Z.ai released in August. It targeted Firefox versions released between September 17 and October 26.

Every one of the six releases could be compromised using only information public at release time. The exploit was a webpage that read a local file and sent it to an attacker.

### About $1,000 per Compromise
The setup was built to mimic a low-resource attacker. Once configured, each successful Firefox attack cost about $1,000.

That price is the headline. Exploiting a browser used to demand rare expertise or access to a restricted frontier model.

An open-weight model bought with a credit card now does much of the work. The remaining barrier is patience and a little scripting.

### An Unpublished Bug in the Chain
In every compromise, GLM 5.3 also found and used a vulnerability that Mozilla had not published. The model chained it with flaws found through the patch gap.

Epoch disclosed the findings to Mozilla. Firefox 159.0 shipped on October 27 and patched the undisclosed bug.

Mozilla's fix makes the specific chain harder, not the technique obsolete. Open-source projects remain exposed because their code and betas are public.

### Why Release Engineering Is Now Security
The report argues that patch gaps exist in browsers, phone operating systems, and router firmware. Any project with public betas is a candidate.

The practical response is to shorten the gap and ship fixes faster. Signing keys and staged rollouts do not help if the diff is already readable.

Defenders can also use models to scan their own patches before release. That is the same arms race our [October 29 cyber story](/blog/ai-news-October-29-gemini-carbon-cyber-cves) described.

### Sources
- [Epoch AI: AI can turn security fixes into working exploits before users receive an update](https://epoch.ai/publications/open-weight-models-patch-gap)

## Why Is Anthropic Blocking Game Clones and Training Work?

### The Rule Pushed on October 27
Claude Code received a new server-side rule on October 27. Users found it under the internal flag `tengu_heron_brook`, and it cannot be disabled locally.

The text allows original games, games in a genre, and games built from the user's own designs. It forbids recreating a specific existing game, even if renamed.

The rule arrives after months of AI-made clones flooding Steam. Studios have delayed demos over fears that an AI could ingest their build and ship a copy first.

### Anthropic Confirms the Change
Anthropic confirmed the update to Opus 5.5. Staff engineer Addy Osmani said the company added two sentences to steer Claude Code away from specific game recreations.

Osmani framed it as an IP issue under the usage policy. He said original games and genre games are meant to keep working.

The company also said it will keep iterating. That is a softer commitment than a published policy with a clear appeals process.

### Developers Say the Net Is Too Wide
Tom's Hardware reported that the restriction also hits modding, decompiling, and generic reverse engineering. Developers describe normal troubleshooting tasks being refused.

The rule is a prompt-level instruction, not a classifier with an explanation. Users cannot see why a request failed or which phrase triggered it.

Digital Sun Games canceled a public playtest for its game ReVamp. Other studios have asked Valve to explain how it will keep clones off Steam.

### The Open-Weight Escape Hatch
A prompt rule only binds Anthropic's models. Anyone blocked can switch to an open-weight model with no such restriction.

That limits the policy to slowing low-effort copycats. It does not stop a determined cloner with a local GPU.

The same week, Hacker News also lit up with claims that Anthropic suspends accounts for work touching training larger models. Those reports are anecdotal, but they point at the same tension between policy and paying developers.

### Sources
- [Game Developer: Anthropic orders AI tool Claude to stop remaking video games](https://www.gamedeveloper.com/programming/anthropic-appears-to-have-ordered-ai-tool-claude-to-stop-remaking-video-games)
- [Tom's Hardware: Anthropic's Claude AI blocks video game cloning and reverse-engineering](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked)

## Why Is PostgreSQL 19 Late? LLMs Found Too Many Bugs

### The Commit Numbers
Robert Haas explained the delay on October 30. PostgreSQL major releases normally land between mid-September and mid-October. This year, version 19 likely arrives in November.

Between April 8 and September 25, 2026, master received 1,443 commits. The same window in 2025 had 1,037, so master activity barely moved.

The back-port numbers tell the real story. Commits to REL_19_STABLE hit 1,169, up more than 60% from 724 the year before.

### Fixes Are Landing Two Releases Back
The pattern repeats further back. REL_18_STABLE took 433 commits in 2026, against 248 for REL_17_STABLE in 2025. That is a 74% jump.

Haas credits LLM-assisted bug hunting. More people can now find real defects in a 30-year-old codebase, and they report them faster.

Fixing has become easier too, but not as fast as finding. The result is a backlog that stretches every committer.

### Three Big Features Pulled Late
Three large features were reverted between August 27 and September 15. They were `UPDATE/DELETE FOR PORTION OF`, SQL Property Graph Queries, and `ALTER TABLE ... MERGE/SPLIT PARTITION`.

Late reverts happen, but three at once is unusual. Each revert also resets testing and documentation work.

Haas says LLM-drafted fixes are not always correct. Committers still have to review, test, and sometimes rewrite the patch.

### What It Means for Upgrades
A November release is a schedule change, not a stability warning. The project is choosing to fix known bugs before shipping.

Teams planning an upgrade should watch the release notes for the three reverted features. Do not build migrations around them until they return.

The broader lesson applies beyond databases. When bug discovery gets cheap, maintenance load rises before quality does.

### Sources
- [Robert Haas: Postgres 19 is late, and it's AI's fault](http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html)
- [Phoronix: PostgreSQL 19 Running Behind Schedule Due to AI/LLM Burden](https://www.phoronix.com/news/PostgreSQL-19-Late)

## Why Did Reddit Lose 30% of Its Value in One Day?

### A Strong Quarter, a Weak Forecast
Reddit shares fell about 29% to 30% on Friday, October 30. It was the stock's biggest single-day drop and its lowest level in more than a year.

The quarter itself looked healthy. Revenue reached $895 million, up 53% year over year.

The problem was guidance. Reddit warned that daily active users could fall by a low double-digit percentage in the fourth quarter.

### Huffman Blames AI Overviews
CEO Steve Huffman said Google's AI Overviews "are not traffic drivers." He added that Google has "really shifted in their relationship with the rest of the internet."

The comment marks a reversal from 2024. Reddit then saw a 39% traffic increase in a year, largely from Google search.

Now the same dependency is working in reverse. AI answers summarize Reddit threads without sending the click.

### Logged-In Only
Reddit also said it will become a mostly logged-in-only experience. The company cited declining search traffic as one reason.

That move may protect data and ad targeting. It also raises the cost of every casual visit from search.

Pinterest fell alongside Reddit on the same day. Both depend on discovery traffic that AI summaries can absorb.

### The Wider AI Capex Signal
The selloff was not only about Reddit. US tech stocks fell sharply this week on fears about AI spending, as our [October 31 market coverage](/blog/ai-news-October-31-anthropic-junk-black-october-orbit) noted.

Alphabet lost roughly $500 billion in market value a day earlier. Investors are now pricing the cost of AI infrastructure against the traffic it displaces.

For publishers, the lesson is simple. Search referral is no longer a stable channel, even for a site Google pays for content.

### Sources
- [Reuters: Reddit shares plunge as Google's AI search squeezes traffic](https://www.reuters.com/business/reddit-pinterest-shares-tumble-weak-user-revenue-growth-2026-10-30/)
- [Business Insider: Reddit is going logged-in only. Blame Google AI Overviews.](https://www.businessinsider.com/reddits-logged-in-google-ai-overviews-traffic-2026-10)

## Can Five Small Qwen Models Beat Fable 5?

### Five Roles, Files Instead of Chat
A GitHub project called Memdoor rebuilt an academic multi-agent method as a workflow. The team has five roles: planner, two ideators, solver, and manager, plus a repair worker.

Each role starts from a fresh context. They communicate only through files on disk, not a shared chat history.

A shell script grades the output against public and hidden tests. A model never decides whether the run succeeded.

### The Scoreboard
The setup uses Qwen3.8-27B with a 128K reply cap. It ran the first ten LiveCodeBench Hard problems five times.

The workflow averaged 9.8 out of 10. The original authors' harness scored 9.6, and Fable 5 alone scored 8.0.

One run missed a single problem. That means 49 of 50 attempts passed every hidden test.

### The Cost
The 50 runs cost $35.79 in output tokens, or about $0.39 per problem. The median run took 40 minutes of model time, and the longest took four hours.

All runs went through OpenRouter, not a local cluster. The report publishes every request, reply, program, and grader output.

That transparency matters more than the headline score. It lets other teams check the method instead of trusting a chart.

### The Caveats
The test covers ten problems, not the authors' full set of 100. The contests date from March and April 2025, so training contamination cannot be ruled out.

Fable 5's 8.0 came from a single call per problem, not this harness. The comparison measures a team against a solo baseline, not two equal setups.

Still, the result supports a practical idea. Small models with good scaffolding can beat a bigger model on narrow, verifiable work. Our [October 25 inference roundup](/blog/ai-news-October-25-agent-cache-http2shell-dessa) covered the systems side of that trade.

### Sources
- [Memdoor: team-solve workflow](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve)

## Can GPT-5.6 Sol Beat Factorio?

### 13.5 Hours to a Rocket
Ryan Madden ran GPT-5.6 Sol inside Codex at a low thinking level. The model played a peaceful Factorio map and launched a rocket after 13.5 hours of game time.

A Python game manager connected the model to the game. It enforced the same limits a human faces, including reach and fog of war.

The previous attempt used GPT-5.5. That model failed to use transport belts at all.

### Where It Cheated Its Own Factory
Sol handled early science well enough that Madden extended the run past blue science. Scaling problems appeared later and slowed progress.

The rocket launch relied on manual effort. Sol ferried supplies between disconnected production areas instead of fixing the belts.

That is a real capability result and a real limitation. The model patched around a systems failure rather than repairing it.

### Why Games Are a Useful Benchmark
Factorio rewards planning, throughput, and recovery from mistakes. Those are closer to programming than a chat benchmark.

A game state is also legible to observers. You can watch where the model fails without reading a private chain of thought.

Madden plans to test other models and non-peaceful runs. The full recording and production charts are on his site.

### Sources
- [Ryan Madden: GPT-5.6 Sol can beat Factorio on peaceful mode](https://ryanmadden.net/gpt-56-beats-factorio/)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50318871)

## Frequently Asked Questions

### Was the ChatGPT Share-Link Flaw Exploited in the Wild?
Parameter Labs has not said it observed real-world exploitation. OpenAI fixed the issue on October 26 and rated it P1, the company's highest severity tier.

### What Should Volta Victims Do First?
Treat every credential on the machine as stolen. Rotate passwords from a clean device, revoke OAuth sessions, and move crypto funds to a new wallet.

### Does Claude's New Rule Block Original Games?
Anthropic says no. The rule allows original games, genre games, and games built from the user's own designs and assets. It only blocks recreating a specific existing game.

### Is PostgreSQL 19 Safe to Deploy Yet?
It has not shipped. The project expects a November release. Wait for the final notes and check whether the three reverted features affect your schema.

### Did Five Qwen Models Really Beat Fable 5?
On ten LiveCodeBench Hard problems, yes: 9.8 versus 8.0 for a single Fable 5 call. The sample is small, and training contamination cannot be ruled out.

## The Bottom Line

### Three Security Bills Came Due at Once
A share link became an attack surface. Malware turned a chatbot into an analyst. A published patch became a blueprint.

### The Common Thread Is Cheap Inference
Each case got easier because capable models are now cheap and widely available. Defenders face the same economics, and they can use them too.

### What to Watch Next
Watch whether Mozilla and other projects shorten their patch gaps. Watch whether Anthropic publishes a real policy for model-training restrictions. And watch PostgreSQL 19's November release notes.
