#!/usr/bin/env python3
"""
Split docs/index.md into one file per H2 section under docs/sections/.
Re-runs are idempotent and overwrite generated files.
"""
import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'docs' / 'index.md'
OUT = ROOT / 'docs' / 'sections'

def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-]", "", text)
    return text

def main():
    if not SRC.exists():
        print(f"Missing {SRC}", file=sys.stderr)
        sys.exit(1)
    OUT.mkdir(parents=True, exist_ok=True)
    text = SRC.read_text(encoding='utf-8')
    parts = re.split(r"\n(?=##\s+)", text)
    sections = []
    for p in parts:
        if p.startswith('## '):
            m = re.match(r"##\s+(.+)", p)
            title = m.group(1).strip() if m else 'section'
            body = re.sub(r'^##\s+', '# ', p, count=1)
            slug = slugify(title)
            sections.append((title, slug, body))

    for i, (title, slug, body) in enumerate(sections, 1):
        fn = OUT / f"{i:02d}-{slug}.md"
        fn.write_text(body.strip() + "\n", encoding='utf-8')
        print(f"Wrote {fn}")

if __name__ == '__main__':
    main()

