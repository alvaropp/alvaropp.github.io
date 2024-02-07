---
layout: page
date: 2020-11-01
title: Real-time GPS tracking
description: using your phone
brief: Easily track location and progress along a given route with the idea of being able to track people in long runs. I have been using this successfully in the last few months so that I can be tracked (and track my parter) in order to meet along the way or to be picked up at the end. I've been using the Overland app to transmit location data from my phone and hosting the server in PythonAnywhere.
img: https://user-images.githubusercontent.com/4785303/104010194-0c6eb380-51a4-11eb-9564-5ac11df666ef.jpg
skills: js, Leaflet, Python, Flask.
big_img: https://user-images.githubusercontent.com/4785303/104010342-4344c980-51a4-11eb-920c-fdf64beb573a.jpg
type: software
---

<br> The idea is to be able to track a runner or cyclist along a route in real-time in order to be able to meet along the way or to pick them up at the end. While there are some companies that offer this kind of service, I didn't find anything that worked well (tried a couple of apps) and thought that this should be easy to build and maintain.

I have some experience using <a href="https://leafletjs.com/" target="_blank">Leaflet.js</a> and there are a number of cool plugins that deal with gpx data, so this was the obvious candidate. In terms of the web server, <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">Flask</a> is normally my framework of choice. An easy way to serve the map is to use <a href="https://www.pythonanywhere.com/" target="_blank">PythonAnywhere</a> or <a href="https://www.heroku.com/" target="_blank">Heroku</a>.

On the phone side, I found the <a href="https://overland.p3k.app/" target="_blank">Overland app</a>, which is available for both Android and iOS, and does exactly what I need for this project. It lets you configure an end-point of your choice and it just sends GPS data. You can select the desired frequency and it has a lot of nice features like caching the data locally if no connection is available, etc. I've found battery consumption is very reasonable as well.

With respect to the route, I normally upload a gpx file with my intended route and it is displayed in the map alongside with my progress. This is quite useful to infer how far in the runner is into the run, etc. Also, there are some statistics at the bottom, including the total distance travelled so far and the total ascent. These are computed purely relying on phone GPS data, which can be inaccurate (specially altitude, in some phones!), so I decided to query a free  <a href="https://elevation.racemap.com" target="_blank">DEM</a> service online to correct elevation data before it's stored in the current trip.

All in all, this project turned out to be quite useful and works well. It's easy to maintain and can be easily deployed online for free, as mentioned above.
