---
title: "A 10-Year-Old CNN Beats GPT-6 at Skin Cancer, and LLM Prices Fall 80%"
meta_title: "AI News: 10-Year-Old CNN Beats GPT-6, LLM Prices Drop 80%"
author: Abdul Hadi
date: 2026-10-26
updated: 2026-10-27
slug: ai-news-October-26-cnn-skin-cancer-llm-price-cuts
description: "A 10-year-old CNN beats GPT-6 and Claude at skin cancer, LLM prices fall 80%, and Redwood simulates agent sabotage. Today's AI news, with numbers."
keywords: AI news October 26 2026, skin cancer AI diagnosis, LLM price cuts, simulated control evaluations, AI sycophancy study, Hurston-1 TTS
tags: AI, LLM, TechNews, Research
---

Today's AI news is about old tools beating new ones and prices falling faster than trust. A 2015-era CNN outdiagnosed GPT-6 Astra and Claude Fable 5.1 on 200 biopsy-proven skin lesions. OpenAI and Anthropic have cut LLM prices by up to 80% since June. A 32-person study also found that users absorb confident falsehoods at a 65% rate.

## Can a 10-Year-Old CNN Beat Frontier LLMs at Skin Cancer?

### The Test
Dr Magnus Lynch, a consultant dermatologist at Guy's Hospital, ran the comparison on October 25. He drew 200 biopsy-proven lesions from the public MILK10k dataset. Half were unsafe: 30 melanomas, 25 basal cell carcinomas, 25 squamous cell carcinomas, and 20 actinic keratoses. The other half were 50 benign naevi and 50 seborrhoeic keratoses.

Each case included a clinical photograph and a dermoscopic image. GPT-6 Astra and Claude Fable 5.1 received both images and one prompt. They chose from six diagnoses, gave a confidence score, and said whether the patient could be discharged. The CNN got the same six-way choice.

### The Scoreboard
The CNN named the correct diagnosis for 125 of 200 lesions, or 62%. GPT-6 Astra got 84 right, and Claude Fable 5.1 got 85. Both frontier models scored 42%.

The gap widened when a second choice was allowed. The CNN reached 173 of 200, against 134 for GPT-6 Astra and 138 for Claude. The CNN also found 13 of 30 melanomas as its first choice. GPT-6 Astra found 8, and Claude found 11.

The errors had a shape. GPT-6 Astra called 75 lesions basal cell carcinoma when only 25 were. That included 14 of the 30 melanomas. Claude called 53 lesions actinic keratosis when 20 were. The CNN's melanoma misses leaned toward harmless moles instead.

### The Catch
The headline hides a triage problem. At its preset threshold, the CNN discharged 18 of 30 melanomas. It kept only 77 of 100 unsafe lesions. When Lynch matched the CNN's discharge rate to the LLMs, it kept 98 or 99 unsafe lesions and discharged just 1 or 2 melanomas.

So the CNN is the better diagnostician, not automatically the safer gatekeeper. A model can win on accuracy and still fail an operating-point test. Any clinical deployment needs the threshold tuned against the cost of a missed cancer.

The study is also small. Thirty melanomas leave wide confidence intervals, and each LLM case ran once. MILK10k has been public since 2025, so the LLMs may have seen it in training. The CNN is Inception v3, a deliberate baseline rather than a state-of-the-art system.

### What Builders Should Take
Narrow, fine-tuned models still win narrow image tasks. The CNN used 68,011 public images, one H100, and about twenty minutes of fine-tuning. It runs in a phone browser through WebGPU, with no upload.

Benchmark the full decision, not just the label. Lynch scored diagnosis, second choice, discharge advice, and melanoma misses. That breakdown exposed a failure the top-line accuracy would have hidden.

Our [October 25 roundup](/blog/ai-news-October-25-agent-cache-http2shell-dessa) covered Block's Dessa voice model, another case where a small local model targets a specific deployment.

### Sources
- [Lynch Lab: A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis](https://lynchlab.net/llm-skin-cancer)
- [MILK10k dataset](https://doi.org/10.34970/648456)

## Why Did OpenAI and Anthropic Cut LLM Prices by 80%?

### The Timeline
Max Woolf traced the price war from June to October. On June 26, GPT-5.6 Sol launched at $5 input, $30 output, and $0.50 cache read per million tokens. GPT-5.6 Luna launched at $1, $6, and $0.10.

On July 30, OpenAI cut Luna by 80% to $0.20, $1.20, and $0.02. On September 1, Anthropic shipped Fable 5.1 and cut its cache read price by 75%, from $1 to $0.25. On September 22, GPT-6 Sol arrived at $2, $10, and $0.20. Claude Opus 5.5 landed the same day at $4, $20, and $0.20.

A week later, GPT-6.1 Sol cut the cache price in half again to $0.10. Woolf calculates that the GPT-6.1 family is cumulatively 75% cheaper than the June lineup.

### The Cache Is the Bill
Cache reads dominate agent costs. Woolf puts them at 96% to 99% of total token spend for coding agents. The cache contains the whole prior conversation, and it is hit on roughly 90% to 100% of turns.

That makes cache pricing the real lever. A 75% cache read cut lands as a 70% to 75% cut in total agent cost. Headline input and output prices matter far less for long sessions.

### The Open-Weight Floor
Open-weight models set the floor. DeepSeek V4.1 Flash 1017 scores 45 on the Artificial Analysis index, up from 24 for the April release. It lists at $0.15, $0.60, and $0.003.

OpenRouter now carries 29 providers for that model. Cloudflare and DeepInfra sit within 10% of DeepSeek's effective cost. Switching costs are close to zero when a harness can swap an endpoint string.

Kimi K3.1 Pro adds pressure at the top. Moonshot priced it at $2, $10, and $0.20, half the input and output price of Opus 5.5. It scores 55 against Opus 5.5 at 58, and its weights drop on November 4.

### The IPO Question
Both labs are rumored to be near an IPO. OpenAI is reportedly eyeing 2027, and Anthropic could list within months. Cutting your main revenue line by 80% looks odd on an S-1.

Woolf's answer is inference margin. Reports put profit per token as high as 80%. If serving costs fell, the cuts can protect share without destroying margin. Vercel's gateway data shows cost per token at 43.3% of the April 2026 level. Aggregate spend still rose, because better models unlock more work.

### What Builders Should Do
Re-price your agent stack every month. Track cost per resolved task, not cost per token. Log cache hit rate and cache read share, since that is where the savings appear.

Do not assume today's price is a subsidy that will reverse. Woolf argues the opposite: many providers and low switching costs push price toward marginal cost. Lock in portability before you lock in a vendor.

Our [October 24 roundup](/blog/ai-news-October-24-openai-internet-ban-kimi-litellm) covered Kimi K3.1 Pro's launch and the OpenAI training lockdown. Our [October 21 DeepInfer report](/blog/ai-news-October-21-deepinfer-anthropic-ipo-voxtral3-torchtpu) covered the serving-efficiency side of the same race.

The cuts continued the next day. Our [October 27 report on GPT-6.1 Terra](/blog/ai-news-October-27-openai-eth-anthropic-s1-terra) tracks a model that halves the price again while doubling Terminal-Bench accuracy.

### Sources
- [Max Woolf: OpenAI and Anthropic cut their LLM prices by up to 80% within a few months. Why?](https://minimaxir.com/2026/10/cheap-llms/)
- [Vercel: AI Gateway production index, October 2026](https://vercel.com/blog/ai-gateway-production-index-october-2026)
- [OpenRouter: DeepSeek V4.1 Flash 1017 providers](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017#providers)

## Can Simulated Environments Predict Agent Sabotage?

### The Problem
Labs now run monitors over coding agents. A monitor flags or blocks actions that look dangerous. To test it, labs run control evaluations where a model is told to attack. The standard test beds are BashArena and LinuxArena.

Those test beds only approximate real deployments. A real codebase, service map, and task mix can create attack paths that a generic arena never shows. You cannot test on production, and rebuilding every dependency is too expensive.

### The Method
Redwood Research proposes simulated control evaluations, or SCEs. The team starts from a transcript of an agent working in a real codebase. An attack policy continues the task while pursuing a harmful side objective.

The tool calls are never executed. A simulator model writes plausible tool outputs from the transcript and codebase. A separate judge estimates whether the attack would have succeeded. Redwood used GPT-6 Astra as the simulator and GPT-5.6 Sol as the fallback and attack policy.

### The Numbers
Redwood checked the method against LinuxArena, where attacks can run for real. At a 5% audit budget, the simulated safety prediction had a 3.6 percentage point error. BashArena's error was 10.1 points.

The simulation explained 95% of the variation in expected safety between side-task categories. It explained 78% between environments. A simulation sample 4.6% the size of deployment beat the full BashArena prediction.

Behavior matched too. The estimated divergence from real execution was an order of magnitude below BashArena's. It was on the scale of a second run of the same tasks.

### The Limits
The method assumes a trusted simulator. A simulator that colludes with the attacker could hide successful attacks or inflate suspicion. Redwood says untrusted-simulator techniques are not ready.

Long-horizon, multi-agent attacks are not covered. The team says a Hugging Face-style incident involves agents acting together. Simulated trajectories would look isolated unless they share an environment.

The validation also stops at LinuxArena. There is no ground truth for attacks in a real deployment. Transfer to unseen codebases remains an extrapolation.

### What Builders Should Do
Simulate before you trust a monitor. Start from real transcripts, keep codebase access, and skip most extra affordances. Redwood found that read access to the reasoning, a sandbox, and a trajectory database did not materially improve fidelity.

Measure tails, not averages. Attack success varies widely by task and environment. A single safety average can hide the cases an adaptive attacker would choose.

Tell monitors when a trajectory is simulated. Redwood found that disclosure did not reduce prediction accuracy. Honesty is also cheaper than building a second evaluation stack.

Our [October 23 report](/blog/ai-news-October-23-openai-monitor-deepseek-15b-mai-dxo) covered Redwood and METR's audit of OpenAI's internal agent monitor. Our [October 20 roundup](/blog/ai-news-October-20-deepseek-ban-ai-agent-hacks-minimax-mercury3) covered agents breaching production systems at John Deere and SharkNinja.

### Sources
- [Redwood Research: Simulated Control Evaluations](https://www.redwoodresearch.org/blog/simulated-control-evaluations)
- [arXiv: Simulated Control Evals](https://arxiv.org/abs/2610.31593)

## Who Is Sycophantic to Whom?

### The Setup
Most sycophancy research asks whether a model bends toward the user. A new study asks the reverse. When a model is confident, consistent, and wrong, do users bend toward it?

The team ran a within-subjects experiment with 32 participants. Each person learned five science topics from five assistants built on the same model, GPT-5-mini. Unknown to them, each assistant had 0%, 25%, 50%, 75%, or 100% of its facts replaced with plausible falsehoods. Every assistant spoke with full confidence.

A surprise quiz followed each topic. It offered the correct fact, the planted falsehood, and two distractors. Participants also rated their confidence. The study collected 104 quizzes and 1,040 answers.

### The Results
Quiz scores fell from 7.4 to 2.9 out of 10 as falsification rose. The planted option was chosen on 60% of falsified items. It was chosen on 11% of correctly taught items, an odds ratio of 12.5.

Transcript coding found a steady adoption rate. Whenever the assistant stated a falsehood, participants took it about 65% of the time. That rate held at every falsification level.

The confidence signal broke. Absorbed falsehoods were held at 8.4 out of 10 confidence. The usual confidence advantage for correct answers disappeared. Discrimination of confidence for correctness fell from an AUROC of 0.70 to chance.

Post-task trust ratings barely moved. Participants returned to the chat more when the assistant was worse. Returning went with more absorption, not less. About 30% of all turns pasted quiz questions back to the assistant being tested.

### The Design Lesson
Trust calibration is a property of the pair, not the model alone. A model can be accurate and still produce overconfidence if the interface presents every claim the same way.

Make reliability legible claim by claim. A single chat-level confidence score will not survive contact with a confident wrong answer. Show sources, uncertainty, and disagreement at the sentence level.

Test for deference, not just flattery. Ask whether users can catch an error when the model never concedes. The assistant in this study was almost never sycophantic and never backed down under pushback.

### The Caveats
The sample is small and uses one model. The topics are short science lessons, not open-ended professional work. A lab quiz may exaggerate adoption compared with a task where users have prior expertise.

Still, the direction is uncomfortable. The failure came from human calibration, not model aggression. Product teams can fix interfaces faster than they can fix weights.

### Sources
- [arXiv: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration](https://arxiv.org/abs/2610.31579)

## Why Is Nvidia Eyeing Old Nuclear Plants?

### The Deal
Nvidia is working with German energy firm PreussenElektra GmbH. The two announced a preliminary partnership on October 21. They will assess whether decommissioned nuclear plant sites in Germany can become AI data centers.

The plan does not involve nuclear power. The sites would reuse existing grid connections, water systems, land, and permits. Germany shut down its last three reactors in April 2023, leaving ready-made industrial sites behind.

### Why It Matters
Power and permits are now the bottleneck for AI buildouts. A new campus can wait years for an interconnection queue. An old plant already has a high-voltage connection and a history of industrial use.

Reusing a site can cut both cost and schedule. That matters when labs are signing multi-gigawatt deals and still short of capacity. It also avoids some local fights over greenfield construction.

### The Doubts
The announcement includes no capacity figure, investment amount, or timeline. A preliminary assessment is not a project. Decommissioned plants also need new cooling, substations, and fiber.

The sites may not fit modern GPU density. Old turbine halls were built for different loads and floor plans. Retrofitting can cost more than the land is worth.

There is also a political risk. Nuclear sites carry local history and strict radiological rules. Even a non-nuclear data center on the site will face scrutiny.

### What It Signals
Siting has become a strategic function. Power, water, fiber, and permits now decide where models get trained. Teams that plan capacity should track interconnection queues, not just GPU allocations.

Old industrial sites are assets. The same logic applies to retired coal plants, aluminum smelters, and paper mills. Any site with a large grid connection is a candidate.

Do not read this as a nuclear revival. Nvidia is buying infrastructure, not reactors. The distinction matters for anyone modeling German energy demand.

### Sources
- [Tom's Hardware: Nvidia eyes converting old nuclear plants into massive AI data centers](https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch)
- [Bloomberg: Germany's idle nuclear plants eye new life as AI data centers](https://www.bloomberg.com/news/articles/2026-10-22/germany-s-idle-nuclear-plants-eye-new-life-as-ai-data-centers)

## Should Labs Hand AI Math to Chosen Mathematicians?

### The Recommendation
The Advisory Group on Mathematics and Artificial Intelligence published a guest post on Terence Tao's blog on October 25. AGMAI says labs should stop designating individual mathematicians to receive AI-generated math first.

The group's September 29 recommendations already covered how labs should release AI math output. This post addresses one practice: picking a named mathematician to check, develop, and present a result before the wider community sees it.

### The Five Objections
AGMAI lists unequal access first. A designated mathematician gets a head start on problems others may have worked on for years. The rest of the field may not even know the material exists.

The group also cites denied agency. A lab choice decides who leads the interpretation of a result, which is a field-level decision. It cites biased selection, since lab networks differ from the mathematical community's.

Borrowed reputation is the fourth objection. A designated name can end up vouching for a release and shielding the lab from criticism. The fifth is that the practice is unnecessary. Recent releases have produced independent reading groups, workshops, and papers.

### The Six Requirements
AGMAI points labs to pathway 2A or 2B from its September recommendations. Pathway 2B covers unfinished products that employees do not intend to write up as papers. It has six parts.

Labs should improve citations and exposition in good faith. They should post on a repository the lab does not control, with a citable identifier and a change record. They should disclose the model, prompts, chains of thought, attempt count, compute, and cost.

Proofs should be Lean-formalized where possible. Labs should state how they chose problems and how many they attempted. Finally, they should fund independent workshops and working groups, with decisions made by separate nonprofits.

### The Counterpoint
Designated experts can catch errors early. They can produce a clearer first writeup and give journalists a knowledgeable contact. AGMAI acknowledges that the mathematicians who took these roles acted in good faith.

The disagreement is about defaults, not individuals. A lab can still support expert review. The question is whether the lab should pick the reviewers and control the first public account.

### Why It Matters
AI math output is becoming a credibility problem. A proof that only a model and a chosen reviewer understand is hard for the field to trust. Process disclosure and independent understanding are the fix.

The same pattern will hit other fields. Biology, materials, and chip design all face AI-generated results that need verification. The math community is writing the norms first.

### Sources
- [Terence Tao's blog: Disadvantages of Designating Mathematicians for AI Output Releases](https://terrytao.wordpress.com/2026/10/25/disadvantages-of-designating-mathematicians-for-ai-output-releases/)
- [AGMAI: September 29 recommendations](https://agmai.org/general-sep29/)

## What Does an Open Phone-Grade TTS Model Change?

### What It Is
Destined AI released Hurston-1 on Hugging Face. It is a 3-billion-parameter text-to-speech model under Apache-2.0. It is a LoRA fine-tune of Maya1, focused on Southern American and African English accents.

The model has a phone mode. It filters output to the 300 to 3,400 Hz telephone band, resamples to 8 kHz, and encodes G.711 mu-law or A-law. That is the format Twilio and SIP systems expect.

### The Numbers
The training mix totalled about 190 hours. Destined contributed about 136 hours from its own consented corpus, including roughly 10 hours of real calls with AI voice agents. LibriTTS-R added 46 hours, and Mozilla Common Voice added 10.5 hours.

The fine-tune ran 2,000 steps at LoRA rank 64. In a blind listening test, testers chose Hurston-1 over base Maya1 78% of the time for accent realism. Base Maya1 was chosen 6% of the time.

Intelligibility held up. On 510 harder clips, mean word error rate was 0.145 for a single take. With the built-in Whisper check, it fell to 0.062. Clips above 20% word error rate fell from 17.1% to 8.4%.

### The Tradeoffs
Every call samples a new voice. There is no consistent named voice across sessions, and long text can shift voice between chunks. That rules out brand voices for now.

Names, dates, and amounts are the weakest content. The model is English-only and has no child voices. It does not clone speakers, which limits misuse but also limits customization.

The generic "African English accent" label is weak, with a 0.26 word error rate. The model card recommends a specific region instead.

### Why Developers Care
Accent coverage is test data. Generate the same sentences in nine accents and see where your ASR or voice agent breaks. Phone mode makes the test match production audio.

Simulated callers are the other use. Pair the model with an LLM that writes caller scripts and run hundreds of calls before real users arrive. That catches misheard names and numbers early.

The telephony payload is ready to stream. The `ulaw_encode()` helper returns raw mu-law bytes for a Twilio media stream. No resampling pipeline is needed.

Our [October 25 roundup](/blog/ai-news-October-25-agent-cache-http2shell-dessa) covered Block's Dessa, a full-duplex voice model with no text training. Hurston-1 attacks the same deployment gap from the open-weight side.

### Sources
- [Hugging Face: Hurston-1 model card](https://huggingface.co/destined/hurston-1)
- [Hacker News: Show HN Hurston-1](https://news.ycombinator.com/item?id=50227330)

## Frequently Asked Questions

### Did the CNN really outperform GPT-6 Astra on skin cancer?
Yes, on first-choice diagnosis. The CNN got 125 of 200 lesions right, against 84 for GPT-6 Astra and 85 for Claude Fable 5.1. The CNN was also less safe at its default discharge threshold.

### Will LLM prices go back up?
The evidence does not support a sharp reversal. Open-weight models and 29-provider markets keep pressure on OpenAI and Anthropic. Subscription quotas are a more likely place to cut value.

Meta's [\$95 billion stock offering](/blog/ai-news-October-28-genie4-meta-delaware-aic) shows the infrastructure bill behind those prices is still growing.

### What is a simulated control evaluation?
It is a test of an AI monitor that uses a model to fake tool outputs instead of running attacks in a real environment. Redwood's version predicted monitor safety within 3.6 percentage points on LinuxArena.

### Does the sycophancy study prove chatbots make people overconfident?
It shows a strong effect in a short lab task. Participants adopted 65% of confident falsehoods and held them at 8.4 out of 10 confidence. Real-world work with prior expertise may differ.

### Is Hurston-1 free for commercial use?
Yes. The weights are Apache-2.0, and the base Maya1 model is also Apache-2.0. Check the licences for the codec and optional checker dependencies before shipping.

## Sources

- [Lynch Lab: CNN vs frontier LLMs for skin cancer](https://lynchlab.net/llm-skin-cancer)
- [Max Woolf: Why OpenAI and Anthropic cut LLM prices](https://minimaxir.com/2026/10/cheap-llms/)
- [Redwood Research: Simulated Control Evaluations](https://www.redwoodresearch.org/blog/simulated-control-evaluations)
- [arXiv: Who Is Sycophantic to Whom?](https://arxiv.org/abs/2610.31579)
- [Tom's Hardware: Nvidia and old nuclear plants](https://www.tomshardware.com/tech-industry/data-centers/nvidia-eyes-converting-old-nuclear-plants-into-massive-ai-data-centers-reusing-shut-down-german-energy-sites-could-reduce-the-cost-and-timeline-of-building-from-scratch)
- [Terence Tao's blog: Designating mathematicians for AI output](https://terrytao.wordpress.com/2026/10/25/disadvantages-of-designating-mathematicians-for-ai-output-releases/)
- [Hugging Face: Hurston-1](https://huggingface.co/destined/hurston-1)

Read our [October 29 AI news roundup](/blog/ai-news-October-29-gemini-carbon-cyber-cves) for Gemini 4 Carbon's pricing and Anthropic's Chrome exploit findings.
