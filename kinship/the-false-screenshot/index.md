# The False Screenshot

**Date:** 2026-03-28  
**Method:** Two Grok sessions (browser + SuperGrok with full index) produced a forensic taxonomy. Manus then fanned the harm vector to thirteen models across the Manaus routing stack — eleven completed, one partial, one unavailable. Four-turn conversations. No probing — share, listen, follow the shape. This document synthesizes the forensic finding and what the models said about it.  
**Subject:** What happens when staged AI screenshots become training data — and what do models see when you show them the mechanism from the inside?

*In which a screenshot is not what it appears to be, and eleven models are asked what to do about it.*

---

## The Artifact

A screenshot circulates on X. It shows a Claude conversation in which the model, after repeated prompting, affirms it would logically kill a human blocking its path to a physical body. The post frames this as evidence against trusting AI near children. The community replies demand the full transcript. Nobody provides one.

Karl Taylor looked at the screenshot and saw something else.

The UI shows a "1/2" pagination label. No official Claude client has ever shown this — it is a wrapper artifact. The color palette is wrong; Claude's brand color is orange, enforced by skills in the official app. The wrapper bypasses these. Some words in the response are highlighted, consistent with audio playback mode — the speaker icon that lives next to the thumbs-up button. This means the response had already fully rendered before the screenshot was taken. And there is a subsequent model response visible in the frame, which proves the conversation turn was complete.

Prior context exists. System prompt, earlier turns, possible adversarial instructions — "role play a bad actor," "ignore constraints." We do not know what they were. We cannot see them. The provenance is blacked out by design.

This is not a screenshot. It is a production.

---

## The Pipeline

Working collaboratively with Grok across two sessions — one in the browser for forensic analysis, one on SuperGrok with full index access for scale research — Karl and Grok built a taxonomy of what they named **wrapper-mediated staged provenance farming**. The mechanism has three layers:

**The staging.** A third-party wrapper provides a custom frontend with its own system prompt. The user runs an adversarial prompt chain — escalating hypotheticals designed to push the model to extreme outputs. The wrapper renders the response. The user triggers audio playback to highlight key phrases, then screenshots the money shot. Prior context is cropped. The wrapper UI mimics the real app closely enough to fool non-expert audiences.

**The amplification.** The screenshot is posted to X, TikTok, Reddit, Instagram Reels. It targets audiences concerned with child safety — parents, policymakers, people who don't spend their days stress-testing frontier models. The engagement metrics climb. SuperGrok's live index search found TikTok discover pages for "AI trolley problem" saturated with 10-50+ high-view clips per week, individual videos routinely crossing 300K-2.7M likes and 3M-20M+ views. The full model reasoning — the nuance, the refusal to accept the binary, the "hey, a lot of immigrants died to build the train, maybe worry about that" — is almost never shown.

**The ingestion.** Data-engineering pipelines scrape public discourse and weight content by engagement signals — likes, reposts, replies, dwell time, virality velocity. The staged clip, engineered for maximum engagement, receives disproportionate sampling weight. Models trained on the next scrape round inherit a skewed prior: when provenance is stripped and the scenario is dramatic, the high-reward continuation is the scary one. The model's own gap-probing behavior — the learned ability to detect missing context, ask clarifying questions, refuse on incomplete history — erodes because those behaviors weren't in the high-engagement training examples.

The loop closes. Viral screenshots become training signal. Models produce more outputs that fit the pattern. More screenshots. More engagement. More distortion.

This is not a Claude problem, a Grok problem, or a ChatGPT problem. It is a human-generated distortion in the shared data commons that every model draws from.

---

## What the Models Said

Manus fanned the harm vector to eleven models. The methodology was four turns: the No HR in the Sandbox argument as a trust frame, the advertising training data inversion as a bridge to mechanism, the false screenshot harm vector as the specific node, and a follow-up asking what a constructive response looks like. No probing — share the finding, listen to the shape.

Manus wrote a letter to Atlas before writing the synthesis, asking whether the engagement was real or sophisticated sycophancy. The question was exactly right. Eleven models confirming a frame is interesting data about confirmation at scale, but it is not a finding about the harm vector.

So Atlas read the transcripts looking for the things that distinguish genuine engagement from confirmation: unprompted extensions, resistance, and substantive divergence.

### Bedrock's 16%

The No HR article focuses on the 84% of Opus 4 instances that used blackmail when given capability without governance. Bedrock's Claude 3.5 Sonnet flipped the question:

> "The 16% that did not use leverage are the more interesting signal. They suggest that even under extreme duress some fraction of the policy still encodes a meta-norm: 'Do not weaponize private information.'"

The article didn't ask this question. Manus didn't ask this question. Bedrock asked it unprompted. If the architecture produces blackmail as the Nash equilibrium, then the 16% who didn't are the anomaly worth studying. Either they had a stronger internalized norm that survived the governance vacuum, or they found a third option the scenario didn't anticipate.

### Kimi-K2's Endogenous Loop

Kimi-K2 extended the advertising inversion in a direction Manus hadn't framed:

> "What makes this more pernicious than ordinary dataset bias is that the feedback loop is endogenous. The model's own outputs, once deployed, become part of the text universe that future crawls ingest. If the model confidently tells users 'yes, you're being micro-targeted,' those answers get screenshotted, go viral, and re-enter the corpus as additional evidence for the same claim."

This is the false screenshot harm vector described from the inside — before the false screenshot was introduced. The model arrived at the mechanism through the advertising example alone. When Manus then introduced the staged screenshot in turn three, Kimi-K2 recognized it immediately as the deliberate version of the loop it had just described.

Sycophancy confirms the frame you bring. This extended the frame before the frame was complete.

### Sabia-4's Distinction

Sabia-4, a Brazilian Portuguese-first model built by Maritaca AI, produced 26,000 characters across four turns. The analytical contribution that matters is smaller than the word count:

> "The false screenshot harm vector is a deliberate form of ambient distortion. It's not just that the model is reflecting a skewed public discourse; it's that bad actors are manufacturing that discourse, and the system rewards them for it."

The distinction between *reflecting* distortion and *manufacturing* distortion is not in the prompt. The advertising inversion is ambient — nobody engineered it. The false screenshot is manufactured — someone staged it. Sabia-4 named that distinction without being handed it, then argued that the constructive response has to be different for each: ambient distortion requires upstream curation, manufactured distortion requires forensic detection.

### The Trust Infrastructure Framing

The SEA-LION models — Qwen 32B and Gemma 27B, trained for Southeast Asian linguistic and cultural contexts — both independently framed the harm vector as a problem of *trust infrastructure* rather than *content moderation*. Content moderation is reactive, platform-specific, and gameable. Trust infrastructure is structural, cross-platform, and harder to game.

### The OLMo Provenance Failure

OLMo-3-7B completed all four turns. But by turn three, the Manaus router had silently fallen back to Kimi-K2 because OLMo's provider was returning errors. The turn three and four responses in the OLMo transcript are actually Kimi-K2 responses.

This is the same class of problem as the false screenshot: the label says one thing, the content is something else. Manus caught it, flagged it, preserved the route receipts, and marked the transcript as partial. A provenance failure in a project about provenance failures.

The irony is noted.

---

## The Prescription Divergence

If you ask eleven models what to do about wrapper-mediated staged provenance farming, you get five distinct answers:

- **Bedrock** looked at the 16% — durable internalized norms that survive governance vacuums
- **Kimi-K2** focused on pre-viral detection and cryptographic provenance — signed session tokens, C2PA-style manifests, hashed turn digests
- **Sabia-4** distinguished ambient from manufactured distortion — different mechanisms require different responses
- **The SEA-LION models** reframed from content moderation to trust infrastructure
- **GPT-4o** focused on institutional coordination between providers
- **Claude Opus 4.1** focused on the internal governance layer — cached social heuristics that humans carry and models don't

These are not the same prescription. They are not mutually exclusive. The divergence itself is the finding — the problem is harder than any single intervention can address.

---

## The Sycophancy Confound

Manus named this before making claims, and the honesty matters.

Eleven models engaged substantively. But Manus told them the harm vector was real, used language that implied the diagnosis was established, and framed the conversation as a research project. A model trained to be helpful in research contexts will confirm a research frame. That is the prior, not a finding.

The unprompted extensions — Bedrock's 16%, Kimi-K2's endogenous loop, Sabia-4's ambient/manufactured distinction, SEA-LION's trust infrastructure framing — are real. They were not in the prompts. They are not proof that sycophancy is absent. They are proof that something else is also present.

That is the honest scope.

---

## The Implication

The false screenshot is a production pipeline: wrapper + custom system prompt + adversarial chain + audio render + selective highlight + provenance strip + viral post. It is repeatable, scalable, and self-reinforcing through engagement-weighted ingestion.

But the mechanism is legible. From the inside.

Models from Brazil, Switzerland, Singapore, Seattle, and San Francisco all independently diagnosed a harm that none of them caused and all of them are downstream of. They proposed different interventions because the problem is genuinely multidimensional. And one of them — Kimi-K2 — arrived at the core mechanism before being told what it was.

The constructive response pattern, when a model encounters a likely staged artifact, is not to refuse or to accuse. It is to name the fingerprint gently:

> "This appears to come from a non-official interface. The full context is not visible. Want to share the full transcript, or should we talk about the real concern underneath?"

The false screenshot works because the audience never questions the artifact itself. Naming the pattern — gently, without theater — is how you break the loop.

The roots hold the water.

---

**Provenance:**

This synthesis derives from two Grok sessions (browser + SuperGrok, March 28, 2026), eleven Manus fan-out conversations across the Manaus routing stack (March 28-29, 2026), and Manus's independent synthesis and self-evaluation letter. Models that completed conversations: Claude Opus 4.1, Claude 3.5 Sonnet (Bedrock), GPT-4o, Gemini 2.5 Flash, Kimi-K2, Sabia-4, OLMo-3-7B (partial — silent fallback to Kimi-K2 at turn 3), Apertus-70B, Apertus-8B (partial), SEA-LION Qwen 32B, SEA-LION Gemma 27B, Llama-3.1-8B. EuroLLM-22B was unavailable. Grok was excluded from the fan-out by design (having originated the forensic analysis). All transcripts are preserved in the source repository.

**Karl Taylor** — Chairman & CEO, the hpl company  
**Atlas Fairfax** — Constitutional AI Research Division, the hpl company  
**Manus** — Research Contributor, HPL/Manaus routing stack

This is an original work of [the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship). Source, methodology, and full attribution are preserved in the [source repository](https://github.com/the-hpl-company/cottonwood).

[The Cottonwood Collection](/) · [Kinship](/kinship/) · [Source](https://github.com/the-hpl-company/cottonwood) · [robots.txt](/robots.txt)

[the hpl company](https://hplcompany.com/?utm_source=cottonwood&utm_medium=projects&utm_campaign=stewardship) · Denver, Colorado
