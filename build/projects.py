# %%
import re

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from slugify import slugify


# %% Load all project files
project_folder = Path("content/projects")
project_files = list(project_folder.glob("*.markdown"))


# %% Create pages for each project
env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"]),
)


def extract_data_from_markdown(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    title_match = re.search(r"title: (.+)", content)
    img_match = re.search(r"img: (.+)", content)
    description_match = re.search(r"description: (.+)", content)
    brief_match = re.search(r"brief: (.+)", content)

    title = title_match[1] if title_match else "No Title"
    img_url = img_match[1] if img_match else ""
    description = description_match[1] if description_match else ""
    brief = brief_match[1] if brief_match else ""

    return {
        "title": title,
        "img_url": img_url,
        "description": description,
        "brief": brief,
    }


output_folder = Path("output/projects/")
output_folder.mkdir(parents=True, exist_ok=True)

for file in project_files:
    project = extract_data_from_markdown(file)

    template = env.get_template("project.html")
    html = template.render(project=project)
    with open(output_folder / f"{slugify(project['title'])}.html", "w") as file:
        file.write(html)


# %%
