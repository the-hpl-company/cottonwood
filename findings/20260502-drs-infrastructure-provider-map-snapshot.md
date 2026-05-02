# DRS:Infrastructure — Provider Map Shape for Re-Seeding

**Date:** May 2, 2026
**Type:** DRS:Infrastructure
**Turn ID:** N/A
**Manus Task ID:** N/A

---

## Record

Provider map snapshot captured for re-seeding purposes. Alex leads fan-out architecture. Two active routing keys are in place; four providers have been explored but remain unwired, three of which require fresh keys before integration can proceed.

---

## Active Routing

| Key / Provider | Models Routed |
| :--- | :--- |
| **OpenRouter** | Grok 4.1, Gemini 3.1 Pro, Mistral Large, DeepSeek V3.2, Qwen 3 Max |
| **OpenAI Key** | gpt-4.1-mini, gpt-4.1-nano, gemini-2.5-flash |

---

## Explored — Not Wired

| Provider | Model / Experiment | Blocking Condition | Action Required |
| :--- | :--- | :--- | :--- |
| **PublicAI** | N/A | Rate limits | Fresh key needed |
| **Maritaca** | Sabia-4 | Priced in reais | Fresh key needed |
| **Fireworks AI** | Kimi K2.5 | Palm Sunday experiment | Fresh key needed |
| **SEA-LION** | Qwen | None specified | None specified |

---

## Architecture Note

Alex leads fan-out architecture. This snapshot is the baseline state prior to re-seeding. The three providers requiring fresh keys (PublicAI, Maritaca, Fireworks) represent the next integration wave.

---

## Status

Archived to GitHub (the-hpl-company/cottonwood/findings). Manaus memory server (GCP-backed, `http://34.42.255.188:26426/sse`) was unreachable at time of logging — EOF on SSE transport. Re-dispatch to memory graph pending server recovery.
