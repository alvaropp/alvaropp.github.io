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
    no_img_match = re.search(r"no_img: (.+)", content)
    skills_match = re.search(r"skills: (.+)", content)
    how_to_match = re.search(r"how-to: (.+)", content)
    featured_match = re.search(r"featured: (.+)", content)
    awards_match = re.search(r"awards: (.+)", content)
    type_match = re.search(r"type: (.+)", content)
    text_match = re.search(r"---\n\n(.+)", content, re.DOTALL)

    date = date_match[1] if date_match else ""
    title = title_match[1] if title_match else ""
    description = description_match[1] if description_match else ""
    brief = brief_match[1] if brief_match else ""
    img_url = img_match[1] if img_match else ""
    big_img_url = big_img_match[1] if big_img_match else ""
    no_img = no_img_match[1] if no_img_match else ""
    skills = skills_match[1] if skills_match else ""
    how_to = how_to_match[1] if how_to_match else ""
    featured = featured_match[1] if featured_match else ""
    awards = awards_match[1] if awards_match else ""
    if type_match:
        _type = type_match[1]
    else:
        raise ValueError(f"`type` field not found in project: {file_path}")
    text = text_match[1] if text_match else ""

    return {
        "date": date,
        "title": title,
        "description": description,
        "brief": brief,
        "img_url": img_url,
        "big_img_url": big_img_url,
        "no_img": no_img,
        "skills": skills,
        "how_to": how_to,
        "featured": featured,
        "awards": awards,
        "text": text,
        "type": _type,
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
