from pathlib import Path
import re
from markdown2 import markdown


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


# Save the generated HTML to a file or print it
code = generate_html_for_grid("../projects")
with open("../projects_grid.html", "w") as file:
    file.write(code)
