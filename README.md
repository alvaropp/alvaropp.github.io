# alvarop.me

Personal website built with Python and deployed via GitHub Pages.

## Structure

- `index.html` - Main page source
- `content/projects/*.markdown` - Project source files with YAML frontmatter (taken from my old site)
- `templates/` - Jinja2 templates for HTML generation
- `build/*.py` - Python scripts to convert markdown to HTML
- `docs/` - Generated site (GitHub Pages root)

## Development

```bash
# Build site
make
```

## Adding Projects

Create a new `.markdown` file in `content/projects/`:

```markdown
---
date: YYYY-MM-DD
title: Project Title
description: Short description
brief: Longer description
img: URL to thumbnail
type: hardware or software
---

Project content here
```

Run `make` to generate HTML.

## Dependencies

Uses [uv](https://docs.astral.sh/uv/) for Python dependency management. Dependencies are declared inline in each Python script.
