---
title: "Nvidia's Scarcity Machine, a Wallet for AI Agents, and the Theorems Hiding in Gödel's Notebooks"
meta_title: "AI News Nov 14: Nvidia Scarcity, ChatGPT Wallet, Gödel"
author: Abdul Hadi
date: 2026-11-14
updated: 2026-11-14
slug: ai-news-November-14-nvidia-scarcity-chatgpt-wallet-godel
image_alt: "Rows of NVIDIA data-center GPUs mounted in a black server chassis on a trade show floor"
description: "Nvidia allegedly funded AI startups to buy its own GPUs, ChatGPT Wallet lets agents check out, and Claude read 1,009 pages of Gödel's notebooks."
keywords: AI news November 14 2026, Nvidia GPU scarcity, ChatGPT Wallet, OpenAI robotics team, Gödel notebooks Claude, FAA SMART AI, MathHelm, llama.cpp v1.0, 4-bit training
tags: AI, LLM, TechNews, Nvidia, OpenAI, Anthropic, Google, Research
---

## Today's Storylines

### A Day of Machines Paying, Reading, and Flying

Nvidia faced a report that it funded the demand for its own chips. OpenAI put a wallet inside ChatGPT and folded its robotics team into general research. Anthropic's Claude read decades of hidden mathematics, while the FAA took an AI adviser nationwide.

### The Five-Minute Version

- The Wall Street Journal alleged Nvidia invested in AI startups that bought Nvidia GPUs.
- The report says CFO Colette Kress wanted to scale back a $250 billion OpenAI deal.
- OpenAI disbanded its stand-alone robotics team and moved researchers under Mark Chen and Greg Brockman.
- OpenAI launched ChatGPT Wallet for U.S. Pro users, letting its "dots" complete purchases.
- Claude produced a digest of 1,009 pages of Gödel's shorthand in about two days.
- The FAA expanded its $875 million SMART tool to all 22 air route traffic control centers.
- Mathematicians launched MathHelm to discuss 722 OpenAI-generated manuscripts.
- llama.cpp and ggml both hit v1.0.0 after three and a half years.
- Thinking Machines trained Inkling 2 Small end to end with a native 4-bit forward pass.

## Nvidia Reportedly Funded the Demand It Was Selling Into

### What the Wall Street Journal Alleges

The Wall Street Journal reported on November 13 that Nvidia invested in small AI cloud providers that then bought Nvidia GPUs. The alleged goal was to keep demand looking strong and to move an oversupply of chips from TSMC. TechPowerUp summarized the report, which cites an August meeting between former CEO Jensen Huang and his finance team.

### The $250 Billion Argument

At that meeting, CFO and acting CEO Colette Kress pushed to reduce circular financing agreements. She also wanted to scale back Nvidia's $250 billion deal with OpenAI. Huang allegedly called her a "deer in the headlights" and pushed further investment into small cloud providers. Kress warned that those providers could not afford the GPUs anyway.

### Why "Circular Financing" Is the Right Worry

Circular financing means a vendor invests in a customer, and the customer spends that money with the vendor. The revenue is real, but it is not independent demand. Nvidia was reportedly facing an "avalanche" of GPUs from TSMC with no immediate buyers. That is a demand-quality problem, not just a marketing story.

### What the Report Does Not Prove

The summary does not describe accounting fraud. Vendor financing is legal and common in hardware. What it questions is the quality of Nvidia's backlog if the company helped create the buyers. The TechPowerUp summary does not include a response from Nvidia. The allegation lands two days after Huang's resignation, which [staff are still protesting](/blog/ai-news-November-13-nvidia-petition-tsmc-breach-amd-port).

### The Week That Made This Credible

Huang left on November 12 after affair allegations and a board investigation. The [board's decision](/blog/ai-news-November-12-nvidia-oust-anthropic-alarm-gemini-decisions) cost Nvidia about $1 trillion in market value. Lawmakers and the FBI have opened investigations, according to WIRED. A demand-inflation story fits the mood better than it would have a month ago.

**Sources:** [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus)

## OpenAI Disbands Its Stand-Alone Robotics Team

### The Reorganization, in Plain Terms

OpenAI disbanded its stand-alone robotics team and reassigned the researchers. The research staff now reports to Chief Research Officer Mark Chen. The applied robotics and hardware teams moved into the Applied organization under President Greg Brockman. OpenAI told Fortune the change accelerates robotics work rather than ending it.

### An Empty Booth at CoRL

The timing was awkward. OpenAI had registered booth 208 at CoRL, a major robotics conference in Austin this week. Fortune visited the booth and found it empty, with no OpenAI logo in sight. The conference app still listed the company. A reorganization is easy to announce and harder to hide at a trade show.

### Why General Models Might Drive Robots

OpenAI is betting that models trained on language, code, and vision can also control physical machines. That would remove the need for a separate robotics model team. Fortune reports that researchers connected GPT-6 Astra to robots and saw surprising performance. The [GPT-6 rollout](/blog/ai-news-October-08-gpt6-haiku5-5-math) already hinted that the model was built for more than chat.

### The 2027 Humanoid Deadline

This is OpenAI's third robotics phase. It wound down an early team in 2020, citing limited robot data. It rebuilt a team in 2024 and partnered with Figure, but that deal ended in February 2025. CEO Sam Altman now targets a first public humanoid demonstration in 2027. Centralizing the team is a bet that general models can beat specialized robot stacks before that deadline.

**Sources:** [Fortune](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/)

## ChatGPT Wallet Lets AI Agents Shop and Check Out

### Who Gets It First

OpenAI launched ChatGPT Wallet on Friday, November 13. It is limited to a small group of U.S. ChatGPT Pro subscribers aged 18 and over. Users need a U.S.-issued Visa, Mastercard, or American Express card. The feature lets OpenAI's agents, called "dots," help users decide what to buy and then pay for it.

### How the Payment Actually Works

Users add a card to the wallet once. At checkout, OpenAI charges a payment token instead of the real card number. The dot sends the merchant the shipping address and contact details. The user reviews the item, total, and card before approving with Face ID or a fingerprint. Credit card rewards and dispute protections still apply.

### The Retailer Resistance

Amazon blocks AI agents from shopping on its site and pushes users toward Alexa. DoorDash and Uber have reported low numbers of agent-placed orders. Meta's Muse, with more than 10 million users, says AI-assisted shopping is a top activity. OpenAI also published a Commerce Partner Playbook for retailers that want to support agent checkout.

### What Could Go Wrong

An agent that can pay is an agent that can be tricked into paying. Prompt injection, stale prices, and wrong-item orders are all live risks. The biometric approval step limits silent purchases for now. OpenAI says future versions will add spending limits and category or time-based controls. That is when the real liability questions begin.

**Sources:** [TechCrunch](https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/), [OpenAI](https://openai.com/index/introducing-chatgpt-wallet/)

## Claude Read 1,009 Pages of Gödel's Shorthand

### A Page a Week Became Two Days

Kurt Gödel left 16 notebooks from the early 1940s, totaling 1,009 pages of dense mathematics. Much of it is written in Gabelsberger shorthand, which was obsolete even then. Jan von Plato's team at Helsinki University had worked through it at about a page a week since 2017. In September, von Plato gave the material to Claude.

### Hundreds of Theorems Nobody Catalogued

Within a couple of days, Claude produced a comprehensive digest of the whole collection. Von Plato told the Guardian he was "flabbergasted." He says the notebooks contain hundreds of proved theorems. They also hold dozens of anticipations of results from the 1970s and 1980s, plus 14 themes in logic nobody pursued. Gödel had fled Austria in 1940 and spent the rest of his career at Princeton.

### The Verification Problem

A digest is not a proof. The Guardian's report relies on von Plato's assessment, and the notebooks remain the primary source. Claude compressed a century of difficult shorthand into a map. Historians still have to check every claim against the page. That is the correct division of labor: the model finds the signal, the humans certify it.

### Why This Is the Best Version of AI Scholarship

This is not a model inventing a theorem. It is a model reading something humans could not read quickly. The gain is access, not authority. It also connects to OpenAI's [October claim](/blog/ai-news-October-27-openai-eth-anthropic-s1-terra) that its model helped disprove a landmark conjecture. In both cases, the useful output is a lead for experts.

**Sources:** [The Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

## The FAA Takes Its AI Adviser to All 22 Centers

### 180 Flights and 80 Gallons

The FAA expanded its SMART system from the Washington, D.C. region to all 22 air route traffic control centers. SMART is a cloud tool that combines weather, flight paths, traffic flow, and controller staffing data. It suggests routes and arrival orders. The agency says it helped reroute 180 flights since September 21, saving about 10 minutes and 80 gallons of fuel per flight. The system cost $875 million.

### Humans Still Validate the Advice

FAA specialists in Washington review every SMART recommendation before sending it to local facilities. Controllers can decline the advice. The FAA says the tool cannot replace controllers or take over an aircraft. That is a sensible guardrail. It is also a reminder that the system is advisory, not autonomous.

### The Union Says It Was Left Out

The National Air Traffic Controllers Association represents more than 15,000 members. It told Flying magazine that it was not involved in the design, testing, or implementation of SMART. The union said it therefore cannot speak to the tool's effect on the workforce. Airline CEOs Ed Bastian and Robert Isom praised the rollout. The people who would use it daily were not at the table.

### A Ground Stop in the Same Week

On November 13, the FAA ordered a nationwide ground stop that lasted about four and a half hours. The agency attributed it to communications problems, not to SMART. The Atlantic noted that many Americans blamed AI anyway. That reaction is the real adoption problem. Automation advice and automated blame arrive together.

**Sources:** [Ars Technica](https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/), [NBC News](https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247)

## MathHelm Gives AI-Generated Papers a Public Lab

### 722 Manuscripts and No Verdict

On October 6, OpenAI released 722 mathematical manuscripts generated by an internal AI model. Most were not verified by humans, and many lacked Lean proofs. On November 13, a group of mathematicians launched MathHelm. The forum is for discussing those papers and any similar AI-generated work. It was announced in a guest post on Terence Tao's blog.

### The Rules of the Forum

Researchers register under their real names and discuss in English. Comments can address correctness, readability, originality, or a single step in a proof. Users can upload PDF notes. The forum is nonprofit and takes no position for or against AI. Its policy prohibits organizations from using forum content to train models.

### The Committee Behind It

The scientific committee includes Xinyi Yuan of Peking University as chair. It also includes Yi Ni of Caltech and Xiaoming Sun of the Chinese Academy of Sciences. Liang Xiao of Peking University, Yuan Yuan of Westlake University, Ruixiang Zhang of UC Berkeley, and Fan Zheng of ICMAT-CSIC complete the group. That is a credible roster for a difficult job.

### Why This Beats Both Cheerleading and Boycotts

Mathematicians have no obligation to check AI-generated papers. MathHelm's insight is that small comments still help. A question about one proof step can save the next reader hours. Distributed review is the only realistic response to 722 papers. The alternative is either blind trust or a blanket refusal to look.

**Sources:** [Terence Tao's blog](https://terrytao.wordpress.com/2026/11/13/introducing-mathhelm-a-place-to-discuss-ai-generated-papers/), [MathHelm](https://mathhelm.org/)

## llama.cpp Reaches 1.0

### What Actually Changed

The llama.cpp and ggml projects released v1.0.0 on November 13. The release comes three and a half years after the project began. From now on, both libraries follow semantic versioning. A breaking change to the public C API bumps the major version. New model support and backends bump the minor version. Bug fixes bump the patch version.

### 150 Architectures and a CI Bill

llama.cpp supports more than 150 model architecture variants and all mainstream speculative decoding methods. Its ggml backends compile as dynamic libraries and can load at runtime. The project tests across hardware from NVIDIA, AMD, Qualcomm, Arm, IBM, and Intel. It uses Hugging Face Buckets and HF Jobs to scale continuous integration. Prebuilt packages cover Linux, macOS, Windows, Android, iOS, Docker, Homebrew, conda-forge, MacPorts, and Winget.

### Why Semver Matters for Local AI

Local inference used to be a demo. It is now a dependency inside desktop apps, servers, and agents. Downstream developers need to know when an update will break their build. A stable public header and a clear version policy are boring infrastructure. Boring infrastructure is how a project becomes a platform.

**Sources:** [Hugging Face blog](https://huggingface.co/blog/ggml-org/llama-cpp-v1), [ggml v1.0.0 release](https://github.com/ggml-org/ggml/releases/tag/v1.0.0)

## Thinking Machines Trains End to End in 4 Bits

### Three Formats, Three Jobs

Thinking Machines published its recipe for training with low-precision arithmetic on NVIDIA GB300 hardware. BF16 uses 16 bits per value and runs at 2.5 PFLOPS. MXFP8 uses 8.25 bits and runs at 5 PFLOPS. NVFP4 uses 4.5 bits and runs at 15 PFLOPS. NVFP4 stores values with 3.6 times fewer bits than BF16 and runs up to six times faster.

### Where Rounding Hurts Most

Pretraining forward passes and reinforcement learning sampling care most about speed and memory. Backward passes care about bias. A value that always rounds up creates an error that compounds across layers and steps. Thinking Machines uses NVFP4 in expert layers for forward passes. It uses MXFP8 for backward passes with re-quantization and stochastic rounding.

### The 8% Wall-Clock Win

The result is Inkling 2 Small. The company says it is the largest model it knows of trained end to end with a native 4-bit forward pass. The same numeric recipe runs from pretraining through the final RL rollout. That removes the need to calibrate a quantized checkpoint after training. In the largest jobs, the recipe delivered an 8% wall-clock improvement.

### What It Does Not Prove

This is one model on one hardware stack. The 8% figure comes from Thinking Machines' own jobs, not an independent benchmark. Four-bit training may not transfer to every architecture or cluster. The useful lesson is systems co-design. Faster math only helps when the kernels, communication, and rounding strategy agree.

**Sources:** [Thinking Machines](https://thinkingmachines.ai/blog/end-to-end-4-bit-training/)

## FAQ

### Did Nvidia really buy its own GPUs?

Not directly, according to the report. Nvidia allegedly invested in small cloud providers that then bought Nvidia GPUs. That is vendor financing, not a fake sale. The concern is that the demand was not independent.

### Is ChatGPT Wallet available to everyone?

No. It launched for a limited group of U.S. ChatGPT Pro subscribers aged 18 and over. Users need a U.S.-issued Visa, Mastercard, or American Express card. OpenAI says it will expand access after testing.

### Did Claude prove new theorems in Gödel's notebooks?

Claude produced a digest of the notebooks. Von Plato says that digest revealed hundreds of theorems and dozens of earlier-than-known results. Those claims still need checking against the original pages by historians.

### Is the FAA's SMART system controlling flights?

No. SMART recommends routes and arrival orders. FAA specialists review each recommendation, and controllers can decline it. The FAA says the tool cannot take over an aircraft.

### Can I run llama.cpp v1.0 on a laptop?

Yes, if the model fits your memory. The project supports CPU and GPU backends across Linux, macOS, and Windows. The 1.0 release is mainly about API stability, not a new model.

## What to Watch Tomorrow

### Three Threads Worth Following

Nvidia still has to answer the Wall Street Journal's reporting in detail. OpenAI's wallet will face its first fraud tests as access expands. And the air traffic controllers' union will decide whether to fight SMART or join its next review.

### The Pattern Behind Today

Three of today's stories are about the same thing: who checks the machine. Nvidia's investors must check whether demand is real. Gödel's historians must check Claude's digest. The FAA's controllers must check SMART's advice. The tools are getting better. The verification layer is still human.

**Sources:** [TechPowerUp](https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus), [The Guardian](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths), [Ars Technica](https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/)
