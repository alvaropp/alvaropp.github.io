from pathlib import Path
import re
from jinja2 import Environment, FileSystemLoader, select_autoescape


def extract_data_from_md(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        title_match = re.search(r"title: (.+)", content)
        img_match = re.search(r"img: (.+)", content)
        title = title_match[1] if title_match else "No Title"
        img_url = img_match[1] if img_match else ""
        return title, img_url


def generate_html_for_grid(directory):
    html = '<div class="projects-grid">'
    for filename in Path(directory).glob("*.markdown"):
        title, img_url = extract_data_from_md(filename)
        project_html = f'<div class="project-item"><img src="{img_url}" alt="{title}"><p>{title}</p></div>'
        html += project_html
    html += "</div>"
    return html


output_folder = Path("output")
output_folder.mkdir(parents=True, exist_ok=True)

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape(["html", "xml"]),
)

template = env.get_template("projects.html")

project_grid = generate_html_for_grid("content/projects/")
html = template.render(project_grid=project_grid)

with open(output_folder / "projects.html", "w") as file:
    file.write(html)
