PY=python3

.PHONY: sections serve build gh-deploy

sections:
	$(PY) scripts/generate_sections.py

serve: sections
	mkdocs serve -f mkdocs.nopdf.yml

build: sections
	mkdocs build -f mkdocs.nopdf.yml

gh-deploy: sections
	mkdocs gh-deploy -f mkdocs.nopdf.yml -c

