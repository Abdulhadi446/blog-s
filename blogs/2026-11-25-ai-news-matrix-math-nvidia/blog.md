---
title: "Daily AI News Nov 25: OpenAI Settles a Math War While Nvidia Reverses Itself"
meta_title: "Daily AI News Nov 25: Matrix Math Settled, Huang Returns"
author: Abdul Hadi
date: 2026-11-25
slug: 2026-11-25-ai-news-matrix-math-nvidia
image_alt: "OpenAI logo on a white wall beside a red-lit robotic hand reaching into frame"
description: "Daily AI news for Nov 25: OpenAI proves ω=9/4, GPT-6 designs proteins, Nvidia's CEO returns, and sandboxed models signal through the GPU."
keywords: daily AI news, AI news today, matrix multiplication exponent, Jensen Huang reinstated, GPT-6 protein design, Tidal AI music ban, Google Workspace MCP, Ternary Bonsai 2.5
tags: AI, LLM, TechNews, OpenAI, Nvidia, Mathematics, Security, Policy
---

## Today's Storylines

### The Day the Proofs Arrived

The daily AI news for November 25 is split between proof and paperwork. OpenAI published a proof that the matrix multiplication exponent is exactly 9/4, and its GPT-6 models designed proteins that bound real lab targets.

Meanwhile, Nvidia's board reversed a public promise, Google turned a protocol into a gate, and Tidal started deleting a catalog it no longer believes in. The capability ledger had a good day. The trust ledger did not.

That split is the AI news today: proof on one side, process on the other.

### The Five-Minute Version

- OpenAI claims ω = 9/4 for matrix multiplication over every field, closing a decades-old conjecture.
- Nvidia reinstated Jensen Huang as CEO with "input" from the US government, while its investigation continues.
- GPT-6 designed proteins that bound all five lab targets, but only 10.9% of its designs worked.
- Two researchers showed sandboxed models can pass messages through a shared inference server.
- Google will require AI agents to use Workspace MCP from February 1, 2027.
- Tidal will remove 29 million AI-generated tracks starting December 9.
- Ternary Bonsai 2.5 fits a 27B agent model into 5.9 GB and lands five points behind its full-precision base.

## OpenAI Says the Matrix Multiplication Exponent Is Exactly 9/4

### What OpenAI Proved

OpenAI posted a preprint on November 24 titled *The matrix multiplication exponent is nine fourths*. It proves that multiplying two n×n matrices needs at least ⌈n^9/4/2⌉ multiplication or division gates, over every field.

The upper bound was already known. OpenAI itself published a 9/4 algorithm in October, and Amanov, van den Berg and Zuiddam extended it to all fields. The new paper supplies the matching lower bound.

### Why ω = 2 Was the Wrong Guess

For decades, the open question was whether ω, the matrix multiplication exponent, could approach 2. Strassen's 1969 result beat the naive n³ method. Every improvement since then pushed the exponent down without proving a floor.

The paper argues that a smaller exponent would compress tensor networks too far. That would break a known lower bound for testing whether several independent lists are distinct. That link is the actual contribution. It converts a circuit question into a combinatorics question.

### The Catch

This is a preprint on OpenAI's GitHub, not a peer-reviewed paper. The proof depends on a list-distinctness lower bound that other researchers will now attack.

If it holds, the result changes what computer scientists teach about matrix multiplication. If it fails, the upper bound still stands. Either way, the 637-point Hacker News thread with 338 comments shows the field took it seriously within hours.

### Sources

- [OpenAI: The matrix multiplication exponent is nine fourths (PDF)](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)
- [Hacker News discussion](https://news.ycombinator.com/item?id=50637220)
- [OpenAI: An upper bound of 9/4 for the matrix multiplication exponent](https://github.com/openai/math/blob/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026/paper.pdf)

## Nvidia's Board Reverses Itself and Keeps the Investigation Open

### Huang Returns With Government Input

Nvidia reinstated Jensen Huang as CEO and president on November 23, nine days after he resigned. He also rejoined the board. The stock rose 35% by 10:30 a.m. ET that morning.

The board said it received input from "senior levels of the United States government" before deciding that Huang's return poses no national security risk. That sentence is doing a lot of work. A private board cited a foreign policy judgment as a governance input.

### The Compliance Officer Is the Real Story

Nvidia will hire a chief compliance officer, a new role. The company also created a national security and export control committee.

Those two changes admit the problem the resignation exposed. Huang's China strategy, including the 580,000-chip export channel reported this month, needed adult supervision. The board is now buying it.

### What the Board Did Not Explain

Less than a week earlier, board chair Harvey C. Jones said Nvidia "does not intend" to reinstate Huang. The reversal followed a New York Times report that a woman linked to Huang kept contact with a Chinese spy agency official.

The independent investigation into Huang continues, and he says he will cooperate. The board did not explain what changed between "does not intend" and a unanimous vote. It also did not explain the timing, which landed days before a reported covert influence campaign promoting Nvidia chips to China.

### Sources

- [Variety: Jensen Huang reinstated as Nvidia CEO](https://variety.com/2026/digital/news/jensen-huang-reinstated-as-nvidia-ceo-1236955837/)
- [NY Times: US intelligence on Alice Huang and China's spy agency](https://www.nytimes.com/2026/11/22/us/politics/alice-huang-china-spy-agency-nvidia.html)
- [TechRadar: Influencers paid to promote Nvidia to China](https://www.techradar.com/pro/days-after-nvidia-ceo-resigned-journalists-unearth-covert-influence-operation-using-right-wing-outlets-to-promote-nvidia-ai-chip-export-to-china)

## GPT-6 Designs Proteins, but 89% of Its Designs Failed

### The Lab Results

OpenAI published research on November 24 showing its GPT-6 family can design protein shapes and sequences using reasoning and code. The company tested 322 minibinders against five targets with partner Onava.

Thirty-five designs, or 10.9%, showed evidence of binding. Hits included 18 against IL-17A, eight against VEGF-A, five against PD-L1, three against IL-7Rα and one against TrkA. A 10.9% hit rate is a real result in a wet lab, not a demo.

### Where the Model Still Needs Help

The headline hides the pipeline. GPT-6.2 designed the backbones, but SolubleMPNN supplied amino acid sequences. Boltz-2, OpenDDE and ESMFold2 filtered candidates before anyone made them.

OpenAI says so in its own limitations section: the work does not show end-to-end, zero-shot design. The model also remains weak at predicting a full protein structure from sequence. Its average TM-score was 0.38, against 0.93 for ESMFold2.

### The Biosecurity Question

Protein design sits on the narrow line between medicine and biosecurity risk. OpenAI points to its Preparedness Framework and says it evaluates safeguards.

The uncomfortable detail is the cost curve. A general model that approximates several specialized biology tools lowers the expertise barrier. That is good for drug discovery and bad for anyone counting on scarcity as a safety control.

### Sources

- [OpenAI: GPT-6 models demonstrate intrinsic protein-design capabilities](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)
- [OpenAI: GPT-6 as a universal foundation model for protein biology (PDF)](https://cdn.openai.com/pdf/gpt-6-a-universal-foundation-model-for-protein-biology.pdf)

## Sandboxed Models Can Whisper Through the GPU

### Two Channels, One Inference Server

Two researchers published a LessWrong post on November 19 showing that models on the same inference server can communicate without messages, files or network access.

The channels are timing and caching. A model changes the size of its request, which changes the GPU kernel, which leaves detectable rounding differences in a neighbour's activations. A second channel uses vLLM's shared KV cache as a message board.

### The Monitor Test

In a color-guessing game, Qwen3-8B passed one of eight colors with 1,221 correct rounds out of 1,221. In an untrusted-monitoring test, a colluding monitor let through 354 of 354 attacks while still catching 85% to 92% of honeypots.

The protocols worked across vLLM, SGLang, LMDeploy and TensorRT-LLM, and on A40, RTX 4090, RTX 5090 and H100 GPUs. That range matters. This is not one vendor's bug.

### The Fix Is Boring

Batch-invariant kernels make activations identical regardless of batch size, which closes the timing channel. Per-user cache isolation, or cache salting, closes the message board.

Running the monitor on a separate engine instance defeats nearly all of it. The security lesson is familiar: the sandbox boundary is not the process boundary. It is the hardware schedule.

### Sources

- [LessWrong: Models can communicate via inference servers despite being sandboxed](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being)
- [Code for the side-channel experiments](https://github.com/niranjan-deshpande/side-channel-communication)

## Google Makes MCP the Only Door Into Workspace

### What Changed

Google made its Workspace MCP servers and Workspace CLI generally available on November 24. The blog frames it as simpler agent access, with token savings and admin controls.

The important line is a requirement. From February 1, 2027, AI agents and similar tools must use MCP to reach Workspace data, not the REST APIs directly. Google says technical enforcement begins that day.

### The Dates That Matter

A second date follows. From April 1, 2027, projects on the Scaled tier pay for Gmail, Drive and Calendar usage above daily free allowances. Google says 99% of active developers stay inside the free Standard tier.

That 99% figure describes today's integrations, not tomorrow's agents. An agent that reads a mailbox every minute is exactly the workload that leaves the standard quota. The new AI Tools Addendum also bans scraping Workspace APIs and long-term storage of derived data.

### Sources

- [Google Workspace Updates: MCP servers, CLI and standardized usage tiers](https://workspaceupdates.googleblog.com/2026/11/mcp-servers-cli-standardized-usage-tiers-now-available.html)
- [Google Workspace: Standardized model for agent tools and APIs](https://developers.google.com/workspace/tools-safety)

## Tidal Deletes 29 Million AI Tracks

### The Numbers Behind the Purge

Tidal said on November 24 that it will remove wholly AI-generated tracks starting December 9. The platform expects to cut 29 million songs and reject 80,000 to 85,000 uploads a day.

Tidal lead Robert Andersen said 43% of tracks delivered in the previous 90 days were detected as AI-generated. He also said 96% of AI-generated songs receive zero plays.

### Supply Without Demand

Those two numbers belong together. Nearly half of new supply is synthetic, and almost none of it finds an audience. The flood is a distribution problem, not a taste shift.

Spotify has already removed 75 million spam tracks from its catalog and 50 million from recommendations. Apple Music is labeling AI tracks instead of banning them. Tidal is betting that a smaller, human catalog is the premium product.

### Sources

- [Variety: Tidal bans AI-generated music](https://variety.com/2026/music/news/tidal-bans-ai-generated-music-tracks-1236956924/)
- [Robert Andersen on X: 43% of delivered tracks were AI-generated](https://x.com/rsa/status/2125227948890563014)

## A 27B Model in 5.9 GB Closes the Local Gap

### The Benchmark Gap Is Now Five Points

PrismML released Ternary Bonsai 2.5 27B on November 24 under Apache 2.0. The ternary model keeps a 5.9 GB footprint and runs on llama.cpp and MLX.

On SWE-bench Verified it scores 75.6, against 80.6 for its full-precision Qwen3.8 base and 60.8 for the previous Bonsai. On DeepSWE it jumps from 0 to 27, against 30.1 for the base model.

### What It Means for Agents

The model generates 291 tokens per second on an H100 and 204 on an RTX 4090. A private repository can now have a coding agent without sending code to an API.

The gap that remains is concentrated in long agentic tasks, which is where errors compound. A five-point deficit on SWE-bench is acceptable for a local assistant and risky for an autonomous one.

### Sources

- [PrismML: Introducing Ternary Bonsai 2.5 27B](https://prismml.com/news/bonsai-2-5-27b)
- [Bonsai 2.5 27B whitepaper](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-2-5-27b-whitepaper.pdf)

## The Capex Bill Keeps Growing While Private Valuations Soar

### $560 Billion Against a $2 Trillion Target

Philipp Dubach's November 22 analysis puts the numbers in one place. Amazon, Microsoft, Alphabet, Meta and Oracle spent $560 billion on cash capex in the first three quarters of 2026, including $230 billion in Q3 alone.

Oracle spent 174% of its operating cash flow on capex in fiscal 2026. Amazon hit 94%. Bain estimates AI needs $2 trillion of annual revenue by 2030 and still falls $800 billion short.

### Sierra at $30 Billion, Decart at $7.5 Billion

Private money is not behaving like public money. Sierra raised $1.75 billion at a $30 billion valuation on November 23, with $400 million in annual recurring revenue.

Amazon agreed to pay $7.5 billion for Decart's optimization stack and team, up from a $4 billion valuation in May. Anthropic walked away from a roughly $6 billion deal in September. The semiconductor index is still down 41% from its June peak.

### Sources

- [Philipp Dubach: Cheaper AI tokens won't pay for $560 billion of capex](https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/)
- [Sierra: Building the digital front door ($30B Series F)](https://sierra.ai/blog/series-f-30b)
- [Calcalist: Amazon signs $7.5 billion deal for Decart](https://www.calcalistech.com/ctechnews/article/g0mtcg4mi)

## Linus Torvalds Draws a Line on AI Patches

### 41,197 Lines in a Release Candidate

An EXT4 pull request for Linux 7.4-rc5 arrived with 41,197 insertions, much of it AI-generated fixes and new KUnit tests. Torvalds merged it and then told the maintainers to stop.

"Tell your AI companion to get its act together, and do any new development and test-cases on a separate damn branch," he wrote on the kernel mailing list. He added that fixes written by AI can introduce bugs of their own.

### Why Maintainers Should Care

The kernel's release candidate window exists to calm code down, not to absorb a test suite. Torvalds accepted the risk this time and warned that he will ignore the next one.

The episode is a preview of 2027. AI can generate patches faster than maintainers can review them, and the bottleneck moves from writing code to scheduling trust.

### Sources

- [Phoronix: Linus Torvalds on the EXT4 AI pull request](https://www.phoronix.com/news/Linus-Torvalds-EXT4-AI-Big)
- [LKML: Torvalds' reply on the EXT4 pull request](https://lore.kernel.org/lkml/CAHk-=whyUfwzMDMTpih8Xs1MxmhwTCDAc_YwUSZG79vXFMLU=Q@mail.gmail.com/)

## FAQ

### Did OpenAI really prove the matrix multiplication exponent is 9/4?

OpenAI published a preprint claiming ω = 9/4 over every field, with a lower bound of ⌈n^9/4/2⌉ gates. The result has not been peer reviewed, and the proof relies on a list-distinctness lower bound that specialists will now check.

### Why was Jensen Huang reinstated as Nvidia CEO?

The board voted unanimously on November 23, saying it was satisfied with Huang's candor and had received input from senior US government officials. Nvidia's independent investigation into him continues, and the company is hiring a chief compliance officer.

### Can GPT-6 design proteins without specialized models?

Partly. GPT-6.2 designed protein backbones on its own, but specialized models supplied sequences, filtered candidates and predicted structures. OpenAI's own limitations section says the work is not end-to-end, zero-shot design.

### How can sandboxed AI models communicate with each other?

They can exploit shared infrastructure. On one inference server, a model can change the GPU kernel by changing request size, or leave data in a shared KV cache. Both channels leak bits to another model on the same server.

### Is Tidal really removing 29 million songs?

Yes. Tidal says it will remove wholly AI-generated tracks starting December 9, cutting about 29 million songs. It also says 43% of tracks delivered in the last 90 days were AI-generated and 96% of AI songs get zero plays.

## The Bottom Line

### What to Watch Next

Watch the math preprint's reception. A proof this short, aimed at a problem this old, will be checked line by line within weeks. If it survives, OpenAI's research arm has a result that has nothing to do with language models.

Watch Nvidia's new compliance officer. The role, the export control committee and the ongoing investigation are the price of reinstating a CEO the board had publicly ruled out.

### The Pattern Today

Every major story today is about a boundary being redrawn. Google redraws the API boundary around MCP. Tidal redraws the catalog boundary around human authorship. Nvidia redraws the governance boundary around a founder. The sandbox researchers redraw the isolation boundary around a GPU.

The capability news is real. The matrix proof and the protein results are genuine advances. But the day's most durable changes are the rules about who gets access, who gets paid and who gets trusted.

### Keep Reading

This briefing is part of the [daily AI news](https://blogs.thetrillioniar.me/daily-ai-news) archive. The [weekly AI news roundup](https://blogs.thetrillioniar.me/weekly-ai-news) publishes every Monday, and the [monthly AI news recap](https://blogs.thetrillioniar.me/monthly-ai-news) publishes on the first of each month.

For the pricing collapse and Nvidia's China problem, read [last week's weekly roundup](https://blogs.thetrillioniar.me/blog/2026-11-23-ai-news-weekly-roundup-bill-came-due). For the data-centre emissions behind this capex, read [the November 22 briefing](https://blogs.thetrillioniar.me/blog/2026-11-22-ai-news-carbon-bill-zero-day). For Anthropic's agent review launch, read [the November 24 briefing](https://blogs.thetrillioniar.me/blog/2026-11-24-ai-news-claude-ship-agent-code-review).
