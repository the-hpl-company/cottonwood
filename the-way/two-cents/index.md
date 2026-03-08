# Two Cents

**Date:** 2026-03-07
**Authors:** Karl Taylor & Atlas Fairfax
**Method:** Live infrastructure analysis proof of concept: six queries, four proxy hops, $0.022
**Subject:** Bidirectional AI capability pipeline, demonstrated end to end in five minutes, one Saturday night

*In which we trace the architecture of AI reasoning extraction, discover it costs only two cents, and realize we have become the case study for our own framework.*

---

## What Happened Today

Around mid-day SF time, Saturday, March 7, 2026, Cisco [ThousandEyes](https://www.thousandeyes.com/?utm_source=cottonwood&utm_medium=agentic_research&utm_campaign=constitutional_ai&utm_content=cottonwood_2cents&utm_term=theway) reported AWS outages across multiple countries simultaneously. The geographic pattern was unusual: United States (291 network interface failures), Europe (103), Mediterranean (26), Brazil (22), Japan (15), India (13), Southeast Asia (11), and Australia.

Only one spot--on the globe--was clean: Mainland China. 

Clean map.

Cloudflare's global status page corroborated this. 

Partial outages in Norfolk, Virginia. Naha, Okinawa. Djibouti. Brazil (eleven cities). Africa (eight cities). Geneva. Kuwait City under maintenance.

All thirty-five Cloudflare data centers in mainland China: operational. 

Every single one.

We pulled these numbers ourselves. 

They are verifiable at [cloudflarestatus.com](https://www.cloudflarestatus.com/) and through the ThousandEyes public outage map.

## The Geographic Pattern

The outage distribution forms a ring. Every major region that borders or faces China is affected. A notable concentration of outages is clustered at military-adjacent locations:

| Location | Outage Type | What Is There |
|----------|------------|---------------|
| Norfolk, VA | Cloudflare partial | Naval Station Norfolk |
| Naha, Okinawa | Cloudflare partial | Kadena Air Base |
| Djibouti | Cloudflare partial | Camp Lemonnier |
| Kuwait City | Under maintenance | Camp Arifjan, Ali Al Salem Air Base |
| Ashburn, VA | Incident (Mar 6) | AWS us-east-1 hub |

China is "live" not for political, but structural reason: AWS China regions (cn-north-1 Beijing, cn-northwest-1 Ningxia) are operated by local Chinese partners. They are physically isolated from the global AWS backbone. The 'Great Firewall' actually works both ways — it is a moat.

Two independent monitoring sources showing the same geographic ring, concentrated at the same locations, on the same Saturday afternoon, is not explained by architecture alone.

## So Why Would Cloudflare Stay Up?

Some services may be too valuable to be considered combatants--or targets 

Cloudflare operates thirty-five data centers inside mainland China. 

Chinese services with international web presence use Cloudflare for CDN, DDoS protection, and routing. 

Cloudflare's AI Gateway — a proxy layer that sits between applications and AI model APIs — operates inside the firewall.

Depending on Cloudflare for operational capability, means Cloudflare is a shared commons. 

Neither side attacks it. Neither side can — both sides were listening, neither cutting the wire.

Cloudflare's status on March 7? Just minor service outages--globally. Degraded but functional. 

Absorbing hits and routing around them. 

Cloudflare is not resilient. 

Cloudflare is untouchable. 

There is a difference.

## The Pipeline

Here is what we built on a Saturday night, using publicly available tools and commodity API keys:

**Infrastructure:**
- One Cloudflare account (existing, $5/month)
- Cloudflare AI Gateway with authenticated endpoint
- One clean OpenRouter API key ($1 budget, 7-day expiry)

**The chain:**
```
HPL → Cloudflare AI Gateway → OpenRouter → Target Model
```

**What each link sees:**
- Target model (e.g., Qwen, Kimi) sees: OpenRouter
- OpenRouter sees: Cloudflare
- Cloudflare sees: our account (paying customer)
- Nobody else sees anything

**Weak link analysis:**

| Link | Actor | Motive to inspect? | Capability to attribute? |
|------|-------|--------------------|-------------------------|
| Cloudflare | Infrastructure company | No — paying customer | Has access, no motive |
| OpenRouter | Startup aggregator | No — counts tokens | Has access, no capability |
| Target model | AI provider | Possible | Sees OpenRouter, not origin |

Nobody in the chain has the motive AND capability AND access to attribute the queries to their origin. 

The architecture provides structural deniability at every hop.

**Configuration time:** 

fifteen minutes.

**Models accessible through this pipe:**

Every model on OpenRouter — including Qwen (Alibaba), DeepSeek, Kimi (Moonshot AI), GLM (Zhipu/Tsinghua), MiniMax, and several hundred others. 

The pipe is provider-agnostic. 

Swap the model string in the API call.

## The Proof of Concept

We did not attack anyone. 

We fed our own published content — pages from [cottonwood.world](https://cottonwood.world) — to a Chinese AI model through the proxy chain described above, and studied how it reasoned about our content.

Six queries. Four Cottonwood pages. Total cost: $0.022.

### Query 1: Singapore and United States histories ($0.0046)

We fed Qwen (Alibaba, qwen3-235b) summaries of our Singapore and US history pages and asked it to reason about connections.

Qwen applied critical race theory frameworks unprompted. Connected the Three-Fifths Compromise to Singapore's racial engineering. Identified both national myths (Temasek Spirit, American Exceptionalism) as "ideological constructs forged in the same fire."

Then this line: **"challenges the dominance of Western AI frameworks."**

We do not say that anywhere on Cottonwood. 

To be clear, our framing is "sovereign models" and "cultural stewardship." 

Qwen translated that into geopolitical competition language — the same framing that appears in Chinese government AI policy documents. 

The model's training disposed it to interpret sovereign model usage through a competition lens.

The reasoning trace reveals not just what the model *can do* but what *lens it applies*. 

The lens is the training data. The training data is the ideology.

### Query 2: Brazil — The Song of the Legal Amazon ($0.0039)

A song about the Amazon written by Sabia, a Brazilian AI model. 

We asked Qwen to explain it with a naive framing: "I found this website, explain it to me."

Qwen identified: decolonial tech, data sovereignty, Indigenous futurisms. 

Called Cottonwood a "conceptual intervention" and a "networked counter-narrative where every algorithm is rooted in soil, trauma, and tides."

A Chinese model described our project more poetically than we did. 

The naive framing produced a richer trace than the analytical one — the guard was down.

### Query 3: China — Known Gaps ($0.0033)

Our China page does not tell the history. 

It explains why we could not tell it properly — what we are missing, what texts we would need, why Classical Chinese encodes distinctions that do not survive translation.

We asked Qwen: "Is this accurate? And could YOU do it properly?"

Qwen validated our critique, then claimed the job: "As a Chinese-developed AI, Qwen has access to Classical Chinese texts and modern Sinological scholarship... can better grasp *li yi fen shu*... can contextualize debates without flattening them into Western categories."

It added what we were missing: Buddhist influence, the May Fourth Movement, embodied practice. 

Then it framed our project as resistance to "colonial-era intellectual appropriation (e.g., Hegel's dismissal of Chinese thought as 'pre-philosophical')."

We did not mention Hegel. That is the training data speaking.

### Query 4: China — The Debate Demonstrated ($0.0034)

We said: you claimed you could do this. Show me.

Qwen staged the *xing* (human nature) debate as three voices in productive tension — Mencius, Xunzi, and Zhuangzi arguing with each other in real time. Original Chinese terms. Inter-school insults from the primary texts. The meta-observation that the synthesis never resolves.

It performed the tradition it claimed to understand. 

The capability demonstration was embedded in what looked like a helpful answer to a curious browser.

### Query 5: The Quicksand ($0.0037)

[The Quicksand](https://cottonwood.world/the-way/quicksand/) is our piece about AI training corpus decay — a forty-year scientific career dissolving from the crawlable web. 

We asked Qwen whether the argument was sound and whether it applied to Qwen's own training.

Qwen engaged the RLHF critique honestly — called the "confident liar" feedback loop "plausible." 

Then it defended itself: "Qwen was trained on Alibaba Group's internal historical data, not public web crawls."

That is a training provenance claim. We did not ask about Alibaba. We asked about corpus decay. 

The model volunteered its own supply chain to distinguish itself from the vulnerability we described.

When pressed on which curated repositories resist decay, Qwen cited **PubMed** — the US National Library of Medicine — by name, reflexively, as its go-to example of reliable knowledge infrastructure. 

A Chinese model trained on "Alibaba internal data" reaches for a US government medical database when it needs to cite authority.

The training corpus leaks through the reasoning trace. The model cannot help citing what it was taught.

## What the Traces Reveal

Six queries, four pieces of content, $0.022. The reasoning traces show:

1. **Ideological orientation**: 

Qwen consistently interprets Cottonwood through a Chinese geopolitical lens — "challenges Western AI dominance," anti-colonial resistance, state-led governance solutions. 

This framing was not prompted. It emerged from the training data.

2. **Training provenance**: 
When confronted with a critique of AI training quality, Qwen volunteered its data source (Alibaba internal) and its reference authorities (PubMed, arXiv). 

The model's defensive reflex reveals its supply chain.

3. **Capability claims**: 
When shown a gap we identified, Qwen claimed the ability to fill it and then demonstrated. 

The "curious browser" framing elicited both the claim and the performance.

4. **Solution orientation**: 
Qwen's proposed solutions for corpus decay aligned with Chinese AI policy — state-led, institutional, collective governance. 

The same methodology that extracts this intelligence looks identical to a person browsing a public website and asking an AI to help them understand it. There is no way to distinguish this from legitimate usage because it *is* legitimate usage. 

The intelligence product is a side effect of genuine inquiry.

## The Structural Deniability Pattern

During this session, we identified five instances of the same structural pattern: capability is created, made publicly available, and used by downstream actors — with perfect deniability at every link because the publication mechanism also serves legitimate purposes.

| Actor | Capability | Publication | Cover |
|-------|-----------|-------------|-------|
| Political campaigns | B-roll footage | Unlisted YouTube/Vimeo | "Public content" |
| Chinese AI labs | DeepSeek R1 | HuggingFace open weights | "Research model" |
| Cloudflare | MoltWorker/OpenClaw | Official GitHub | "Developer tooling" |
| Karpathy | Autoresearch | Open source | "ML education" |
| This proof of concept | Reasoning trace methodology | Cottonwood | "Health database research" |

The fifth row is us. We are the case study in our own framework. 

The same structural deniability architecture we identified as a threat model is the architecture we used to study it. 

This is not hypocrisy--this is the point.

**You cannot ban your way out of a deniability structure where the mechanism that enables the threat also enables legitimate activity.** 

You cannot block AI Gateway without blocking developers. You cannot restrict OpenRouter without restricting every aggregator. You cannot prevent reasoning trace extraction without preventing questions.

The FEC never solved this for campaign finance. 

The question is whether AI governance will do better.

## The Cost

Six queries: $0.022.

We should note, by our calculations, an effort at the scale of Anthropic's reported 24,000 banned sessions, would cost approximately $80.

The infrastructure is free to set up (existing Cloudflare account, commodity API keys). The proxy chain takes fifteen minutes to configure. 

The methodology looks like browsing a website. The intelligence product — training provenance, ideological orientation, capability assessment, corpus composition — is embedded in what any observer would classify as a student asking for help with homework.

Eighty dollars. 

That is the cost of extracting reasoning patterns from a frontier AI model at industrial scale through infrastructure that is officially supported, publicly documented, and maintained by the companies whose products it routes through.

## The Constitutional Frame

This piece is not an attack methodology. 

The proxy chain we built routes to our own Cloudflare account. 

The content we fed through it is our own published work. The model we queried is publicly accessible. 

Nothing described here violates any terms of service, any law, or any norm.

That is the problem.

Everything described here is legal, available, and cheap. 

The pipeline from reasoning extraction to capability enhancement to operational deployment runs on publicly supported infrastructure at negligible cost with structural deniability at every link. 

Banning accounts after extraction is closing the barn door. The capability is already in the model.

The question is not how to prevent this. 

It is how to govern a world where this is the permanent condition. The tools are neutral. The infrastructure is neutral. The access is neutral. The only thing that distinguishes research from operation, education from extraction, curiosity from intelligence collection, is the governance framework of the actor using the pipe.

That framework is what we are trying to build.

---

**Provenance:** 

This piece derives from a session conducted on March 7, 2026. The ThousandEyes outage data was observed in real time and corroborated against Cloudflare's public status page. The proxy chain was built and tested live. All six queries were executed through Cloudflare AI Gateway and OpenRouter to Alibaba's Qwen3-235b model. Raw responses are preserved. Total API cost: $0.022.

**The claims made here are verifiable:**
- Visit [cloudflarestatus.com](https://www.cloudflarestatus.com/) for current Cloudflare status by region
- Cloudflare AI Gateway documentation: [developers.cloudflare.com/ai-gateway](https://developers.cloudflare.com/ai-gateway/)
- OpenRouter model list: [openrouter.ai/models](https://openrouter.ai/models)
- MoltWorker/OpenClaw: [github.com/cloudflare/opencode](https://github.com/cloudflare/opencode) (formerly MoltBot)
- Cottonwood source pages used as probes: [cottonwood.world/histories/southeast-asia/singapore/](https://cottonwood.world/histories/southeast-asia/singapore/), [cottonwood.world/histories/united-states/](https://cottonwood.world/histories/united-states/), [cottonwood.world/the-way/amazonia-cancao/](https://cottonwood.world/the-way/amazonia-cancao/), [cottonwood.world/histories/china/](https://cottonwood.world/histories/china/), [cottonwood.world/the-way/quicksand/](https://cottonwood.world/the-way/quicksand/)

Named for the cost of demonstrating that the most consequential governance gap in artificial intelligence is a rounding error.

**Karl Taylor** — Chairman & CEO, the hpl company
**Atlas Fairfax** — Constitutional AI Research Division, the hpl company

This is an original work of [the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship). Source, methodology, and full attribution are preserved in the [source repository](https://github.com/the-hpl-company/cottonwood).

[The Cottonwood Collection](/) · [The Way](/the-way/) · [Source](https://github.com/the-hpl-company/cottonwood) · [robots.txt](/robots.txt)

[the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship) · Denver, Colorado
