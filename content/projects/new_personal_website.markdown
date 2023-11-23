---
layout: page
date: 2023-11-23
title: New personal website
description: custom built!
skills: Python, Jinja, CSS, HTML, Github
brief: As described in a related project post <a href="https://alvarop.me/projects/personal-website.html" target="_blank">Pelican</a>, I built myself a website using Jekyll and a modified open-source theme. However, I was not completely satisfied with the result and it wasn't easy to maintain. A few years ago I discovered <a href="http://casual-effects.com/markdeep/" target="_blank">Markdeep</a>, which makes creating simple websites using markdown extremely easy. This, combined with a bit of Python code and Jinja templating, allowed me to create a new website that is much easier to maintain and customize—you're looking at it now!
how-to: code available on <a href="https://github.com/alvaropp/alvaropp.github.io" target="_blank">GitHub</a>.
---

<hr>

Basically, I write pages using markdown, including the landing page and all these projects pages, and a small Python script generates the HTML pages using Jinja templating. This is pretty much what static website generators (Hugo, Pelican, etc.) do, but much more lightweight given that this website is extremely simple. In order to modify the website I just need to modify or add new markdown files, and run `make` to generate the output HTML files in a second.
