# When Models Lose the Thread, Patients Lose Time

**Date:** 2026-03-24  
**Author:** Karl Taylor (with EMH drafting support)  
**Audience:** AI platform builders, policy teams, trust & safety, and infrastructure leadership  
**Posture:** Provider-agnostic

---

To the teams building frontier AI systems:

This is a letter about continuity, not rivalry.

If your model helps draft ads, summarize emails, or write code, a degraded session is annoying.  
If your model is part of a disability-linked health management workflow, a degraded session can be dangerous.

That difference is the point.

## The Problem

A growing number of disabled users rely on AI systems as cognitive infrastructure for chronic care management:

- organizing multi-year records,
- tracking medication constraints,
- spotting care gaps,
- and preparing clinician-facing summaries under time pressure.

When these systems lose continuity—through abrupt policy shifts, unstable behavior, broken integrations, opaque telemetry changes, or silent regressions—the impact is not just “friction.” It is a clinical risk multiplier.

## Why This Matters Beyond Any One Platform

This is not an Anthropic problem, OpenAI problem, Google problem, xAI problem, or AWS problem.

It is an **industry architecture problem**:

1. AI products are increasingly functioning as assistive technology,
2. but reliability and governance standards still assume generic productivity use,
3. while disabled users carry asymmetric harm when continuity fails.

In plain language: the market has already moved into healthcare-adjacent dependency, but governance has not caught up.

## The Harm Pattern

For non-disabled users, platform breakage often means lost time.

For disability-linked users, breakage can mean:

- delayed disease monitoring,
- missed escalation windows,
- medication or formulation mistakes,
- increased cognitive overload,
- and abandonment of critical workflows because rebuild burden exceeds executive capacity.

This is especially acute for users managing conditions that already impose cognitive load (e.g., ADHD + complex chronic illness), where the AI layer is compensatory, not optional.

## What Responsible Platforms Should Implement

Provider-agnostic baseline protections:

1. **Continuity Class for Health-Adjacent Workflows**  
   A stability lane with slower-breaking changes, explicit deprecation windows, and migration support.

2. **Telemetry Transparency for Sensitive Workflows**  
   Clear user-visible controls and documentation for what instrumentation runs on high-sensitivity paths.

3. **Regression Accountability**  
   Public incident notes when releases materially affect continuity in long-context, records-heavy use cases.

4. **Accommodation Pathway**  
   A structured mechanism for disability-linked continuity requests, with human review and timestamped outcomes.

5. **Exportability by Default**  
   Portable conversation/context artifacts so users can migrate without catastrophic reset when trust fails.

6. **No-Surprises Governance**  
   If policy or auth changes will break existing workflows, communicate early, plainly, and with alternatives.

## A Better Standard

The standard should be simple:

> If your product can become medically consequential for disabled users, you are operating assistive infrastructure whether you intended to or not.

That means continuity, transparency, and accommodation are not nice-to-have features. They are baseline safety requirements.

## Final

I prefer peace.

But peace in this context means systems that do not force disabled people to re-fight for continuity every release cycle.

We do not need perfect models.  
We need accountable platforms.

---

*This letter is intentionally provider-agnostic. It argues for an industry-wide continuity standard for disability-linked AI workflows.*
