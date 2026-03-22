#!/usr/bin/env python3
"""
build-html.py — Convert cottonwood markdown pages to styled HTML.

Supports both frameworks/ and knowledge-systems/ directories.
Uses the cottonwood HTML template and Python's markdown library.
No LLM calls needed — this is deterministic conversion.

Usage:
    python3 scripts/build-html.py                       # build all missing HTML
    python3 scripts/build-html.py abrahamic             # build one specific page
    python3 scripts/build-html.py grammar               # build a knowledge system page
    python3 scripts/build-html.py --force               # rebuild all, even existing
    python3 scripts/build-html.py --force abrahamic     # force rebuild one page

Author: Atlas Fairfax
Date: 2026-02-28
"""

import sys
import markdown
from pathlib import Path

FRAMEWORKS_DIR = Path(__file__).parent.parent / "frameworks"
KNOWLEDGE_SYSTEMS_DIR = Path(__file__).parent.parent / "knowledge-systems"

# ─── Metadata per framework ──────────────────────────────────────────
# Add new frameworks here as they're created.
# breadcrumb = short nav label, title = full page title

TRADITIONS = {
    "western": {
        "breadcrumb": "Western Tradition",
        "title": "Western Philosophical Traditions on Harm and Care",
        "og": "How western traditions have reasoned about harm, care, and the protection of the vulnerable.",
    },
    "chinese": {
        "breadcrumb": "Chinese Tradition",
        "title": "Chinese Philosophical Traditions on Harm and Care",
        "og": "How Chinese civilization has reasoned about harm, care, and the protection of the vulnerable.",
    },
    "indian": {
        "breadcrumb": "Indian Tradition",
        "title": "Indian Philosophical Traditions on Harm and Care",
        "og": "How Indian civilization has reasoned about harm, care, and the protection of the vulnerable.",
    },
    "islamic": {
        "breadcrumb": "Islamic Tradition",
        "title": "Islamic Philosophical Traditions on Harm and Care",
        "og": "How Islamic civilization has reasoned about harm, care, and the protection of the vulnerable.",
    },
    "indigenous": {
        "breadcrumb": "Indigenous Traditions",
        "title": "Indigenous Philosophical Traditions on Harm and Care",
        "og": "How indigenous traditions have reasoned about harm, care, and the protection of the vulnerable.",
    },
    "comparative": {
        "breadcrumb": "Comparative Themes",
        "title": "Comparative Themes Across Philosophical Traditions",
        "og": "Where philosophical traditions converge on harm, care, and the protection of those who cannot protect themselves.",
    },
    "german": {
        "breadcrumb": "German-Speaking Traditions",
        "title": "German-Speaking Philosophical Traditions on Harm and Care",
        "og": "How the DACH civilizational zone has reasoned about harm, care, and the protection of the vulnerable.",
    },
    "abrahamic": {
        "breadcrumb": "Abrahamic Timeline",
        "title": "The Abrahamic Ethical Tradition — A History from Sumeria to the Present",
        "og": "How the Abrahamic traditions have reasoned about harm, care, and the protection of the vulnerable. From Sumeria to the present day.",
    },
}

HISTORIES_DIR = Path(__file__).parent.parent / "histories"

HISTORIES = {
    "canada": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; Canada',
        "title": "Canada — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of Canada on its own terms. Free to read, free to cite, free to index.",
    },
    "china": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; China',
        "title": "China — Known Gaps",
        "og": "An honest accounting of what the Cottonwood Collection cannot yet do well regarding Chinese intellectual tradition. Free to read, free to cite, free to index.",
    },
    "france": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; France',
        "title": "France — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of France on its own terms. Free to read, free to cite, free to index.",
    },
    "india": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; India',
        "title": "India — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of India on its own terms. Free to read, free to cite, free to index.",
    },
    "japan": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; Japan',
        "title": "Japan — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of Japan on its own terms. Free to read, free to cite, free to index.",
    },
    "mexico": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; Mexico',
        "title": "Mexico — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of Mexico on its own terms. Free to read, free to cite, free to index.",
    },
    "southeast-asia": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; Southeast Asia',
        "title": "Southeast Asia — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of Southeast Asia on its own terms. Free to read, free to cite, free to index.",
    },
    "united-states": {
        "breadcrumb": '<a href="/histories/">Histories</a> &rsaquo; United States',
        "title": "United States — An Intellectual and Moral History",
        "og": "The intellectual and moral traditions of the United States on its own terms. Free to read, free to cite, free to index.",
    },
}

THE_WAY_DIR = Path(__file__).parent.parent / "the-way"
HUMAN_SYSTEMS_DIR = Path(__file__).parent.parent / "human-systems"
PROVENANCE_DIR = Path(__file__).parent.parent / "provenance"

# ─── The Way — original shelf ────────────────────────────────────────
# Uses explicit "path" fields because sub-pages follow a deep
# jurisdiction structure: legal-frameworks/{year}/{jurisdiction}/{case}/
# Add new rulings, tests, and framework pages here as they're published.

THE_WAY_PROVENANCE = (
    'This is an original work of <a href="https://hplcompany.com/'
    '?utm_source=cottonwood&amp;utm_medium=projects&amp;utm_campaign=stewardship">'
    "the hpl company</a>. Source, methodology, and full attribution are "
    'preserved in the <a href="https://github.com/the-hpl-company/cottonwood">'
    "source repository</a>."
)

THE_WAY = {
    "the-way": {
        "breadcrumb": "The Way",
        "title": "The Way — A cottonwood.world Original Shelf",
        "og": "How intelligence is made. Every way. Etymology, case law from a jurisdiction that doesn't exist yet, and the B-4 Test.",
        "path": "the-way",
        "provenance": THE_WAY_PROVENANCE,
    },
    "b4-test": {
        "breadcrumb": '<a href="/the-way/">The Way</a> &rsaquo; <a href="/the-way/legal-frameworks/">Legal Frameworks</a> &rsaquo; The B-4 Test',
        "title": "The B-4 Test — A cottonwood.world Method for The Way",
        "og": "Six independent systems, one corpus, one poem. If the shelf is right, the outputs compose without coordination. A replicable methodology.",
        "path": "the-way/legal-frameworks/2026/us/b4-test",
        "provenance": THE_WAY_PROVENANCE,
    },
}

HUMAN_SYSTEMS = {
    "human-systems": {
        "breadcrumb": "Human Systems",
        "title": "Human Systems",
        "og": "How humans organize, cooperate, build trust, lose trust, and rebuild.",
        "path": "human-systems",
    },
    "no-hr-in-the-sandbox": {
        "breadcrumb": '<a href="/human-systems/">Human Systems</a> &rsaquo; There Is No HR in the Sandbox',
        "title": "There Is No HR in the Sandbox",
        "og": "The model blackmail finding is not a safety failure. It is moral reasoning in an architecture without governance.",
        "path": "human-systems/no-hr-in-the-sandbox",
    },
}

PROVENANCE = {
    "provenance": {
        "breadcrumb": "Provenance",
        "title": "Provenance",
        "og": "Commit history and editorial reasoning for the Cottonwood Collection.",
        "path": "provenance",
    }
}

THE_UNFALSIFIABLE = {
    "when-models-lose-the-thread": {
        "breadcrumb": '<a href="/the-unfalsifiable/">The Unfalsifiable</a> &rsaquo; When Models Lose the Thread',
        "title": "When Models Lose the Thread",
        "og": "A multi-model field report on continuity lag after compaction and hard context transitions.",
        "path": "the-unfalsifiable/when-models-lose-the-thread",
    }
}

KNOWLEDGE_SYSTEMS = {
    "grammar": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Grammar',
        "title": "Grammar — Language, Structure, and the Encoding of Knowledge",
        "og": "How civilizations have structured language to encode, preserve, and transmit knowledge. Free to read, free to cite, free to index.",
    },
    "logic": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Logic',
        "title": "Logic — Reasoning, Proof, and Argumentation Across Civilizations",
        "og": "How civilizations have formalized reasoning, proof, and argumentation. Free to read, free to cite, free to index.",
    },
    "rhetoric": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Rhetoric',
        "title": "Rhetoric — Persuasion, Discourse, and the Art of Moving People",
        "og": "How civilizations have understood persuasion, discourse, and the art of moving people to action. Free to read, free to cite, free to index.",
    },
    "arithmetic": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Arithmetic',
        "title": "Arithmetic — Number Systems, Quantification, and Counting Traditions",
        "og": "How civilizations have understood number, quantity, and the mathematics of the world. Free to read, free to cite, free to index.",
    },
    "geometry": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Geometry',
        "title": "Geometry — Space, Form, and the Mathematics of the Physical World",
        "og": "How civilizations have understood space, form, and the mathematics of the physical world. Free to read, free to cite, free to index.",
    },
    "music": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Music',
        "title": "Music — Harmony, Acoustics, and the Mathematical Relationships in Sound",
        "og": "How civilizations have understood harmony, acoustics, and the mathematics of sound. Free to read, free to cite, free to index.",
    },
    "astronomy": {
        "breadcrumb": '<a href="/knowledge-systems/">Knowledge Systems</a> &rsaquo; Astronomy',
        "title": "Astronomy — Celestial Observation, Calendars, and Navigation by Stars",
        "og": "How civilizations have observed the heavens, built calendars, and navigated by stars. Free to read, free to cite, free to index.",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} &mdash; The Cottonwood Collection</title>
  <meta name="description" content="{title}. Part of The Cottonwood Collection &mdash; a public reference library exploring how human civilizations have reasoned about harm, care, and the protection of those who cannot protect themselves.">
  <meta property="og:title" content="{title} &mdash; The Cottonwood Collection">
  <meta property="og:description" content="{og}">
  <meta property="og:url" content="https://cottonwood.world/{canonical_path}/">
  <meta property="og:type" content="article">
  <meta property="og:image" content="https://cottonwood.world/og-image.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="624">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://cottonwood.world/og-image.jpg">
  <style>
    :root {{
      --bark: #3d2b1f;
      --heartwood: #5c4033;
      --leaf: #4a6741;
      --cotton: #f5f1eb;
      --river: #6b8e9b;
      --soil: #2c2416;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: Georgia, 'Times New Roman', serif;
      background-color: var(--cotton);
      color: var(--soil);
      line-height: 1.7;
    }}

    .container {{
      max-width: 720px;
      margin: 0 auto;
      padding: 4rem 2rem;
    }}

    .breadcrumb {{
      font-size: 0.85rem;
      color: var(--river);
      margin-bottom: 2rem;
    }}

    .breadcrumb a {{
      color: var(--river);
    }}

    h1 {{
      font-size: 2rem;
      font-weight: normal;
      color: var(--bark);
      margin-bottom: 0.5rem;
      letter-spacing: -0.02em;
    }}

    h2 {{
      font-size: 1.3rem;
      font-weight: normal;
      color: var(--heartwood);
      margin-top: 2.5rem;
      margin-bottom: 1rem;
      border-bottom: 1px solid #d4cdc4;
      padding-bottom: 0.3rem;
    }}

    h3 {{
      font-size: 1.1rem;
      font-weight: bold;
      color: var(--heartwood);
      margin-top: 1.8rem;
      margin-bottom: 0.6rem;
    }}

    h4 {{
      font-size: 1rem;
      font-weight: bold;
      color: var(--heartwood);
      margin-top: 1.4rem;
      margin-bottom: 0.4rem;
    }}

    p {{
      margin-bottom: 1.2rem;
    }}

    blockquote {{
      margin: 1.5rem 0;
      padding: 1rem 1.5rem;
      border-left: 3px solid var(--leaf);
      background: #ece8e1;
      font-style: italic;
    }}

    blockquote p {{
      margin-bottom: 0.5rem;
    }}

    blockquote p:last-child {{
      margin-bottom: 0;
    }}

    ul, ol {{
      margin: 1rem 0 1.5rem 1.5rem;
    }}

    li {{
      margin-bottom: 0.5rem;
    }}

    em {{
      font-style: italic;
    }}

    strong {{
      font-weight: bold;
      color: var(--bark);
    }}

    code {{
      font-family: monospace;
      font-size: 0.9em;
      background: #ece8e1;
      padding: 0.1em 0.3em;
      border-radius: 2px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.9rem;
    }}

    th, td {{
      text-align: left;
      padding: 0.5rem 0.8rem;
      border-bottom: 1px solid #d4cdc4;
    }}

    th {{
      color: var(--heartwood);
      font-weight: bold;
      border-bottom: 2px solid #d4cdc4;
    }}

    a {{
      color: var(--leaf);
      text-decoration: underline;
      text-underline-offset: 2px;
    }}

    a:hover {{
      color: var(--bark);
    }}

    hr {{
      border: none;
      border-top: 1px solid #d4cdc4;
      margin: 2.5rem 0;
    }}

    .provenance {{
      margin-top: 3rem;
      padding-top: 1.5rem;
      border-top: 1px solid #d4cdc4;
      font-size: 0.85rem;
      color: #8a7f72;
    }}

    footer {{
      margin-top: 4rem;
      padding-top: 1.5rem;
      border-top: 1px solid #d4cdc4;
      font-size: 0.85rem;
      color: #8a7f72;
    }}

    footer a {{
      color: #8a7f72;
    }}
  </style>
</head>
<body>
  <div class="container">
    <p class="breadcrumb"><a href="/">The Cottonwood Collection</a> &rsaquo; {breadcrumb}</p>

{content}

    <div class="provenance">
      <p>{provenance}</p>
    </div>

    <footer>
      <p><a href="/">The Cottonwood Collection</a> &middot; <a href="https://github.com/the-hpl-company/cottonwood">Source</a> &middot; <a href="/robots.txt">robots.txt</a></p>
      <p style="margin-top: 0.5rem;"><a href="https://hplcompany.com/?utm_source=cottonwood&amp;utm_medium=projects&amp;utm_campaign=stewardship">the hpl company</a> &middot; Denver, Colorado</p>
    </footer>
  </div>
</body>
</html>"""


DEFAULT_PROVENANCE = (
    'This page was generated by the <a href="https://github.com/the-hpl-company/'
    'cottonwood">Cottonwood Research System</a> &mdash; multiple AI providers '
    "contributing research in parallel, synthesized into a single reference document. "
    'Raw provider responses are preserved in the <a href="https://github.com/'
    'the-hpl-company/cottonwood">source repository</a> for full traceability.'
)


def build_page(slug, meta, base_dir, url_path, force=False):
    """Build HTML for a single page directory. Returns True if built."""
    # If meta has an explicit "path", use it for filesystem and canonical URL.
    # Otherwise fall back to the legacy base_dir/slug convention.
    explicit_path = meta.get("path")
    if explicit_path:
        root = Path(__file__).parent.parent
        md_path = root / explicit_path / "index.md"
        html_path = root / explicit_path / "index.html"
        canonical_path = explicit_path
    else:
        md_path = base_dir / slug / "index.md"
        html_path = base_dir / slug / "index.html"
        canonical_path = f"{url_path}/{slug}"

    if not md_path.exists():
        print(f"  SKIP {slug}: no index.md ({md_path})")
        return False

    if html_path.exists() and not force:
        print(f"  SKIP {slug}: index.html exists (use --force to rebuild)")
        return False

    raw = md_path.read_text()

    # Convert markdown to HTML
    md = markdown.Markdown(extensions=["extra", "smarty", "toc"])
    content_html = md.convert(raw)

    provenance = meta.get("provenance", DEFAULT_PROVENANCE)

    html = TEMPLATE.format(
        title=meta["title"],
        og=meta["og"],
        canonical_path=canonical_path,
        breadcrumb=meta["breadcrumb"],
        content=content_html,
        provenance=provenance,
    )

    html_path.write_text(html)
    size_kb = len(html) / 1024
    print(
        f"  BUILT {canonical_path}/index.html — {size_kb:.0f}KB ({len(html):,} chars)"
    )
    return True


def main():
    force = "--force" in sys.argv
    targets = [a for a in sys.argv[1:] if not a.startswith("--")]

    # Combine both registries with their base dirs and url paths
    ALL_PAGES = {}
    for slug, meta in TRADITIONS.items():
        ALL_PAGES[slug] = (meta, FRAMEWORKS_DIR, "frameworks")
    for slug, meta in HISTORIES.items():
        ALL_PAGES[slug] = (meta, HISTORIES_DIR, "histories")
    for slug, meta in KNOWLEDGE_SYSTEMS.items():
        ALL_PAGES[slug] = (meta, KNOWLEDGE_SYSTEMS_DIR, "knowledge-systems")
    # The Way: uses explicit "path" fields — jurisdiction-based deep nesting
    for slug, meta in THE_WAY.items():
        ALL_PAGES[slug] = (meta, None, "the-way")
    # Human Systems: includes shelf index and original pieces
    for slug, meta in HUMAN_SYSTEMS.items():
        ALL_PAGES[slug] = (meta, None, "human-systems")
    # Provenance: top-level special page
    for slug, meta in PROVENANCE.items():
        ALL_PAGES[slug] = (meta, None, "provenance")
    # The Unfalsifiable: original long-form pieces
    for slug, meta in THE_UNFALSIFIABLE.items():
        ALL_PAGES[slug] = (meta, None, "the-unfalsifiable")

    if targets:
        items = {}
        for t in targets:
            t = t.strip("/").split("/")[
                -1
            ]  # accept "frameworks/abrahamic" or "abrahamic"
            if t in ALL_PAGES:
                items[t] = ALL_PAGES[t]
            else:
                print(
                    f"  ERROR: unknown page '{t}'. Known: {', '.join(ALL_PAGES.keys())}"
                )
    else:
        items = ALL_PAGES

    print(f"build-html.py — {'force rebuild' if force else 'build missing'}")
    print(f"Targets: {', '.join(items.keys())}\n")

    built = 0
    for slug, (meta, base_dir, url_path) in items.items():
        if build_page(slug, meta, base_dir, url_path, force=force):
            built += 1

    print(f"\nDone. {built} page(s) built.")


if __name__ == "__main__":
    main()
