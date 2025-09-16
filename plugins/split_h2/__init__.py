from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import os
import re


class SplitH2Plugin(BasePlugin):
    config_scheme = (
        ('source', config_options.Type(str, default='docs/index.md')),
        ('output_dir', config_options.Type(str, default='docs/sections')),
    )

    def on_pre_build(self, config):
        src = self.config['source']
        out_dir = self.config['output_dir']
        if not os.path.exists(src):
            return
        os.makedirs(out_dir, exist_ok=True)

        with open(src, 'r', encoding='utf-8') as f:
            text = f.read()

        # Split by H2 headings (## )
        parts = re.split(r'\n(?=##\s+)', text)
        # If the file starts with H1, keep it only on index; skip if no H2
        sections = []
        for p in parts:
            if p.startswith('## '):
                # capture title
                m = re.match(r'##\s+(.+)', p)
                title = m.group(1).strip() if m else 'section'
                body = p
                # promote to H1 for standalone page
                body = re.sub(r'^##\s+', '# ', body, count=1)
                slug = re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', title.lower()))
                sections.append((title, slug, body))

        # Write each section as its own page
        for idx, (_, slug, body) in enumerate(sections, start=1):
            fn = os.path.join(out_dir, f"{idx:02d}-{slug}.md")
            with open(fn, 'w', encoding='utf-8') as w:
                w.write(body.strip() + "\n")

        # Let MkDocs pick up files from filesystem. If user has an explicit nav,
        # we do not modify it.
        return config

