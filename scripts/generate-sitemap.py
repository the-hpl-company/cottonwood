#!/usr/bin/env python3
"""Generate sitemap.xml for cottonwood.world from published index.html files."""

from pathlib import Path
from datetime import datetime, timezone
import xml.etree.ElementTree as ET


ROOT = Path(__file__).parent.parent
BASE_URL = "https://cottonwood.world"
OUTPUT = ROOT / "sitemap.xml"


def url_for(html_path: Path) -> str:
    rel = html_path.relative_to(ROOT)
    if rel.name != "index.html":
        return f"{BASE_URL}/{rel.as_posix()}"
    parent = rel.parent.as_posix()
    if parent == ".":
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{parent}/"


def main() -> None:
    urlset = ET.Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9",
    )

    pages = sorted(
        path
        for path in ROOT.rglob("index.html")
        if ".git" not in path.parts and "_working" not in path.parts
    )

    generated = datetime.now(timezone.utc).date().isoformat()

    for page in pages:
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = url_for(page)
        ET.SubElement(url, "lastmod").text = generated

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write(OUTPUT, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {OUTPUT} with {len(pages)} URLs")


if __name__ == "__main__":
    main()
