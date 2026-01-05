all: copy build

# Create docs/ directory and copy necessary files
# it would be nice to call it output/ or similar but github pages
# requires a docs/ directory
copy:
	mkdir -p docs
	cp -r imgs docs/
	cp index.html docs/
	cp style.css docs/
	cp CNAME docs/

# Create static website
build:
	uv run build/projects.py
	uv run build/project_grid.py

.PHONY: all copy build