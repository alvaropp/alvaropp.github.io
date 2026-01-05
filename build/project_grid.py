# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "jinja2==3.1.6",
#     "markdown2==2.4.10",
#     "python-slugify==8.0.1",
# ]
# ///

import re

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from slugify import slugify

PROJECT_TYPES = ["hardware", "software"]


def extract_data_from_md(file_path):
    with open(file_path, "r") as file:
        content = file.read()

        date_match = re.search(r"date: (.+)", content)
        title_match = re.search(r"title: (.+)", content)
        img_match = re.search(r"img: (.+)", content)
        project_type_match = re.search(r"type: (.+)", content)

        date = date_match[1] if date_match else ""
        title = title_match[1] if title_match else ""
        img_url = img_match[1] if img_match else ""
        project_type = project_type_match[1] if project_type_match else ""

        return date, title, img_url, project_type


def generate_html_for_grid(directory):
    projects = {project_type: [] for project_type in PROJECT_TYPES}

    for filename in Path(directory).glob("*.markdown"):
        date, title, img_url, project_type = extract_data_from_md(filename)
        projects[project_type].append(
            {"title": title, "img_url": img_url, "date": date}
        )
    for project_type in PROJECT_TYPES:
        projects[project_type] = sorted(
            projects[project_type], key=lambda x: x["date"], reverse=True
        )

    html = ""
    for project_type, projects in projects.items():
        html += f'<div class="nonumberh2">{project_type.capitalize()}</div>'
        html += '<div class="projects-grid">'
        for project in projects:
            project_html = (
                f'<div class="project-item">'
                f'<a href="projects/{slugify(project["title"])}.html">'
                f'<img src="{project["img_url"]}" alt="{project["title"]}"></a>'
                f"<p>{project['title']}</p></div>"
            )
            html += project_html
        html += "</div>"
    return html


output_folder = Path("docs")
output_folder.mkdir(parents=True, exist_ok=True)

env = Environment(loader=FileSystemLoader("templates"), autoescape=True)

template = env.get_template("projects.html")

project_grid = generate_html_for_grid("content/projects/")
html = template.render(project_grid=project_grid)

with open(output_folder / "projects.html", "w") as file:
    file.write(html)
