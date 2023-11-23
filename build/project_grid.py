import re

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape
from slugify import slugify


def extract_data_from_md(file_path):
    with open(file_path, "r") as file:
        content = file.read()

        date_match = re.search(r"date: (.+)", content)
        title_match = re.search(r"title: (.+)", content)
        img_match = re.search(r"img: (.+)", content)

        date = date_match[1] if date_match else ""
        title = title_match[1] if title_match else ""
        img_url = img_match[1] if img_match else ""
        return date, title, img_url


def generate_html_for_grid(directory):
    projects = []
    for filename in Path(directory).glob("*.markdown"):
        date, title, img_url = extract_data_from_md(filename)
        projects.append({"title": title, "img_url": img_url, "date": date})

    projects = sorted(projects, key=lambda x: x["date"], reverse=True)

    html = '<div class="projects-grid">'
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
