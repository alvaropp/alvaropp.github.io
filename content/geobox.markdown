---
layout: page
date: 2019-05-09
title: GeoBox
description: reverse geocaching present
brief: Fun birthday present based on <a href="http://www.sundial.com/" target="_blank">Sundial's Quest Box</a>. It consists of a locked wooden box with no latch or keyhole displaying a small LCD screen and a switch. When the switch is flicked, the screen lights up and displays four different numbers. The user has to figure out that these are distances to four different points on Earth, which can then be triangulated. The box will automatically open once it has visited these four places and contains a present inside.
img: https://user-images.githubusercontent.com/4785303/57459450-30f5e800-726b-11e9-8455-c01724ee50ca.png
skills: Making, Electronics, Arduino
big_img: https://user-images.githubusercontent.com/4785303/57458453-479b3f80-7269-11e9-8038-207870ebd43e.jpg
---

Originally conceived a few years ago, these reverse geocaching boxes have acquired quite a lot of popularity and full builds and DIY kits are sold by the folks of <a href="http://www.sundial.com/" target="_blank">sundial.com</a>. However, when browsing online for inspiration to make my own, I realised that all the boxes I could find had a single secret destination. While this may be enough for some purposes, I wanted to build a longer quest that took my girlfriend to a few nice places and I ended up expanding the original box with three extra destinations, for a total of four.

When the box is turned on, it prompts the user to take it outside until the GPS unit hidden inside gets a satellite fix. It will then display four numbers in the LCD screen, corresponding to the distances in meters to the four secret destinations. Once the box is turned on within a small radious of a given destination, it will show a success message to the user. Finally, when all four destinations have been cleared, it will automatically open allowing access to a present located inside.

I used an Arduino Uno as a brain, an Adafruit GPS module and backlight screen, and a small solenoid latch. The whole thing is powered by an RC rechargeable battery and showed below.

<div class="img_single">
    <img class="col three" src="https://user-images.githubusercontent.com/4785303/57458460-4b2ec680-7269-11e9-8b2a-b0e740b4aaf0.jpg"/>
</div>

<hr>
Quest Box is a registered trademark by Sundial. They do, however, encourage people to build their own boxes and do sell DIY kits in their website.