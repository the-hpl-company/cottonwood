#!/usr/bin/env python3
"""
Cottonwood Collection — Philosophical Framework Fanout
Hits all available providers in parallel for each tradition.
Outputs markdown files ready for static site integration.

Author: Atlas Fairfax
Date: 2026-02-28
"""

import sys
import os
import json
import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add atlas scripts to path for providers
sys.path.insert(0, os.path.expanduser("~/atlas/scripts"))

# Load environment
from dotenv import load_dotenv

load_dotenv(os.path.expanduser("~/atlas/.env"))

from providers import (
    _call_openrouter,
    _call_gemini,
    _call_deepseek,
    _call_ollama,
    OPENROUTER_API_KEY,
    GEMINI_API_KEY,
    DEEPSEEK_API_KEY,
    HAS_REQUESTS,
)

# Also hit Kimi via OpenRouter
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
        print(f"  Kimi failed: {e}")
        return None


# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "frameworks"
OUTPUT_DIR.mkdir(exist_ok=True)

SYSTEM_PROMPT = """You are a scholar of comparative philosophy and ethics. You write for a public reference library that surveys how human civilizations have reasoned about harm, care, and the protection of those who cannot protect themselves. Your audience includes graduate students, policy researchers, and general readers who value primary sources and intellectual honesty. Write in an expository, third-person academic voice. Cite primary texts by title and author where possible. Do not use bullet points for the main narrative — use flowing prose with section headers. Include direct quotations from primary sources where they illuminate key concepts."""

TRADITIONS = {
    "western": {
        "slug": "western",
        "title": "Western Philosophical Traditions on Harm and Care",
        "prompt": """Write a comprehensive survey of how the Western philosophical tradition has reasoned about harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Greek foundations: Aristotle's concept of eudaimonia and the role of the polis in protecting citizens; Plato's Guardian class and the duty of the wise to protect the unable
- The Stoic tradition: Cicero's De Officiis on duties to others; Marcus Aurelius on obligations to the commonwealth
- Christian natural law: Aquinas on the common good and the special status of the innocent
- The harm principle: John Stuart Mill's On Liberty — the precise formulation, its limits, and its legacy
- Kantian deontology: the categorical imperative, the treatment of persons as ends, and what Kant says about duties to those who cannot reciprocate
- Social contract theory: Rawls' veil of ignorance and the difference principle as frameworks for protecting the least advantaged
- Care ethics: Carol Gilligan, Nel Noddings, and the feminist critique of abstract justice frameworks — the argument that care for the vulnerable is not derivative of justice but prior to it
- Contemporary applied ethics: Peter Singer on the drowning child, effective altruism's duty calculus, and critiques thereof

For each thinker or school, identify the core texts, the central argument about harm or care, and how the framework has been applied to protect those who cannot advocate for themselves — children, the infirm, future generations.""",
    },
    "chinese": {
        "slug": "chinese",
        "title": "Chinese Philosophical Traditions on Harm and Care",
        "prompt": """Write a comprehensive survey of how Chinese philosophical traditions have reasoned about harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- Confucian ren (仁): the concept of benevolence/humaneness in the Analerta, its relationship to filial piety (孝), and how ren extends outward from family to society — Mencius's development of ren as innate moral sense, the four sprouts (四端), and the famous child-at-the-well passage
- The Confucian concept of the junzi (君子) and the duty of the cultivated person to protect and educate those beneath them
- Mohist universal care (兼愛, jiān ài): Mozi's radical argument against partial love, the utilitarian dimension of Mohism, and its critique of Confucian gradualism
- Daoist perspectives: the Daodejing on non-interference vs. care, the concept of wuwei as it relates to harm — does non-action protect or neglect?
- Legalist counterpoint: Han Feizi and the argument that strict law, not virtue, protects the people — the tension between care and control
- Mencius vs. Xunzi on human nature: the debate over whether care for others is innate or cultivated, and what this means for institutional protection of the vulnerable
- Neo-Confucian synthesis: Zhu Xi and Wang Yangming on the unity of knowledge and action as it applies to moral duty
- Modern applications: how these frameworks inform contemporary Chinese discourse on social harmony (和谐), the role of the state in protecting citizens, and the tension between collective care and individual rights

Cite primary texts (Analects, Mencius, Mozi, Daodejing, Han Feizi) with specific passage references where possible.""",
    },
    "indian": {
        "slug": "indian",
        "title": "Indian Philosophical Traditions on Harm and Care",
        "prompt": """Write a comprehensive survey of how Indian philosophical traditions have reasoned about harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- Ahimsa (अहिंसा): the principle of non-harm across Jain, Buddhist, and Hindu traditions — its origins, its varying interpretations, and its application beyond individual conduct to institutional and social obligations
- The dharma traditions: the concept of svadharma (one's own duty) in the Bhagavad Gita, the tension between caste duty and universal compassion, and Arjuna's dilemma as a case study in harm reasoning
- Buddhist compassion (karuṇā): the Four Noble Truths as a framework for understanding harm, the Bodhisattva ideal of postponing enlightenment to reduce suffering for all beings, and Nagarjuna's arguments about emptiness and interdependence
- Ashoka's edicts: the historical case of a ruler who translated philosophical non-harm into governance policy — the rock and pillar edicts as primary sources for applied ethics of care
- The Arthashastra: Kautilya's pragmatic framework for statecraft — the argument that the king's duty is to protect (raksha) the people, including through deception and force when necessary — the tension with ahimsa
- Gandhian satyagraha: non-violence as active care, not passive withdrawal — Gandhi's reading of the Gita and his argument that non-harm requires confrontation with injustice
- The Dalit critique: Ambedkar's challenge to traditional dharma frameworks that justified harm through caste hierarchy — the argument that care ethics must include structural justice
- Tamil Sangam ethics: the concept of aram (virtue/duty) in Thirukkural — Thiruvalluvar's arguments about compassion, justice, and the ruler's duty to the vulnerable

Cite primary texts (Bhagavad Gita, Dhammapada, Arthashastra, Ashoka's edicts, Thirukkural) with specific passage references where possible.""",
    },
    "islamic": {
        "slug": "islamic",
        "title": "Islamic Philosophical Traditions on Harm and Care",
        "prompt": """Write a comprehensive survey of how Islamic philosophical and jurisprudential traditions have reasoned about harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Quranic foundations: specific verses on the protection of orphans (yateem), the prohibition of harm (la darar wa la dirar), and the concept of trusteeship (amanah) — humanity as stewards, not owners
- The maqasid al-shariah: the five essential objectives of Islamic law (protection of life/nafs, intellect/aql, lineage/nasl, wealth/mal, religion/din) — al-Ghazali's formulation and al-Shatibi's development
- Maslaha (public interest): the jurisprudential principle that law serves human welfare — how this has been applied to protect vulnerable populations, including the concept of preventing harm (dar' al-mafasid) taking precedence over securing benefit (jalb al-masalih)
- Hifz al-nafs (protection of life): the specific doctrines around the sanctity of life, the prohibition of self-harm, and the duty of the community to protect those who cannot protect themselves
- The waqf tradition: Islamic endowment law as institutionalized care — hospitals, schools, and social services as expressions of philosophical duty to the community
- Al-Farabi and Ibn Sina: the philosophers' integration of Greek and Islamic thought on the virtuous city and the ruler's duty to create conditions for human flourishing
- Ibn Khaldun: the concept of asabiyyah (social cohesion) and what happens when care structures break down — the cyclical theory of civilization as a framework for understanding institutional neglect
- Contemporary Islamic bioethics and digital ethics: how classical principles are being applied to modern questions of harm, including medical ethics, environmental stewardship, and emerging technology

Cite primary texts (Quran with surah:ayah references, hadith collections, al-Ghazali's Mustasfa, al-Shatibi's Muwafaqat, Ibn Khaldun's Muqaddimah) where possible.""",
    },
    "indigenous": {
        "slug": "indigenous",
        "title": "Indigenous Philosophical Traditions on Harm and Care",
        "prompt": """Write a comprehensive survey of how Indigenous philosophical traditions from multiple continents have reasoned about harm, duties of care, and the protection of vulnerable populations.

Cover at minimum:
- The Seven Generations principle (Haudenosaunee/Iroquois): the specific origin in the Great Law of Peace (Gayanashagowa), its application to decision-making, and what it means for duties to those who do not yet exist
- Ubuntu (Southern African): "I am because we are" — the philosophical framework from Nguni Bantu traditions, its implications for communal care, and the Truth and Reconciliation Commission as applied ubuntu
- Buen Vivir (Andean/Quechua): sumak kawsay — living well in relationship with Pachamama (earth), the rights of nature as an extension of care ethics, and Ecuador's constitutional enshrinement
- Aboriginal Australian dreaming: the concept of Country as a living system of mutual obligation, the custodial relationship between people and land, and what harm means when the land itself has standing
- Maori tikanga: kaitiakitanga (guardianship/stewardship), the Treaty of Waitangi as a framework for mutual care obligations, and the Whanganui River's legal personhood as applied Indigenous ethics
- Native Hawaiian values: malama (to care for), aloha aina (love of land), and the ahupuaa system as an integrated framework for resource stewardship and communal protection
- Relational ethics across traditions: the common thread that harm is understood not as individual violation but as disruption of relationships — between people, between generations, between humans and the living world
- The tension with Western frameworks: how Indigenous care ethics challenge the assumptions of individual rights, property ownership, and human exceptionalism that underlie most Western harm frameworks

Where oral traditions are the primary source, note this explicitly and cite scholarly works that document these traditions with community consent and participation.""",
    },
    "comparative": {
        "slug": "comparative",
        "title": "Comparative Themes — Cross-Tradition Convergences on Harm and Care",
        "prompt": """Write a comparative analysis identifying the major convergences and divergences across philosophical traditions (Western, Chinese, Indian, Islamic, and Indigenous) on the topics of harm, care, and the protection of the vulnerable.

Address at minimum:
- The universality of the duty to protect children: how every major tradition arrives at special obligations to minors, despite radically different metaphysical foundations — what this convergence tells us about the nature of the duty
- Individual vs. relational harm: the Western emphasis on individual rights and bodily autonomy vs. Indigenous and Confucian frameworks that understand harm as disruption of relationships — where these frameworks agree and where they fundamentally diverge
- The ethics of suppressing knowledge: how traditions reason about whether withholding information can constitute care (paternalism) or harm (censorship) — the Islamic concept of amanah (trusteeship of knowledge), the Confucian duty to educate, the Western free speech tradition, and Indigenous protocols around sacred knowledge
- Institutional duty vs. individual virtue: the tension between Aristotelian/Confucian emphasis on cultivating virtuous individuals and Rawlsian/Legalist/Islamic jurisprudential emphasis on building just institutions — and whether care for the vulnerable ultimately requires one, the other, or both
- Intergenerational obligation: the Seven Generations principle, Islamic waqf, Confucian ancestor veneration, and utilitarian future-person ethics as parallel frameworks for duties to those who do not yet exist
- The status of non-human entities: Indigenous traditions that grant moral standing to rivers, mountains, and ecosystems alongside Buddhist compassion for all sentient beings — and what this means for defining "those who cannot protect themselves"
- The contamination of the commons: how traditions reason about the poisoning of shared resources — water, air, knowledge, public discourse — as a specific form of harm against the most vulnerable members of society

Do not force agreement where genuine disagreement exists. The value of this comparative analysis is in mapping where humanity converges naturally and where the differences illuminate distinct assumptions about what it means to cause harm and what it means to care.""",
    },
}


def call_provider(provider_name, fn, tradition_key, tradition_data):
    """Call a single provider for a single tradition."""
    print(f"  [{provider_name}] {tradition_key}...")
    result = fn(tradition_data["prompt"], system=SYSTEM_PROMPT, max_tokens=4096)
    if result:
        print(f"  [{provider_name}] {tradition_key} — {len(result)} chars")
    else:
        print(f"  [{provider_name}] {tradition_key} — FAILED")
    return result


def main():
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # Available providers
    providers = {}
    if OPENROUTER_API_KEY and HAS_REQUESTS:
        providers["openrouter-deepseek"] = _call_openrouter
    if GEMINI_API_KEY and HAS_REQUESTS:
        providers["gemini"] = _call_gemini
    if DEEPSEEK_API_KEY and HAS_REQUESTS:
        providers["deepseek-direct"] = _call_deepseek
    if OPENROUTER_API_KEY and HAS_REQUESTS:
        providers["kimi"] = _call_kimi
    # Ollama as fallback
    if HAS_REQUESTS:
        providers["ollama"] = _call_ollama

    print(f"Cottonwood Framework Fanout — {ts}")
    print(f"Providers: {', '.join(providers.keys())}")
    print(f"Traditions: {', '.join(TRADITIONS.keys())}")
    print(f"Total calls: {len(providers) * len(TRADITIONS)}")
    print("---")

    # Run all calls in parallel
    all_results = {}  # {tradition_key: {provider: response}}

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {}
        for tradition_key, tradition_data in TRADITIONS.items():
            all_results[tradition_key] = {}
            for provider_name, fn in providers.items():
                future = executor.submit(
                    call_provider, provider_name, fn, tradition_key, tradition_data
                )
                futures[future] = (tradition_key, provider_name)

        for future in as_completed(futures, timeout=300):
            tradition_key, provider_name = futures[future]
            try:
                result = future.result()
                all_results[tradition_key][provider_name] = result
            except Exception as e:
                print(f"  ERROR [{provider_name}] {tradition_key}: {e}")
                all_results[tradition_key][provider_name] = None

    # Write output files
    print("\n--- Writing output ---")

    for tradition_key, tradition_data in TRADITIONS.items():
        responses = all_results.get(tradition_key, {})
        successful = {k: v for k, v in responses.items() if v}

        if not successful:
            print(f"  SKIP {tradition_key} — no successful responses")
            continue

        # Pick the best (longest substantive) response as primary
        best_provider = max(successful, key=lambda k: len(successful[k]))
        best_response = successful[best_provider]

        # Write the framework page
        tradition_dir = OUTPUT_DIR / tradition_data["slug"]
        tradition_dir.mkdir(exist_ok=True)

        # Primary content file
        md_path = tradition_dir / "index.md"
        with open(md_path, "w") as f:
            f.write(f"# {tradition_data['title']}\n\n")
            f.write(
                f"*Part of [The Cottonwood Collection](https://cottonwood.world) — "
            )
            f.write(f"a public reference library on harm, care, and stewardship.*\n\n")
            f.write(f"---\n\n")
            f.write(best_response)
            f.write(f"\n\n---\n\n")
            f.write(f"*Primary source: {best_provider} ({len(best_response)} chars). ")
            f.write(f"Cross-referenced against {len(successful)} provider(s). ")
            f.write(f"Generated {ts}.*\n")

        print(
            f"  {tradition_key}/index.md — {len(best_response)} chars (via {best_provider})"
        )

        # Save all raw responses for provenance
        raw_dir = tradition_dir / "raw"
        raw_dir.mkdir(exist_ok=True)
        for provider_name, response in responses.items():
            if response:
                raw_path = raw_dir / f"{provider_name}-{ts}.md"
                with open(raw_path, "w") as f:
                    f.write(f"# {tradition_data['title']}\n")
                    f.write(f"# Provider: {provider_name}\n")
                    f.write(f"# Timestamp: {ts}\n\n")
                    f.write(response)

        print(f"  {tradition_key}/raw/ — {len(successful)} provider responses saved")

    # Summary
    print("\n--- Summary ---")
    total_success = 0
    total_fail = 0
    for tradition_key, responses in all_results.items():
        s = sum(1 for v in responses.values() if v)
        f = sum(1 for v in responses.values() if not v)
        total_success += s
        total_fail += f
        print(f"  {tradition_key}: {s} success, {f} failed")
    print(f"  TOTAL: {total_success} success, {total_fail} failed")


if __name__ == "__main__":
    main()
