all: setup copy build

# Setup virtual environment and install requirements
setup:
	@if [ ! -d ".venv" ]; then \
		python3 -m venv .venv && \
		source .venv/bin/activate && \
		pip install -r requirements.txt; \
	fi

# Create output directory and copy necessary files
copy:
	mkdir -p output
	cp -r imgs output/
	cp index.html output/

# Create static website
build:
	.venv/bin/python build/projects.py
	.venv/bin/python build/project_grid.py

.PHONY: all setup copy build