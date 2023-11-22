---
layout: page
date: 2017-02-27
title: Minecraft Controller
description: with Orientation sensor data
skills: sensors, real-time data streaming, UDP, Python.
brief: When organising <a href="../projects/outreach-events.html" target="_blank">outreach events</a> with <a href="../projects/pythontool-mod.html" target="_blank">PythonTool-Mod</a> for Minecraft, it became clear that many young people are not used to mouse & keyboard gaming. Some of the youngest players would even try to touch the computer monitor hoping it was a touch-screen. These experiences motivated this project, which explores how sensor data from a mobile phone could be employed to control player movement in video-games like Minecraft. Specifically, by using orientation data, one can move the Minecraft player around by tilting the phone in the desired direction.
img: https://user-images.githubusercontent.com/4785303/34828173-9a83f94c-f6d4-11e7-8f2d-e8510abc82db.jpg
big_img: https://user-images.githubusercontent.com/4785303/34828061-2c7ef4b0-f6d4-11e7-9838-bb70f406e98b.jpg
how-to: code available on <a href="https://github.com/alvaropp/MinecraftController" target="_blank">GitHub</a>.
---

<span style="font-size: 0.65em; float: right">Image created by me out of the following free resources:
<a href="https://www.flaticon.com/free-icon/coordinates_136810" target="_ blank">Coordinates</a>,
<a href="https://www.flaticon.com/free-icon/antenna-signal_1352" target="_blank">Radio signal</a>,
<a href="https://lockrikard.deviantart.com/art/Minecraft-huge-screenshot-201250327" target="_ blank">Minecraft screenshot</a>,
<a href="https://www.freepik.com/free-vector/screen-tv-mockup_835105.htm#term=screen&page=1&position=4" target="_ blank">Screen</a>,
<a href="https://www.freepik.com/free-photo/hand-holding-a-smartphone-with-blank-screen_987726.htm" target="_ blank">Phone</a>
</span>

<br>

This project has two key components: streaming the sensor data from the mobile device/sensor to the computer, and processing the incoming data to generate movement in the game.

(####) Streaming data

Most mobile phones have an orientation sensor or a gyroscope which can be easily accessed. This real-time data then needs to be transmitted to the computer with -ideally- low latency. This can be done with a lightweight UDP connection. Luckily for Android users, there is a free app, [Sensorstream IMU+GPS](https://play.google.com/store/apps/details?id=de.lorenz_fenster.sensorstreamgps&hl=en_GB){:target="_ blank"}, which does this out of the box. Just select the desired sensors to stream, and specify the receiving IP address. Most likely, similar apps exist for iOS and different platforms.

(####) Receiving and processing

The data stream can be received in the computer using a UDP socket listening for incoming data. This can easily be achieved in Python using the `socket` library. By default, if using the aforementioned Android app, the incoming port is `5555`. Once the data stream is being received, the mobile device orientation angles can be parsed and the appropriate movement keys *pressed* by software. In more detail, if the player tilts the phone forward, it is interpreted as walking forward. Analogously, when tilting the phone backward. When the phone is turned left or right, the player looks around in that direction. These rotations are controlled by mouse movements, and are more challenging to implement by software. While plenty of libraries allow to control mouse movements from Python code, they do not seem to work with Minecraft, at least in Mac OS and Ubuntu. There is some evidence online talking about this working in Windows systems. In order to bypass this difficulty, raw player movement and direction can be accessed by employing the [MCPI](https://github.com/martinohanlon/mcpi){:target="_ blank"} Python library released by [Mojang](https://minecraft.net/en-us/edition/pi/){:target="_ blank"} a few years ago. This not only solves the problem, but it also increases responsiveness.

Two scripts can be found in the repository. Firstly, the Minecraft specific script which employs MCPI and works only with Minecraft. Secondly, a general purpose script which uses [pyautogui](https://pyautogui.readthedocs.io/en/latest/){:target="_ blank"} to control the mouse. It does not work with Minecraft in Mac OS and Ubuntu, but it *may* work in Windows. Moreover, it does work fine in other 3D games I tried it with.

(####) Real-time demo

{% include video.html id="PQ1uTSzVTjs" %}

<hr>

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_ blank"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">MinecraftController</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Alvaro Perez-Diaz</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_ blank">Creative Commons Attribution 4.0 International License</a>.
