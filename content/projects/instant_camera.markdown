---
layout: page
date: 2017-02-03
title: Instant camera
description: with a thermal printer!
brief: An instant camera, Polaroid style. It consists of three separate parts. Namely, a broken action camera which only powers on when connected to power through USB, a Raspberry Pi and a thermal printer like the ones commonly used for purchase receipts. The three things are relatively portable and can be easily powered off a powerbank. Stills are taken with the push of a button which is fixed to the Raspberry Pi's case, and can be instantly printed with a second press when the printer is connected.
img: https://user-images.githubusercontent.com/4785303/36443949-1e8acaba-1672-11e8-8431-a8dba6e2ba0d.jpg
big_img: https://user-images.githubusercontent.com/4785303/36443946-1e2a4aa0-1672-11e8-83c6-b30d27f6784d.jpg
skills: Raspberry Pi, Python, making.
type: hardware
---

The thermal printer itself is a <a href="http://www.pipsta.co.uk/" target="_blank">Pipsta</a>, which comes with support for the Raspberry Pi, and plenty of <a href="https://bitbucket.org/ablesystems/pipsta/overview" target="_blank">code examples</a>. On the camera side, it is a nearly-bricked <a href="https://sjcam.com/product/sj4000/" target="_blank">SJ4000</a>, which can be interfaced from Raspbian as any other webcam. I soldered a push-button and a status LED to two of the RPi's GPIO pins, and fixed these to the RPi's case. Using `cron` I run a Python script which monitors the button presses and, depending on whether the printer is connected to the RPi, takes a still or prints the most recently stored picture. This way, several stills can be taken without the printer, and then printed all together.

<div class="img_row">
  <img class="col two" src="https://user-images.githubusercontent.com/4785303/36443948-1e703cfe-1672-11e8-89f1-7975052f2f34.jpg"/>
  <img class="col one" src="https://user-images.githubusercontent.com/4785303/36443947-1e501a46-1672-11e8-8887-a87b4fded1a5.jpg"/>
</div>
