all: setup copy build

# Setup virtual environment and install requirements
setup:
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv && \
		source .venv/bin/activate && \
		pip install -r requirements.txt; \
	fi

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
	.venv/bin/python build/projects.py
	.venv/bin/python build/project_grid.py

.PHONY: all setup copy build