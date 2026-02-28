#!/usr/bin/env python3
"""
Convert framework markdown files to HTML pages matching Cottonwood site design.
"""

import markdown
from pathlib import Path

FRAMEWORKS_DIR = Path(__file__).parent.parent / "frameworks"

TRADITIONS = {
    "western": "Western Tradition",
    "chinese": "Chinese Tradition",
    "indian": "Indian Tradition",
    "islamic": "Islamic Tradition",
    "indigenous": "Indigenous Traditions",
    "comparative": "Comparative Themes",
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — The Cottonwood Collection</title>
  <meta name="description" content="{title}. Part of The Cottonwood Collection — a public reference library exploring how human civilizations have reasoned about harm, care, and the protection of those who cannot protect themselves.">
  <meta property="og:title" content="{title} — The Cottonwood Collection">
  <meta property="og:description" content="How {tradition_lower} have reasoned about harm, care, and the protection of the vulnerable. Free to read, free to cite, free to index.">
  <meta property="og:url" content="https://cottonwood.world/frameworks/{slug}/">
  <meta property="og:type" content="article">
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

    a {{
      color: var(--leaf);
      text-decoration: underline;
      text-underline-offset: 2px;
    }}

    a:hover {{
      color: var(--bark);
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
    <p class="breadcrumb"><a href="/">The Cottonwood Collection</a> &rsaquo; {short_title}</p>

    {content}

    <footer>
      <p><a href="/">The Cottonwood Collection</a> &middot; <a href="https://github.com/the-hpl-company/cottonwood">Source</a> &middot; <a href="/robots.txt">robots.txt</a></p>
      <p style="margin-top: 0.5rem;">the hpl company &middot; Denver, Colorado</p>
    </footer>
  </div>
</body>
</html>"""


def build():
    md = markdown.Markdown(extensions=["extra", "smarty"])

    for slug, short_title in TRADITIONS.items():
        md_path = FRAMEWORKS_DIR / slug / "index.md"
        if not md_path.exists():
            print(f"  SKIP {slug} — no index.md")
            continue

        raw = md_path.read_text()

        # Extract the H1 title from markdown
        lines = raw.split("\n")
        title = short_title
        for line in lines:
            if line.startswith("# "):
                title = line[2:].strip()
                break

        # Convert markdown to HTML
        md.reset()
        content_html = md.convert(raw)

        # Remove the first H1 since it's in the template breadcrumb context
        # Actually keep it — it's the page title

        html = TEMPLATE.format(
            title=title,
            tradition_lower=short_title.lower(),
            slug=slug,
            short_title=short_title,
            content=content_html,
        )

        html_path = FRAMEWORKS_DIR / slug / "index.html"
        html_path.write_text(html)
        print(f"  {slug}/index.html — {len(html)} chars")


if __name__ == "__main__":
    build()
