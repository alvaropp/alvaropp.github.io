---
layout: page
date: 2020-05-25
title: Interactive maps
description: online table top games
brief: Create zoomable maps of your choice, populate them with characters and share them with friends. Everybody can move characters around and the changes are updated in real-time. Useful for table-top or RPG games in these difficult lockdown times.
img: https://user-images.githubusercontent.com/4785303/104022834-bb1cef00-51b8-11eb-8d16-1c414a02e54d.jpg
no_img: yes
skills: Firebase, js, Leaflet, Python, Flask
how-to: code available on <a href="https://github.com/alvaropp/interactive-fantasy-map" target="_blank">GitHub</a>
---

I played a table-top RPG game during the lockdown and thought it would be cool to be able to play with friends online. Of course, there are lots of RPG websites full of cool features to manage online games, but I found that these need quite a lot of setup and what we wanted was just to have a lightweight shared interactive map that was quick to setup.

This was an interesting exercise and I built the prototype using Google's <a href="https://firebase.google.com/" target="_blank">Firebase</a> as a real-time database and <a href="https://leafletjs.com/" target="_blank">Leaflet.js</a> to handle the interactive maps. By using a tile approach (similar to Google Maps, etc.) I was able to turn high-definition image maps into responsive and lightweight zoomable maps, like the examples below. Each character in the map can be dragged, and the changes are immediately visible in every browser that has the map open (these examples are static though).

<div class="video-container">
  <iframe src="https://alvarop.me/fantasy-map-example/space.html" frameborder="0" allowfullscreen></iframe>
</div>

<br>

<div class="video-container">
  <iframe src="https://alvarop.me/fantasy-map-example/index.html" frameborder="0" allowfullscreen></iframe>
</div>

<br>

I also created a simple form that would allow you to select your map image and the desired number of characters with their icons, and it would automatically create tiles based on the map image at different zoom levels, and host everything online, giving you an url that you can share with the other players.

Although this project is not online anymore, full code is available in Github as linked above.

<hr>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){:target="_ blank"}

[interactive-fantasy-map](https://github.com/alvaropp/interactive-fantasy-map){:target="_ blank"} is available under an [MIT](https://opensource.org/licenses/MIT){:target="_ blank"} license.
