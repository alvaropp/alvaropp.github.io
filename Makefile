# Define default target
all: setup copy build deploy

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

# Run the python scripts
build:
	.venv/bin/python build/projects.py
	.venv/bin/python build/project_grid.py

# Deploy to 'page' branch and clean up
deploy:
	@if ! git diff-index --quiet HEAD --; then \
		echo "Uncommitted changes detected. Commit your changes before deploying."; \
		exit 1; \
	fi
	git checkout -b page || git checkout page
	# rm -rf * .[^.]*
	# cp -r ../output/* .
	# git add .
	# git commit -m "Deploy to page branch"
	# git push origin page
	# git checkout main
	# rm -rf output

.PHONY: all setup copy build deploy