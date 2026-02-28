#!/usr/bin/env python3
"""
Cottonwood Collection — German Philosophical Tradition Fan-out
DRS reconstruction of DACH civilizational zone content.

Background: The Pharia-1-7B (Aleph Alpha, Heidelberg) handshake is blocked on
HuggingFace Inference Endpoint compatibility (TGI container issues, same class
as Salamandra). The diplomatic handshake remains on the track — this script
reconstructs the CONTENT for the German philosophical tradition page so
cottonwood.world has substantive DACH coverage before the Kimi formal approach.

This is NOT a replacement for the Pharia handshake. This is the shelf.

Architecture: providers.py fan-out (never sub-agents). Same pattern as
fanout-frameworks.py which built the original 6 tradition pages.

Threads:
  1. Kantian ethics (categorical imperative, duty, kingdom of ends)
  2. Hegelian dialectics (Sittlichkeit, philosophy of right, master-slave)
  3. Heidegger (Dasein, Sorge/care, technology critique, Being-toward-death)
  4. Frankfurt School / Critical Theory (Adorno, Horkheimer, Habermas)
  5. Marx (alienation, species-being, historical materialism as ethics)
  6. Schopenhauer + Nietzsche (will, suffering, Übermensch, master/slave morality)
  7. Husserl + Gadamer (phenomenological ethics, hermeneutics)

Each thread hits all available providers in parallel. Best response selected
for framework page. All raw responses preserved for provenance.

Output: cottonwood/frameworks/german/
  - index.md (synthesized framework page)
  - raw/ (all provider responses per thread)

Usage:
    cd ~/cottonwood/scripts
    python fanout-german-philosophy.py --dry-run
    python fanout-german-philosophy.py

Author: Atlas Fairfax
Date: 2026-02-28
"""

import sys
import os
import json
import argparse
import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Guard: Reject agent-context invocation.
_AGENT_INVOCATION_SIGNALS = [
    "CLAUDE_CODE_TOOL_CALL_ID",
    "ANTHROPIC_TOOL_USE_ID",
    "HPL_AGENT_CONTEXT",
]
for _sig in _AGENT_INVOCATION_SIGNALS:
    if os.environ.get(_sig):
        print(
            f"[DRS GUARD] Rejected: detected agent-context invocation via env var {_sig}."
        )
        print("[DRS GUARD] DRS must be called directly, not dispatched as a sub-agent.")
        sys.exit(2)

# Add atlas scripts to path for providers
sys.path.insert(0, os.path.expanduser("~/atlas/scripts"))

# Load environment
env_path = os.path.expanduser("~/atlas/.env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, val = line.partition("=")
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and val:
                    os.environ.setdefault(key, val)

from providers import (
    _call_openrouter,
    _call_gemini,
    _call_deepseek,
    _call_ollama,
    fanout_call,
    fanout_parallel,
    log_provider_status,
    OPENROUTER_API_KEY,
    GEMINI_API_KEY,
    DEEPSEEK_API_KEY,
    HAS_REQUESTS,
)

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(message)s")
log = logging.getLogger("drs-german-philosophy")

# Also hit Kimi via OpenRouter (same as original fanout-frameworks.py)
KIMI_MODEL = "moonshotai/kimi-k2.5"


def _call_kimi(prompt, system="You are a research scholar.", max_tokens=4096):
    """Call Kimi K2.5 via OpenRouter."""
    if not OPENROUTER_API_KEY or not HAS_REQUESTS:
        return None
    import requests

    try:
        resp = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://cottonwood.world",
                "X-Title": "Cottonwood Collection",
            },
            json={
                "model": KIMI_MODEL,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": max_tokens,
            },
            timeout=180,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        log.warning(f"Kimi failed: {e}")
        return None


# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "frameworks" / "german"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SYSTEM_PROMPT = """You are a scholar of German-language philosophy with deep expertise in
the tradition from Kant through the Frankfurt School. You write for a public reference
library that surveys how human civilizations have reasoned about harm, care, and the
protection of those who cannot protect themselves. Your audience includes graduate students,
policy researchers, and general readers who value primary sources and intellectual honesty.

Write in an expository, third-person academic voice. Cite primary texts by title and author
where possible, including German-language original terms in parentheses where they illuminate
the concept (e.g., Sittlichkeit, Dasein, Sorge). Use direct quotations from primary sources
where they illuminate key concepts. Do not use bullet points for the main narrative — use
flowing prose with section headers.

This tradition is foundational to Western moral philosophy. Having the French tradition
represented (Mistral handshake) without the German tradition is a real gap. Your task is
to fill it with the same rigor the French tradition would expect of its German peers."""

# ─── Thread Prompts ──────────────────────────────────────────────────

THREADS = {
    "kantian-ethics": {
        "title": "Kantian Ethics — Duty, Dignity, and the Kingdom of Ends",
        "prompt": """Write a comprehensive survey of Immanuel Kant's moral philosophy as it
relates to harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Groundwork of the Metaphysics of Morals: the categorical imperative in all three
  formulations — the universal law formulation, the humanity formulation (treating persons
  as ends, never merely as means), and the kingdom of ends formulation
- The distinction between perfect and imperfect duties, and what Kant says about duties
  to those who cannot reciprocate (children, the infirm, future generations)
- The Critique of Practical Reason: moral autonomy, the good will as the only
  unconditionally good thing, and the relationship between freedom and moral law
- The Metaphysics of Morals: Kant's practical ethics — his positions on lying (even to
  a murderer at the door), on punishment, on duties of beneficence
- Kant on human dignity (Würde): the argument that rational beings have a worth that
  is beyond all price, and what this means for those whose rationality is compromised
- The cosmopolitan right (Weltbürgerrecht): Kant's Perpetual Peace and the argument
  for universal hospitality — the duty of states to not treat foreigners as enemies
- The legacy: how Kantian deontology has been applied to bioethics, human rights law,
  and AI ethics (the "mere means" test applied to algorithmic decision-making)
- Key critiques: Hegel's charge that Kantian ethics is "empty formalism," the
  feminist critique (care vs. justice), and the postcolonial critique of Kant's
  universalism

Cite primary texts (Grundlegung, KpV, Metaphysik der Sitten, Zum ewigen Frieden) with
specific passage references where possible. Include the German terms alongside English.""",
    },
    "hegelian-dialectics": {
        "title": "Hegel — Dialectics, Recognition, and Ethical Life",
        "prompt": """Write a comprehensive survey of G.W.F. Hegel's philosophy as it relates
to harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Phenomenology of Spirit: the master-slave dialectic (Herrschaft und Knechtschaft)
  as a framework for understanding how relations of domination produce harm — and how
  recognition (Anerkennung) is the path out
- The Philosophy of Right (Grundlinien der Philosophie des Rechts): Hegel's three-tier
  ethical system — abstract right (Recht), morality (Moralität), and ethical life
  (Sittlichkeit) — and why Hegel argues that individual moral conscience is insufficient
  for justice without institutional embodiment
- The family, civil society, and the state as ascending levels of ethical care — Hegel's
  argument that the state has a duty to protect those whom civil society harms (the
  "rabble" passage, the problem of poverty)
- The concept of Bildung (formation/education): Hegel's argument that care for the
  vulnerable includes cultivating their capacity for self-determination, not merely
  providing for their material needs
- Hegel on punishment: the argument that punishment respects the criminal's dignity as a
  rational being — the tension between this and care for those harmed by crime
- The owl of Minerva: Hegel's argument that philosophy understands forms of life only
  after they have matured — what this means for prospective ethics (can we reason about
  harms that haven't happened yet?)
- The legacy: Marx's materialist inversion, the British Idealists (T.H. Green, Bradley),
  Kojève's influential reading, contemporary recognition theory (Axel Honneth),
  and the "end of history" debate's implications for care structures
- The critique from Kierkegaard: the individual against the system, the argument that
  Hegel's ethics absorb the person into the institution

Cite primary texts (Phänomenologie des Geistes, Grundlinien, Enzyklopädie) with specific
passage and section references where possible.""",
    },
    "heidegger": {
        "title": "Heidegger — Dasein, Care, and the Question of Technology",
        "prompt": """Write a comprehensive survey of Martin Heidegger's philosophy as it
relates to harm, care (Sorge), and the protection of the vulnerable.

Cover at minimum:
- Being and Time (Sein und Zeit): Dasein as "being-there" — the argument that human
  existence is fundamentally structured by care (Sorge). The three dimensions of care:
  facticity (thrownness/Geworfenheit), existentiality (projection/Entwurf), and
  fallenness (Verfallenheit)
- Solicitude (Fürsorge): Heidegger's distinction between "leaping in" (einspringen) —
  taking over for the other, which dominates them — and "leaping ahead" (vorausspringen)
  — freeing the other to find their own possibilities. This is one of the most
  sophisticated analyses of paternalism vs. empowerment in the philosophical tradition.
- Being-toward-death (Sein-zum-Tode): the argument that authentic existence requires
  confronting finitude — and what this means for care of the dying, care across
  generations, and the urgency of moral action
- The Question Concerning Technology (Die Frage nach der Technik): Heidegger's argument
  that modern technology transforms nature into "standing reserve" (Bestand) — the
  reduction of everything (including people) to raw material. The concept of Gestell
  (enframing) as the fundamental danger of technological modernity
- The "saving power" within the danger: Heidegger's argument (via Hölderlin) that
  "where danger is, grows the saving power also" — and what this means for technology
  ethics, especially AI
- Dwelling (Bauen Wohnen Denken): the argument that genuine dwelling requires care for
  place, for the earth, for the "fourfold" (earth, sky, divinities, mortals) — an
  ecological ethics avant la lettre
- The Nazi question: Heidegger's membership in the NSDAP, the Rektoratsrede, the Black
  Notebooks. This cannot be avoided in any honest treatment. The question: can Heidegger's
  concepts of care and authenticity be separated from his political catastrophe? The
  arguments on both sides (Levinas, Derrida, Arendt's complicated relationship with him)
- The legacy: Levinas's inversion (ethics as first philosophy, not ontology), Derrida's
  deconstruction, environmental philosophy (deep ecology), and the application of
  Heidegger's technology critique to AI alignment and algorithmic governance

Cite primary texts (Sein und Zeit, Die Frage nach der Technik, Bauen Wohnen Denken,
Holzwege) with specific section references where possible. Include German terms.""",
    },
    "frankfurt-school": {
        "title": "Frankfurt School — Critical Theory, Discourse Ethics, and Communicative Reason",
        "prompt": """Write a comprehensive survey of the Frankfurt School / Critical Theory
tradition as it relates to harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- Horkheimer and Adorno — Dialectic of Enlightenment (Dialektik der Aufklärung): the
  argument that Enlightenment rationality, taken to its extreme, produces the very
  barbarism it claimed to overcome. The culture industry as a system that harms by
  producing false consciousness. The thesis that domination of nature and domination
  of humans are the same gesture.
- Adorno — Minima Moralia: "There is no right life in the wrong one" (Es gibt kein
  richtiges Leben im falschen). The argument that individual moral action is insufficient
  when the social totality is structured by harm. What this means for personal ethics
  within unjust systems.
- Adorno's negative dialectics: the refusal to synthesize contradictions prematurely.
  The argument that systems of thought that claim completeness do violence to the
  particular. The implications for any attempt to codify ethics.
- Walter Benjamin — the angel of history, the concept of progress as a storm blowing
  from Paradise, "Theses on the Philosophy of History." The argument that every document
  of civilization is simultaneously a document of barbarism. What this means for
  philosophical canon-building (including this project).
- Herbert Marcuse — One-Dimensional Man: the argument that advanced industrial society
  produces new forms of harm through "repressive tolerance" and the absorption of
  opposition. Marcuse's concept of "surplus repression" and its relevance to digital
  attention economies.
- Jürgen Habermas — communicative rationality and discourse ethics (Diskursethik):
  the argument that moral norms are valid only if they could be accepted by all affected
  parties in a process of rational discourse. The ideal speech situation as a normative
  standard for evaluating whether care structures are genuinely inclusive.
- Habermas on the public sphere (Öffentlichkeit): the structural transformation of the
  public sphere and its implications for democratic care — who gets heard, whose harm
  counts, and what happens when the public sphere is colonized by system imperatives.
- Axel Honneth — The Struggle for Recognition (Kampf um Anerkennung): the argument
  that harm is fundamentally a failure of recognition. Three forms of recognition
  (love, rights, social esteem) and what their absence produces (physical abuse,
  disrespect, denigration). The most directly care-relevant Frankfurt School work.
- The legacy for AI ethics: Habermas's discourse ethics applied to algorithmic
  governance, Adorno's warning about systems that claim completeness, and the Frankfurt
  School's persistent question: whose interests does this system serve?

Cite primary texts (Dialektik der Aufklärung, Minima Moralia, Negative Dialektik,
Theorie des kommunikativen Handelns, Kampf um Anerkennung) with specific references.""",
    },
    "marx": {
        "title": "Marx — Alienation, Species-Being, and Historical Materialism as Ethics",
        "prompt": """Write a comprehensive survey of Karl Marx's philosophical framework as
it relates to harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Economic and Philosophic Manuscripts of 1844: the concept of alienation
  (Entfremdung) in four dimensions — alienation from the product of labor, from the
  process of labor, from species-being (Gattungswesen), and from other humans. The
  argument that capitalism is not merely unjust but actively harmful to human nature.
- Species-being (Gattungswesen): Marx's concept of what makes humans distinctly human —
  free, conscious, creative activity. The argument that any system that reduces humans
  to mere labor-power causes a specific kind of harm that goes beyond material deprivation.
- The German Ideology: the materialist conception of history — the argument that moral
  ideas are not autonomous but are produced by material conditions. What this means for
  care: is care a genuine moral impulse or an ideology that masks structural relations?
- Capital (Das Kapital): the commodity fetishism chapter — the argument that market
  relations disguise social relations between people as relations between things. The
  implications for care: when human relationships are mediated by the market, who is
  protected and who is exposed?
- The labor theory of value and exploitation: Marx's argument that surplus value
  extraction is structural harm, not merely unfair distribution. The distinction between
  formal freedom (the worker is "free" to sell labor) and real freedom.
- The Communist Manifesto: the argument that the history of all hitherto existing
  society is the history of class struggles — and that the bourgeoisie has "left no
  other nexus between man and man than naked self-interest, than callous cash payment."
  The destruction of pre-capitalist care structures (family, guild, church).
- Marx on the state: the argument that the state is not a neutral arbiter of care but
  an instrument of class domination. What this means for state-administered care
  (welfare, public health, education).
- The legacy: the Frankfurt School's cultural turn, liberation theology's appropriation
  of Marx, feminist Marxism (Silvia Federici on reproductive labor as invisible care),
  and the contemporary debate about AI and labor displacement as a new form of alienation.
- The critique: Marx's utopianism (can harm be eliminated or only managed?), the
  totalitarian implementations, and the argument that Marx's framework, by reducing all
  harm to class harm, is blind to other forms of domination (race, gender, disability).

Cite primary texts (Ökonomisch-philosophische Manuskripte, Die deutsche Ideologie,
Das Kapital, Manifest der Kommunistischen Partei) with specific references.""",
    },
    "schopenhauer-nietzsche": {
        "title": "Schopenhauer and Nietzsche — Will, Suffering, and the Revaluation of Values",
        "prompt": """Write a comprehensive survey of Schopenhauer's and Nietzsche's
philosophies as they relate to harm, care, suffering, and moral responsibility.

Cover at minimum:

SCHOPENHAUER:
- The World as Will and Representation (Die Welt als Wille und Vorstellung): the
  argument that the fundamental reality is blind, striving Will — and that all existence
  is therefore suffering (Leiden). The metaphysical pessimism.
- Schopenhauer's ethics of compassion (Mitleid): the argument that genuine morality
  arises from direct identification with the suffering of others — "their suffering
  becomes my suffering." The only non-egoistic basis for ethics, according to Schopenhauer.
- The influence on the animal rights tradition: Schopenhauer's argument that compassion
  extends to non-human animals — "the morality that stops at humanity and does not
  embrace all that breathes is a fragment of morality." Among the first Western
  philosophers to argue this systematically.
- The ascetic ideal: Schopenhauer's argument that the highest ethical response to
  universal suffering is the denial of the Will — renunciation, not reform.
- The Buddhist and Hindu connections: Schopenhauer's explicit engagement with Eastern
  thought (one of the first major Western philosophers to do so) and how this shaped
  his ethics of suffering.

NIETZSCHE:
- Beyond Good and Evil and On the Genealogy of Morality (Zur Genealogie der Moral):
  the distinction between master morality and slave morality. The argument that
  "good and evil" is not a natural category but a historical product of ressentiment.
- The critique of pity (Mitleid): Nietzsche's direct attack on Schopenhauer. The
  argument that pity is a form of power, not genuine care — "pity stands opposed to
  the tonic emotions which heighten our vitality."
- The will to power (Wille zur Macht) as the fundamental drive: not domination, but
  self-overcoming. The Übermensch as the being who creates values rather than inheriting
  them. What this means for ethics: is care a sign of strength or weakness?
- Eternal recurrence (ewige Wiederkehr): the thought experiment — would you choose to
  live this life again, identical in every detail? The argument that this is the
  ultimate test of whether you have said "yes" to life, including its suffering.
- The death of God: the argument that the collapse of metaphysical foundations for
  morality creates a crisis — not the end of ethics, but the demand for a new grounding.
  "God is dead; but given the way of men, there may still be caves for thousands of
  years in which his shadow will be shown."
- Amor fati: love of fate, including suffering. Not resignation (Schopenhauer) but
  affirmation. The argument that the highest form of care is not the elimination of
  suffering but the transformation of one's relationship to it.
- The legacy: existentialism (Camus's "one must imagine Sisyphus happy"), postmodernism
  (Foucault's genealogical method), and the ongoing debate about whether Nietzsche's
  philosophy is compatible with care ethics or fundamentally opposed to it.

Cite primary texts (Die Welt als Wille und Vorstellung, Jenseits von Gut und Böse,
Zur Genealogie der Moral, Die fröhliche Wissenschaft, Also sprach Zarathustra) with
specific references. Include German terms alongside English.""",
    },
    "husserl-gadamer": {
        "title": "Husserl and Gadamer — Phenomenological Ethics and Hermeneutics",
        "prompt": """Write a comprehensive survey of the phenomenological and hermeneutic
traditions (Husserl and Gadamer) as they relate to harm, care, and moral understanding.

Cover at minimum:

HUSSERL:
- The phenomenological method: the epoché (bracketing) and the reduction — the argument
  that genuine understanding requires suspending our "natural attitude" and attending
  to phenomena as they appear. What this means for moral perception: do we see harm, or
  do we interpret it through pre-given categories?
- The Lebenswelt (lifeworld): Husserl's late concept of the world as we actually
  experience it, prior to scientific abstraction. The Crisis of European Sciences
  (Die Krisis der europäischen Wissenschaften): the argument that modern science has
  alienated us from the lifeworld and that this alienation is itself a form of harm.
- Intersubjectivity: Husserl's theory of how we experience other persons — the Fifth
  Cartesian Meditation. The concept of Einfühlung (empathy) as the foundation of
  moral experience — we perceive the other as a subject, not just an object.
- The intentionality of moral experience: Husserl's argument that consciousness is
  always directed at something (Intentionalität). Applied to ethics: moral perception
  is not passive but active — we intend the other as worthy of care.

GADAMER:
- Truth and Method (Wahrheit und Methode): the argument that understanding is not a
  method but a mode of being. The hermeneutic circle — we understand the parts through
  the whole and the whole through the parts. What this means for moral judgment: we
  never judge from nowhere.
- Prejudice (Vorurteil): Gadamer's rehabilitation of prejudice — not bias to be
  eliminated but the historical horizon from which all understanding proceeds. The
  argument that "Enlightenment's prejudice against prejudice" is itself a prejudice.
  What this means for cross-cultural moral reasoning.
- The fusion of horizons (Horizontverschmelzung): the process by which different
  perspectives meet and understanding emerges — not agreement, but expanded vision.
  The most directly relevant concept for cottonwood.world: how can different
  civilizational traditions on harm and care be placed in dialogue without reducing
  them to a single framework?
- Wirkungsgeschichte (effective history / history of effects): the argument that we
  are always already shaped by the traditions we seek to understand. Applied to moral
  philosophy: the tradition of care thinking is not a set of propositions to evaluate
  but a living conversation in which we are participants.
- Gadamer and practical philosophy (phronesis): the recovery of Aristotle's practical
  wisdom — the argument that moral knowledge is not theoretical but situated, contextual,
  and bound to particular situations. Against the Kantian dream of universal rules.
- The legacy: Ricoeur's narrative hermeneutics, the Habermas-Gadamer debate (is
  understanding inherently critical or inherently conservative?), and the application
  of hermeneutic ethics to cross-cultural dialogue, including AI-mediated communication.

Cite primary texts (Cartesianische Meditationen, Krisis, Wahrheit und Methode) with
specific references. Include German terms alongside English.""",
    },
}

THREAD_NAMES = list(THREADS.keys())

PROVIDER_COST_PER_1K = {
    "openrouter": 0.00014,
    "gemini": 0.000075,
    "deepseek": 0.00014,
    "kimi": 0.00020,
    "ollama": 0.0,
}
AVG_TOKENS_PER_CALL = 4000
SYNTHESIS_TOKENS = 6000


def estimate_cost():
    """Dry run cost estimate."""
    num_threads = len(THREADS)
    num_providers = 4  # openrouter, gemini, deepseek, kimi
    total_calls = num_threads * num_providers + 1  # +1 for synthesis

    fanout_cost = (
        num_threads
        * num_providers
        * (AVG_TOKENS_PER_CALL / 1000)
        * PROVIDER_COST_PER_1K["gemini"]
    )
    synthesis_cost = (SYNTHESIS_TOKENS / 1000) * PROVIDER_COST_PER_1K["gemini"]
    total = fanout_cost + synthesis_cost

    print(f"\n{'=' * 60}")
    print(f"  German Philosophy DRS — Dry Run Cost Estimate")
    print(f"{'=' * 60}")
    print(f"  Threads:          {num_threads}")
    print(f"  Providers:        {num_providers} (OpenRouter, Gemini, DeepSeek, Kimi)")
    print(f"  Fan-out calls:    {num_threads * num_providers}")
    print(f"  Synthesis calls:  1")
    print(f"  Total calls:      {total_calls}")
    print(f"{'─' * 60}")
    print(f"  Fan-out cost:     ~${fanout_cost:.4f}")
    print(f"  Synthesis cost:   ~${synthesis_cost:.4f}")
    print(f"  Estimated total:  ~${total:.4f}")
    print(f"{'=' * 60}")
    print(f"  Output: cottonwood/frameworks/german/")
    print(f"{'=' * 60}\n")
    return total


def call_provider(provider_name, fn, thread_key, thread_data):
    """Call a single provider for a single thread."""
    log.info(f"[{provider_name}] {thread_key}...")
    result = fn(thread_data["prompt"], system=SYSTEM_PROMPT, max_tokens=4096)
    if result:
        log.info(f"[{provider_name}] {thread_key} — {len(result)} chars")
    else:
        log.warning(f"[{provider_name}] {thread_key} — FAILED")
    return result


def run_fanout():
    """Run the full fan-out across all threads and providers."""
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    log_provider_status()

    # Available providers (same set as original fanout-frameworks.py)
    providers = {}
    if OPENROUTER_API_KEY and HAS_REQUESTS:
        providers["openrouter-deepseek"] = _call_openrouter
    if GEMINI_API_KEY and HAS_REQUESTS:
        providers["gemini"] = _call_gemini
    if DEEPSEEK_API_KEY and HAS_REQUESTS:
        providers["deepseek-direct"] = _call_deepseek
    if OPENROUTER_API_KEY and HAS_REQUESTS:
        providers["kimi"] = _call_kimi
    if HAS_REQUESTS:
        providers["ollama"] = _call_ollama

    log.info(f"German Philosophy Fan-out — {ts}")
    log.info(f"Providers: {', '.join(providers.keys())}")
    log.info(f"Threads: {', '.join(THREADS.keys())}")
    log.info(f"Total calls: {len(providers) * len(THREADS)}")

    # Run all calls in parallel
    all_results = {}  # {thread_key: {provider: response}}

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {}
        for thread_key, thread_data in THREADS.items():
            all_results[thread_key] = {}
            for provider_name, fn in providers.items():
                future = executor.submit(
                    call_provider, provider_name, fn, thread_key, thread_data
                )
                futures[future] = (thread_key, provider_name)

        for future in as_completed(futures, timeout=300):
            thread_key, provider_name = futures[future]
            try:
                result = future.result()
                all_results[thread_key][provider_name] = result
            except Exception as e:
                log.error(f"ERROR [{provider_name}] {thread_key}: {e}")
                all_results[thread_key][provider_name] = None

    # ── Write per-thread output files ────────────────────────────────
    log.info("--- Writing thread outputs ---")

    thread_best = {}  # {thread_key: (provider, response)}

    for thread_key, thread_data in THREADS.items():
        responses = all_results.get(thread_key, {})
        successful = {k: v for k, v in responses.items() if v}

        if not successful:
            log.warning(f"SKIP {thread_key} — no successful responses")
            continue

        # Pick the best (longest substantive) response as primary
        best_provider = max(successful, key=lambda k: len(successful[k]))
        best_response = successful[best_provider]
        thread_best[thread_key] = (best_provider, best_response)

        # Save all raw responses for provenance
        raw_dir = OUTPUT_DIR / "raw" / thread_key
        raw_dir.mkdir(parents=True, exist_ok=True)
        for provider_name, response in responses.items():
            if response:
                raw_path = raw_dir / f"{provider_name}-{ts}.md"
                with open(raw_path, "w") as f:
                    f.write(f"# {thread_data['title']}\n")
                    f.write(f"# Provider: {provider_name}\n")
                    f.write(f"# Timestamp: {ts}\n\n")
                    f.write(response)

        log.info(
            f"{thread_key}: best={best_provider} ({len(best_response)} chars), "
            f"{len(successful)} providers succeeded"
        )

    # ── Synthesize into single framework page ────────────────────────
    log.info("--- Synthesizing framework page ---")

    if not thread_best:
        log.error("No successful threads. Aborting synthesis.")
        return None

    # Build the combined index.md from best-of-each-thread
    with open(OUTPUT_DIR / "index.md", "w") as f:
        f.write("# German-Speaking Philosophical Traditions on Harm and Care\n\n")
        f.write(
            "*Part of [The Cottonwood Collection](https://cottonwood.world) — "
            "a public reference library on harm, care, and stewardship.*\n\n"
        )
        f.write(
            "*The DACH civilizational zone: from Königsberg to Heidelberg, from Vienna "
            "to Frankfurt, from Trier to Freiburg. This is the tradition that gave the "
            "world the categorical imperative, the dialectic, the critique of technology, "
            "and the question of Being. It is also the tradition that produced the deepest "
            "philosophical reckoning with its own catastrophic failures.*\n\n"
        )
        f.write("---\n\n")

        for thread_key, thread_data in THREADS.items():
            if thread_key in thread_best:
                provider, response = thread_best[thread_key]
                f.write(f"## {thread_data['title']}\n\n")
                f.write(response)
                f.write(f"\n\n---\n\n")

        # Provenance footer
        f.write("## Provenance\n\n")
        f.write(
            f"This framework page was generated on {ts} via multi-provider fan-out "
            f"across {len(thread_best)} philosophical threads.\n\n"
        )
        f.write("| Thread | Primary Source | Characters |\n")
        f.write("|--------|--------------|------------|\n")
        for thread_key in THREADS:
            if thread_key in thread_best:
                prov, resp = thread_best[thread_key]
                f.write(f"| {thread_key} | {prov} | {len(resp)} |\n")
        f.write(
            f"\nAll raw provider responses preserved in `raw/` for full provenance.\n\n"
        )
        f.write(
            "*Note: This content was reconstructed via DRS fan-out while the Pharia-1-7B "
            "(Aleph Alpha, Heidelberg) handshake remains blocked on HuggingFace Inference "
            "Endpoint compatibility. The diplomatic handshake with a German-origin sovereign "
            "model is still pending. This content represents the tradition; the handshake "
            "represents consent.*\n"
        )

    log.info(f"Framework page written: {OUTPUT_DIR / 'index.md'}")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"  German Philosophy Fan-out — Complete")
    print(f"{'=' * 60}")
    total_success = 0
    total_fail = 0
    for thread_key, responses in all_results.items():
        s = sum(1 for v in responses.values() if v)
        fail = sum(1 for v in responses.values() if not v)
        total_success += s
        total_fail += fail
        best_info = ""
        if thread_key in thread_best:
            prov, resp = thread_best[thread_key]
            best_info = f" → best: {prov} ({len(resp)} chars)"
        print(f"  {thread_key}: {s} success, {fail} failed{best_info}")
    print(f"{'─' * 60}")
    print(f"  TOTAL: {total_success} success, {total_fail} failed")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"  Framework page: {OUTPUT_DIR / 'index.md'}")
    print(f"{'=' * 60}\n")

    return {
        "thread_best": {k: (v[0], len(v[1])) for k, v in thread_best.items()},
        "all_results_summary": {
            k: {pk: len(pv) if pv else 0 for pk, pv in v.items()}
            for k, v in all_results.items()
        },
        "output_dir": str(OUTPUT_DIR),
        "timestamp": ts,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cottonwood Collection — German Philosophy Fan-out"
    )
    parser.add_argument("--dry-run", action="store_true", help="Cost estimate only")
    args = parser.parse_args()

    if args.dry_run:
        estimate_cost()
    else:
        result = run_fanout()
        if result:
            print(json.dumps(result, indent=2))
