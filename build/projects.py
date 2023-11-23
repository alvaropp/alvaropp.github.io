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

    date_match = re.search(r"date: (.+)", content)
    title_match = re.search(r"title: (.+)", content)
    description_match = re.search(r"description: (.+)", content)
    brief_match = re.search(r"brief: (.+)", content)
    img_match = re.search(r"img: (.+)", content)
    big_img_match = re.search(r"big_img: (.+)", content)
    skills = re.search(r"skills: (.+)", content)
    how_to = re.search(r"how-to: (.+)", content)
    featured = re.search(r"featured: (.+)", content)
    awards = re.search(r"awards: (.+)", content)
    text = re.search(r"---\n\n(.+)", content, re.DOTALL)

    date = date_match[1] if date_match else ""
    title = title_match[1] if title_match else ""
    description = description_match[1] if description_match else ""
    brief = brief_match[1] if brief_match else ""
    img_url = img_match[1] if img_match else ""
    big_img_url = big_img_match[1] if big_img_match else ""
    skills = skills[1] if skills else ""
    how_to = how_to[1] if how_to else ""
    featured = featured[1] if featured else ""
    awards = awards[1] if awards else ""
    text = text[1] if text else ""

    return {
        "date": date,
        "title": title,
        "description": description,
        "brief": brief,
        "img_url": img_url,
        "big_img_url": big_img_url,
        "skills": skills,
        "how_to": how_to,
        "featured": featured,
        "awards": awards,
        "text": text,
    }


output_folder = Path("docs/projects/")
output_folder.mkdir(parents=True, exist_ok=True)

projects = [extract_data_from_markdown(file) for file in project_files]

for project in projects:
    template = env.get_template("project.html")
    html = template.render(project=project)
    with open(output_folder / f"{slugify(project['title'])}.html", "w") as file:
        file.write(html)


# %%
