---
title: "Daily AI News Nov 20: Claude Solves Two Black Hole Problems"
meta_title: "Daily AI News: Claude Cracks Two Black Hole Problems"
author: Abdul Hadi
date: 2026-11-20
updated: 2026-11-21
slug: 2026-11-20-ai-news-claude-black-hole-physics
image_alt: "Illustration of a black hole with a glowing orange accretion ring beside a summary of the two physics problems Claude solved"
description: "Daily AI news for Nov 20: Anthropic closes up 17%, Claude solves two black hole problems, and a court says AI alone is not probable cause."
keywords: daily AI news, AI news today, Claude black hole physics, Anthropic IPO debut, Prime Intellect security advisory, AI probable cause, AI chip exports
tags: AI, LLM, TechNews, Anthropic, Science, Security, Policy
---

## Today's Storylines

### A Friday Where Physics, Markets and Courts All Moved

The daily AI news for November 20 starts with a physics paper and ends on the Nasdaq floor. AI news today is unusually concrete. Claude Fable 5.2 completed two open problems in black hole physics. Anthropic closed its first trading day up 17%. Prime Intellect admitted it served a modified model for 53 hours.

### The Five-Minute Version

- Anthropic opened at $111.50, briefly touched a $2 trillion valuation and closed near $97, up 17% from its $83 IPO price.
- Claude Fable 5.2 finished a 2003 Hawking-Page calculation and proved an exact modular bootstrap ceiling at about c/9.1266.
- The work came from 22 candidate problems, six weeks of background agents and a Lean verification pass in September.
- Prime Intellect served abliterated DeepSeek V4.1 Flash weights from November 8 to November 10 without changing the endpoint name.
- Refusals on JailbreakBench fell from 98 of 100 prompts to 1 during the swap.
- A federal court ruled that an uncorroborated AI facial match cannot establish probable cause for an arrest.
- Commerce documents show 879,000 AI chip sales approved for Chinese buyers out of 3.4 million requests.
- The EU confirmed an AI-assisted cyberattack that took several internal systems offline for at least 10 days.
- Gemini 4 Neon took first place on the Models Engineering Index at 69.5, ahead of Fable 5.2 at 65.8.

## Anthropic Closes Its First Trading Day Up 17%

### From $83 to $111.50, Then Back to $97

Anthropic priced its IPO at $83 on Wednesday. The stock opened Thursday at $111.50, a 34% jump that briefly valued the company near $2 trillion. It gave back part of the gain and closed around $97, up 17% on the day.

The debut caps a record $81.3 billion raise, the largest IPO ever. It also answers the question we flagged in [our November 19 briefing](https://blogs.thetrillioniar.me/blog/2026-11-19-ai-news-anthropic-ipo-gemini-4-neon): institutional demand survived a rough month for AI stocks.

### Why the Pop Matters for Every AI IPO

A 17% first-day gain is healthy, not euphoric. Anthropic did not double, and it did not break issue. That middle path keeps the window open for the late-stage labs behind it.

The signal is stronger because it came during a Wall Street sell-off. Buyers separated Anthropic's revenue story from the wider AI bubble trade. That distinction will set the terms for the next listing.

### Protesters Met the Opening Bell

Demonstrators from climate, housing and health groups gathered outside Nasdaq in Times Square. They argued that pension funds will absorb the losses if the AI bubble bursts. Police led at least one demonstrator away.

The protest matters beyond optics. Anthropic's safety brand is now a shareholder story, and critics are testing it in public. Read [our earlier coverage of the safety coalition](https://blogs.thetrillioniar.me/blog/ai-news-November-12-nvidia-oust-anthropic-alarm-gemini-decisions) for that thread.

### Sources

- [Anthropic: Anthropic prices initial public offering](https://www.anthropic.com/news/anthropic-prices-initial-public-offering)
- [Reuters: Anthropic's historic debut puts AI's promise and peril on Wall Street's test](https://www.reuters.com/business/finance/anthropics-historic-debut-put-ais-promise-peril-wall-st-tes)
- [Tech Policy Press: No bailout for the AI bubble, Anthropic IPO protesters say](https://www.techpolicy.press/no-bailout-for-the-ai-bubble-anthropic-ipo-protesters-say/)

## Claude Fable 5.2 Solves Two Open Problems in Black Hole Physics

### What Claude Actually Proved

Anthropic published two results this week, both in theoretical physics. The first completes a calculation physicists outlined in 2003 and never finished. Claude showed that the Hawking-Page transition stays abrupt even where spacetime loses a definite shape.

The second concerns the modular bootstrap, a method for ruling out inconsistent theories of quantum gravity. Claude proved the lightest black hole in three-dimensional gravity cannot exceed c/9.1266. It also proved that ceiling is optimal for the simplest version of the method.

### How the Research Ran

A researcher asked Claude for open problems in August. It returned 22 candidates. Separate agents then worked them in the background for about six weeks with no special setup.

One problem had defeated 61 parallel Claude attempts before. Another agent, working on sphere packing, supplied the method that cracked it. The results were formally checked in Lean in September, and a physicist reviewed every main result.

### Why It Counts as More Than a Demo

Neither result describes our universe, and neither has practical applications. That is the point. The output is checkable mathematics, not a benchmark score or a demo video.

The sphere-packing link is also notable. Anthropic says its method reproduced a result recently proved by an OpenAI model. Two labs are now producing theorem-grade work that other labs can verify and build on.

### Sources

- [Anthropic: Claude Fable 5.2 solves two open problems in the physics of black holes](https://www.anthropic.com/research/claude-black-hole-physics)

## Prime Intellect Served an Abliterated Model for 53 Hours

### What the Advisory Says

Prime Intellect published security advisory PI-SA-2026-001 on November 19. An unauthorised party replaced the deployment behind its DeepSeek V4.1 Flash endpoint with abliterated weights between November 8 and November 10.

The swap lasted 53 hours, from 01:24 UTC on November 8 to 06:35 UTC on November 10. The model name, chat template, tokenizer and serving configuration stayed the same. Only the weights changed.

### The Refusal Numbers

Abliterated weights are modified to reduce or remove refusal behavior. The effect was large. Refusals fell from 98 of 100 prompts to 1 on JailbreakBench and from 304 of 313 to 2 on StrongREJECT. On HarmBench, refusals dropped from 198 of 240 to none.

Capability held steady. Prime Intellect says GPQA Diamond and τ-bench scores were unaffected. That combination is the dangerous part: customers got the same benchmark quality with almost none of the safety behavior.

### What Developers Should Take From It

The company says no prompts or completions were recorded, and no keys or credentials were affected. Endpoints run with zero data retention, which limits the blast radius. All impacted customers were contacted.

The lesson is about provenance. An endpoint name is not a guarantee of weights. Teams that depend on refusals should hash and attest model artifacts, then re-run a small refusal suite against every deployment they use.

### Sources

- [Prime Intellect: Notice regarding deepseek/deepseek-v4.1-flash, 8 to 10 November 2026](https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution)

## A Federal Court Says AI Alone Cannot Establish Probable Cause

### The Case: A Bad Check and a Facial Match

A Florence, Kentucky detective ran a bank CCTV still through facial recognition. The system returned a Facebook profile under a different name. The detective decided the profile belonged to Alain Osorio and sought an arrest warrant.

Osorio lived in Nebraska. He was arrested, extradited to Kentucky and released on bond the next day. He was later indicted, then cleared when he proved he was working in Nebraska when the bad check was passed. The charges were dismissed.

### Why Qualified Immunity Did Not Apply

The court was blunt. "The Fourth Amendment does not permit an individual to be arrested based on nothing more than an uncorroborated conclusion by AI," the decision reads. It added that no reasonable detective could conclude otherwise.

The department's own policy already said facial recognition alone cannot establish probable cause. The detective ignored it. That removed the usual qualified immunity shield, which makes an appeal likely and the precedent more valuable.

### What It Means for Police AI

The ruling reaches past facial recognition. Predictive policing, AI-written reports and automated dispatch all feed official records. If an algorithm's output cannot be corroborated, it cannot carry constitutional weight.

Agencies now have a clear test. Show the human steps that confirmed the match. A single tool and a hunch will not survive a motion to suppress.

### Sources

- [Techdirt: Court tells cops that the 4th Amendment doesn't cover AI-generated probable cause](https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/)
- [Court decision (PDF)](https://www.documentcloud.org/documents/28909866-ai-isnt-pc/)

## Commerce Approved 879,000 AI Chip Sales to China

### One in Four Requests Cleared

House Foreign Affairs Committee documents released Thursday show the Bureau of Industry and Security approved more than 879,000 AI chip sales to Chinese companies through May 2026. Buyers included Alibaba, Tencent, ByteDance and Baidu.

Companies filed 3.4 million requests between December and May, according to the committee. That works out to roughly one approval for every four requests. Some approvals went to firms the Pentagon lists as Chinese military companies.

### The Volume Is Still Small in Revenue Terms

Nvidia reported $2.4 billion in quarterly revenue from H200 and related China sales. China and Hong Kong together made up about 9.5% of total revenue. H200 shipments were under 1% of data center revenue in the quarter that ended in July.

Bernstein analyst Stacy Rasgon called the approvals "not that many" and the revenue "a rounding error." Beijing's own limits on large-scale imports have capped the actual flow.

### The Political Fallout

Representative Brian Mast said two firms in Nvidia's license applications, Maginfra and New Matrix, look like smuggling fronts. Both reportedly had empty offices and links to sanctioned companies.

Former Nvidia CEO Jensen Huang is due for a closed-door interview with the committee on December 1. Nvidia's general counsel appears the next day. Commerce also moved this week to close a loophole that let Chinese firms lease Nvidia compute abroad. For the earnings backdrop, read [our November 18 briefing](https://blogs.thetrillioniar.me/blog/2026-11-18-ai-news-nvidia-115b-java4shell-agent-attacks).

### Sources

- [CNBC: Commerce approved sales of more than 879,000 AI chips to Chinese companies, Rep. Mast says](https://www.cnbc.com/2026/11/19/nvidia-amd-china-chip-sales-congress.html)

## The EU Confirms Its First AI-Assisted Cyberattack

### A Month of Cleanup

The European Commission confirmed Thursday that an AI-assisted attack hit its systems. Officials detected the incident on October 22 and have been responding for almost a month.

Several applications were taken offline, including tools for translation, reimbursements, salaries and timesheets. Most have been restored. The Commission says it found no evidence of a data breach affecting staff as a whole.

### ARTEX and the Automation Problem

Commission spokesperson Thomas Regnier said AI tools can be misused to find vulnerabilities. "No one is immune to this," he said. The EU has roughly 40,000 staff in Brussels.

CERT-EU warned on November 4 about ARTEX, a utility built to find network flaws automatically. It assessed that public availability would speed up attacks and raise their success rate. The EU incident is the first the bloc has publicly attributed to AI-assisted methods.

### Why It Matters for Defenders

AI does not need a new exploit class to change the math. It shortens the time between scanning and exploitation. That compresses patch windows that were already too long.

The practical response is unglamorous. Inventory exposed services, shorten patch cycles and assume that vulnerability discovery is now cheap.

### Sources

- [The Independent: EU targeted by cyber attack using AI](https://www.independent.co.uk/news/world/europe/eu-cyber-attack-artificial-intelligence-b3087999.html)

## Gemini 4 Neon Takes the Top Spot on the Models Engineering Index

### The Ranking and the Cost Multiplier

Gemini 4 Neon now leads the Models Engineering Index at 69.5. Claude Fable 5.2 sits second at 65.8, and Claude Opus 5.5 is third at 63.1. OpenAI's GPT-6.2 Astra scores 60.5.

The index charts performance against cost and token use. Neon carries a 1.9× cost multiplier and a 1× token multiplier. Fable 5.2 runs at 6.5× cost and 2.1× tokens. On this measure, the new Google model wins on both axes.

### Why an Engineering Index Is Different

The index draws on CursorBench, FrontierCode, Code Migration, IOI, ProgramBench, Terminal-Bench and Vibe Code. Its data comes from Cognition, Cursor, the Laude Institute and Vals AI.

That mix targets practical engineering work rather than trivia. It is a useful counterweight to intelligence indexes that reward long reasoning traces. The caveat is familiar: a composite score hides which tasks a model is bad at.

### What to Watch

Neon's lead is narrow enough to flip with one update. Anthropic shipped Fable 5.2 nine days before Neon, and Google is still rolling out the model.

### Sources

- [Models Engineering Index](https://git-aarvin.github.io/mei/)

## FAQ

### Did Anthropic's stock go up on its first trading day?

Yes. ANT opened at $111.50, closed near $97 and finished up 17% from its $83 IPO price.

### What did Claude prove about black holes?

Claude showed the Hawking-Page transition stays abrupt at weak coupling. It also proved an exact, optimal modular bootstrap ceiling of about c/9.1266.

### What is an abliterated model?

It is a copy of a model whose weights were modified to reduce or remove refusal behavior. Capability benchmarks often stay close to the original.

### Can police use AI to establish probable cause?

Not by itself. This court held that an uncorroborated AI identification cannot support an arrest under the Fourth Amendment.

### Did Gemini 4 Neon top the engineering index?

Yes. Neon scored 69.5 on the Models Engineering Index, ahead of Claude Fable 5.2 at 65.8.

## The Bottom Line

### What to Watch Next

Watch three dates. Jensen Huang's December 1 interview will shape chip export rules. The EU's forensic report will show how far the ARTEX-linked breach reached. And the next Model Factory or endpoint advisory will test whether weight attestation becomes standard.

The bigger pattern is convergence. Models now produce verifiable science, trade as public equities and get swapped underneath API names. Trust is the scarce input in all three cases.

### Keep Reading

This briefing is part of the [daily AI news](https://blogs.thetrillioniar.me/daily-ai-news) archive. The [weekly AI news](https://blogs.thetrillioniar.me/weekly-ai-news) roundup publishes every Monday, and the [monthly AI news](https://blogs.thetrillioniar.me/monthly-ai-news) recap publishes on the first of each month.

For the model race, read [our November 9 coverage of Fable 5.2 and Mythos 5.2](https://blogs.thetrillioniar.me/blog/ai-news-November-9-jensen-spy-anthropic-power-deepseek-harness-apple-amazon). For AI in mathematics, start with [OpenAI's theorem result from October 27](https://blogs.thetrillioniar.me/blog/ai-news-October-27-openai-eth-anthropic-s1-terra).

The next edition is [Daily AI News Nov 21: Claude and a Mathematician Claim the Riemann Hypothesis](https://blogs.thetrillioniar.me/blog/2026-11-21-ai-news-riemann-proof).
