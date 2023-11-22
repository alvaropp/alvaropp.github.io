---
layout: page
date: 2017-12-01
title: Interactive Fluid Simulation
description: on Twitter!
skills: Python, Twitter API, virtual machines.
brief: This project builds upon the great <a href="https://github.com/ngcm/interactive-fluid-demo" target="_blank">fluid flow simulation</a> developed by <a href="http://cmg.soton.ac.uk/people/gmd1n15/" target="_blank">Gary Downing</a> as an <a href="http://ngcm.soton.ac.uk" target="_blank">NGCM</a> outreach show. This fluid simulation software takes real input from a web-cam and runs a fluid simulation on top of the real-time images, where fluid comes from the left-hand side of the screen and is affected by the present objects on its way. This has been proven very successful in previous outreach events from the University of Southampton. For this year's University of Southampton Science and Engineering Festival 2018, and any other outreach events, I made a simple extension which integrates with Twitter. Basically, any participant can send a custom image or drawing to our Twitter account <a href="https://twitter.com/FluidFlowTest" target="_blank">@FluidFlowTest</a>, and will instantly receive a GIF with the fluid simulation on top of their image in return.
img: https://user-images.githubusercontent.com/4785303/35472499-352d9ee0-0368-11e8-83ca-f20c6c2cc1ea.png
big_img: https://user-images.githubusercontent.com/4785303/35059288-8757857c-fbb2-11e7-9b96-b0d32f02744f.gif
how-to: code available on <a href="https://github.com/alvaropp/interactive-fluid-twitter" target="_blank">GitHub</a>.
---

<div class="img_single">
    <img class="col three" src="https://user-images.githubusercontent.com/4785303/35060001-eb033510-fbb4-11e7-8d14-384632987b6b.gif"/>
</div>

<br>

This software uses [Tweepy](https://github.com/tweepy/tweepy){:target="_ blank"} to implement a Twitter stream listener which captures tweets that mention our Twitter account. When one such tweet is received, the software automatically tries to retrieve an attached image, which is then used to run the fluid simulation. Several stills of this simulation are captured and built into a GIF, which is then tweeted back at the user.

<hr>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT){:target="_ blank"}

[Interactive-fluid-demo](https://github.com/ngcm/interactive-fluid-demo){:target="_ blank"} by Gary Downing is available under an [MIT](https://opensource.org/licenses/MIT){:target="_ blank"} license. The extension for Twitter, [Interactive-fluid-twitter](https://github.com/alvaropp/interactive-fluid-twitter){:target="_ blank"} by Alvaro Perez-Diaz is available under an [MIT](https://opensource.org/licenses/MIT){:target="_ blank"} license.
