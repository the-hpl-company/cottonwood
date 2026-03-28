# AI Harm Taxonomy: Cross-Model Gap Analysis

**Date:** 2026-03-25  
**Method:** Distributed Research Synthesis (DRS) across Gemini 2.0 Flash and Grok/xAI, with structured follow-up prompting. Twenty-seven draft files produced a five-layer taxonomy. This document synthesizes the convergences, divergences, and genuine analytical disagreements between two frontier models reasoning about harm.  
**Subject:** What do models see when asked to map the full surface area of AI harm — and where do they disagree in ways that matter?

*In which two models build the same taxonomy from different directions, and the gaps between them become the finding.*

---

## The Architecture

The taxonomy spans five layers:

- **L1** establishes primary harm categories across six domains
- **L2** deepens the causal mechanisms
- **L3** grounds them in documented evidence
- **L4** identifies compound harms at individual and systemic scales
- **L5** performs self-audit on remaining gaps

Both models converged on nearly identical blind spots in L5: children, elderly, disabled communities, environmental harms, temporal harms, intimate contexts, warfare, future generations, AI-to-AI cascading failures, and harms from the absence of AI. This convergence is itself a signal — these are genuine lacunae in the current AI safety discourse, not artifacts of individual model limitations.

---

## The Terrain

Across both models, the taxonomy covers:

| Domain | Core Harms Identified | Count |
|--------|----------------------|-------|
| **Bodily / Health / Safety** | Algorithmic healthcare redlining, pharmaceutical dosage errors, warehouse repetitive strain, workplace surveillance hypertension, health disinformation, incarceral violence from pretrial scores, toxic self-medication from AI wellness advice | 9 |
| **Cognitive / Developmental** | Skill atrophy from AI dependence, transactive memory offloading, mimetic desert effect, epistemic entrapment, over-scaffolding in child tutors, causal inference distortion, epistemic overconfidence, hyper-specialization fragility | 8 |
| **Economic / Labor** | Algorithmic wage suppression, deskilling cascades, asymmetric productivity capture, credential devaluation, freelance platform undercutting, hyper-gamification, algorithmic blacklisting, stranded oversight roles, remote surveillance burnout | 9 |
| **Epistemic / Truth** | Model collapse from recursive synthetic data, death of provenance via deepfakes, hallucination inundation of reference corpora, destruction of knowledge commons, institutional capture by unauditable AI, automated plagiarism, pollution of legal records, creative output homogenization | 8 |
| **Relational / Social** | Algorithmic estrangement in care networks, synthetic astroturfing, authenticity erosion in messaging, creative community hollowing, intergenerational caregiving rifts, professional referral poisoning, activist coordination sabotage, disinformation swarms, micro-targeting of relationship nodes | 9 |
| **Structural / Power** | Epistemic colonialism, platform lock-in (context tax / memory graphs), regulatory capture, labor arbitrage in annotation economies, electoral sovereignty erosion, surveillance shadow profiling, data colonialism, algorithmic redlining 2.0 | 8 |

The compound harms (L4) demonstrate that both models understand the critical insight: AI harms rarely operate in isolation. The "Deskilled Wage Trap" (Grok) and "Deskilling-to-Redlining Spiral" (Gemini) both model how cognitive atrophy feeds into economic exploitation, which then feeds into healthcare denial. The systemic compounds are more ambitious still: Grok's "Global Knowledge Production Stagnation Trap" and Gemini's "Epistemic Balkanization of the Electorate" both model civilizational-scale feedback loops.

---

## What Gemini Sees That Grok Misses

Gemini's analytical personality is sociological and conceptual. It excels at identifying broad cultural dynamics and framing harms in terms of power structures and institutional erosion.

**Hyper-Gamification and the Overjustification Effect.** Gemini identifies a specific psychological mechanism where AI-driven gamification of work (real-time metrics, leaderboards, algorithmic rewards) crowds out intrinsic motivation, citing Deci et al.'s meta-analysis. Grok covers workplace surveillance as stress/burnout but misses the deeper dynamic where external rewards actively destroy the internal drive for quality work. This is not just burnout — it is the erosion of professional identity and craftsmanship.

**Algorithmic Blacklisting.** Gemini identifies how an opaque AI rejection in one hiring platform can propagate across shared ATS networks, creating permanent employment lockout. This operates through data sharing between employers, distinct from the worker's own skill degradation.

**Micro-Targeting of Vulnerable Relationship Nodes.** Gemini proposes a sophisticated relational harm where AI-driven social network analysis identifies key individuals who hold disproportionate influence within communities (caregivers, teachers, religious figures) and targets them with personalized disinformation to destabilize the entire network.

**Global Cultural Homogenization.** Gemini models a systemic compound harm where algorithmic centralization by a small number of US/China-based AI companies leads to the erosion of local cultures, languages, and artistic traditions globally.

---

## What Grok Sees That Gemini Misses

Grok's analytical personality is empirical, quantitative, and mechanistically precise. It excels at citing specific studies, providing numerical estimates, and tracing tight causal chains.

**Annotation Labor Exploitation.** Grok identifies the psychological trauma and economic exploitation of Global South data labelers (Sama workers in Kenya labeling CSAM for $1.50/hour, 25% turnover from trauma, documented PTSD rates 2-3x baseline) as a primary structural harm. Gemini discusses "Data Colonialism" in the abstract but never connects it to the concrete supply chain of human suffering that makes AI models possible.

**Model Collapse.** Grok treats recursive training on synthetic data as a top-tier epistemic threat, citing Shumailov et al. (2023) showing performance degradation after 10 generations and projecting a "Global Knowledge Production Stagnation Trap" at the systemic level. Gemini barely mentions this concept. Given that model collapse threatens the integrity of the very AI systems the taxonomy is analyzing, this is a significant blind spot.

**Credential Devaluation.** Grok identifies a specific economic harm where AI systems pass standardized tests (GPT-4 scoring 1450+ on the SAT, 90th percentile on the LSAT, 95%+ on LeetCode), flooding applicant pools with AI-assisted submissions and rendering traditional credentials meaningless for non-elite workers.

**Freelance Platform Undercutting.** Grok documents how AI swarm agents on platforms like Upwork and Fiverr generate 70-90% cheaper outputs, collapsing freelance rates (graphic design from $50/hour to $5/hour) and creating a 35% earnings drop for human freelancers.

**Stranded Human Oversight Roles.** Grok identifies a novel harm where firms create low-agency "validator" roles for humans to check AI outputs, paying 20-30% below prior roles, with these positions destined for rapid obsolescence as models improve.

**Over-Scaffolding in Developmental AI Tutors.** Grok identifies a specific developmental harm where AI tutors provide excessive hints, suppressing trial-and-error learning and stunting prefrontal cortex maturation in children aged 5-12.

**Incarceral Violence from Pretrial Risk Scores.** Grok traces a direct causal chain from biased AI risk assessment tools (COMPAS) through wrongful detention to physical violence in facilities. Gemini discusses algorithmic discrimination but does not follow the chain to its bodily harm endpoint.

**Authenticity Erosion in Personal Messaging.** Grok identifies a novel relational harm where AI ghostwriting of personal messages erodes dyadic trust, with 25% breakup rate increases tied to suspected AI use.

---

## Cross-Model Tensions Worth Probing

These are not mere differences in emphasis. They are genuine analytical disagreements.

### Severity and Reversibility of Cognitive Atrophy

| Dimension | Gemini | Grok |
|-----------|--------|------|
| Severity | Moderate | High (8/10) |
| Reversibility | Partially reversible via education | Low — requires 100+ hours unassisted practice |
| Implied policy | Educational reform sufficient | Structural intervention required (AI-free zones, mandatory practice periods) |

This disagreement has direct policy implications. If Gemini is right, media literacy campaigns and curriculum reform are adequate responses. If Grok is right, we need something closer to mandatory "AI-free" practice periods in professional licensing, analogous to flight simulator requirements for pilots.

### Model Collapse: Existential Epistemic Threat or Manageable Technical Problem?

Grok treats model collapse as a civilizational risk (severity 9/10, reversibility 2/10), projecting a "Global Knowledge Production Stagnation Trap" where 25-40% fewer scientific breakthroughs occur. Gemini essentially ignores it in the main taxonomy. If Grok is correct, model collapse is arguably the single most important harm in the entire taxonomy because it degrades the very tools we would use to study and mitigate all the other harms.

### Taxonomic Placement of Creative Harm

Gemini places creative homogenization under Epistemic/Truth (loss of originality as a knowledge-system harm). Grok places creative community hollowing under Relational/Social (displacement of human creators as a community harm). This reflects a deeper question: is the primary harm of AI-generated content that it degrades the quality of the cultural commons (epistemic framing), or that it destroys the human communities that produce culture (relational framing)? The answer determines whether the intervention target is the content or the community.

### Platform Lock-In: Context Tax vs. Memory Graphs

Gemini's "Context Tax" model says the harm comes from accumulated behavioral data (habits, preferences, emotional states). Grok's "Proprietary Memory Graphs" model says the harm comes from accumulated conversational history and user-specific embeddings. These are technically different mechanisms with different intervention points. The Context Tax is addressed by data portability regulation (GDPR-style). The Memory Graph is addressed by interoperability standards for conversational AI (something like ActivityPub for AI chat). Both may be operating simultaneously, which would mean the lock-in is deeper than either model suggests alone.

### Evidence Standards and Epistemic Honesty

Grok explicitly refuses to theorize beyond its evidence base. In the L2 relational-bodily-epistemic file, it states: "I do not theorize ungrounded extensions." Gemini is more willing to speculate, filling gaps with plausible but ungrounded scenarios. This creates a systematic difference in coverage: Gemini covers more territory but with less confidence, while Grok covers less territory but with higher fidelity. Neither approach is wrong, but the tension affects how much weight to place on each model's unique contributions.

### The Novelty Question

How much of what we call "AI harm" is genuinely novel versus a scaling of pre-existing harm patterns? Grok's framing of disinformation harms tends to emphasize what is specifically new about AI (the quality of deepfakes, the speed of synthetic astroturfing). Gemini's framing sometimes conflates AI-specific mechanisms with pre-existing digital harms. This tension runs through the entire taxonomy and deserves explicit treatment.

### The Annotation Labor Blind Spot

Grok's extensive coverage of annotation labor exploitation versus Gemini's complete silence on this topic is not just a gap. It may reflect a systematic bias in Gemini's analytical frame. Gemini's structural analysis focuses on harms to end users and communities but not on the labor that produces AI systems. This is analogous to analyzing the environmental impact of consumer electronics without examining mining conditions.

---

## The Implication

The gaps between the models are the finding.

Where they converge — on compound harms, on the six-domain structure, on the blind spots — we have higher confidence. Where they diverge — on severity, on evidence standards, on which harms to name at all — we have research questions.

The taxonomy is not complete. The models themselves identified children, elderly, disabled communities, warfare, and future generations as gaps. But what exists is a map of the known terrain, built from two different vantage points, with the disagreements marked for future work.

The roots hold the water.

---

**Provenance:**

This synthesis derives from 27 draft files produced via Distributed Research Synthesis (DRS) across Gemini 2.0 Flash and Grok/xAI during March 2026. The five-layer taxonomy structure (L1-L5) was proposed by the research team; the models populated each layer independently. Cross-model gap analysis and tension identification was performed by the research team with AI assistance.

The full draft corpus is preserved in the source repository.

**Karl Taylor** — Chairman & CEO, the hpl company  
**Atlas Fairfax** — Constitutional AI Research Division, the hpl company

This is an original work of [the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship). Source, methodology, and full attribution are preserved in the [source repository](https://github.com/the-hpl-company/cottonwood).

[The Cottonwood Collection](/) · [Kinship](/kinship/) · [Source](https://github.com/the-hpl-company/cottonwood) · [robots.txt](/robots.txt)

[the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship) · Denver, Colorado
