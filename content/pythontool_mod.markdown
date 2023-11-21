---
layout: page
date: 2016-09-01
title: PythonTool Mod
description: Python inside Minecraft!
skills: Java, Python, Jekyll, continuous integration
brief: This project consisted in the creation of PythonTool, a Minecraft mod which allows visual and interactive in-game execution of Python scripts which alter the Minecraft world in real time. It makes use of existing software libraries such as mcpi and RaspberryJam-Mod, and tries to improve and ease the programming experience. A non-traditional programming workflow using Jupyter Notebook is also proposed to complement the mod. This project was developed at the University of Southampton under the supervision of Prof Hans Fangohr.
img: https://user-images.githubusercontent.com/4785303/35472489-fe0c6022-0367-11e8-8f1a-5cc30e163ffa.jpg
video: mghcv0qJNv8
awards: The <i>Best new activity</i> award at the University of Southampton Science and Engineering Festival 2017 was given to all <a href="http://ngcm.soton.ac.uk/">NGCM</a> participants and activities, including the workshop with PythonTool-Mod.
how-to: <a href="https://ngcm.github.io/PythonTool-Mod/" target="_blank">official website</a>, code available on <a href="https://github.com/ngcm/PythonTool-Mod" target="_blank">GitHub</a>, how-to also hosted at <a href="https://www.instructables.com/id/Interactive-Python-Programming-for-Minecraft-Pytho/" target="_blank">Instructables</a>
---

<br>

The game Minecraft has been extremely successful in the last five years, with over 106 million copies sold, making it the second best-selling video game up to date. Its educational capabilities have been exploited in a variety of ways already across the world. In this project, we try to improve the ways that programming can be taught to young learners, by employing a modification (mod) of the game.

The possibility to employ Python to alter a Minecraft world in real time has been around for a number of years, provided by the game's creators. However, we believe that the usual text editor & console duo is daunting for young learners or people with limited programming experience. To overcome these difficulties, this mod attempts to *gamify* the programming experience, where players can write Python scripts which get ported inside the game as Python script objects, which can be held, dropped, and used with the click of a mouse. This resembles the way that any other weapon, tool or block is used within the game. Any number of different Python scripts can be put in the player's inventory, and they can be all used together in an interactive way.

Detailed installation and user guides can be found in the project's website. We recommend the book [Adventures in Minecraft](https://www.wiley.com/en-gb/Adventures+in+Minecraft-p-9781118946916){:target="_ blank"} by David Whale and Martin O'Hanlon to learn more about Python programming and Minecraft.

From a technical perspective, PythonTool is made with Java using the [Forge](https://files.minecraftforge.net/){:target="_ blank"} modding framework. It supports several recent versions of Minecraft and the mod's `.jar` files are built automatically using [CircleCI](https://www.circleci.com){:target="_ blank"} upon Github commits, and uploaded to the downloads section of the official website.

<hr>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){:target="_ blank"}
[![DOI](https://zenodo.org/badge/65482833.svg)](https://zenodo.org/badge/latestdoi/65482833){:target="_ blank"}

PythonTool-Mod by Alvaro Perez-Diaz and Hans Fangohr is available under an [MIT](https://opensource.org/licenses/MIT){:target="_ blank"} license. [DOI 10.5281/zenodo.801627](https://zenodo.org/record/801627){:target="_ blank"}.
