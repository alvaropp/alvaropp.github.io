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
	@current_branch=$$(git rev-parse --abbrev-ref HEAD); \
	echo $$current_branch; \
	if [ "$$current_branch" != "main" ]; then \
		echo "You are not on the 'main' branch. Current branch is '$$current_branch'."; \
		exit 1; \
	fi; \
	if ! git diff-index --quiet HEAD --; then \
		echo "Uncommitted changes detected. Commit your changes before deploying."; \
		exit 1; \
	fi

	git checkout -b page || git checkout page
	git pull origin page
	rm -rf .venv/
	git rm -rf content/
	git rm -rf build/
	git rm -rf imgs/
	git rm -rf templates/
	git rm .gitignore
	git rm index.html
	git rm Makefile
	git rm requirements.txt

	cp -r output/* .
	rm -rf output/
	find . -name '.DS_Store' -type f -delete 
	git add .
	git commit -m "Deploy to page branch"
	git push --set-upstream origin page
	git checkout main

.PHONY: all setup copy build deploy