---
title: Blinkenschild

authors: ['André Maia Chagas']
layout: post
categories: ['Visual','Hardware']
tags: ['Visual','Hardware']
---


[Blinkenschild](https://hackaday.io/project/363-blinkenschild) is a portable sign consisting of 960 RGB LEDs. The images/movies to be displayed are stored in a SD card in a Teensy3 board and controlled via bluetooth. Resolution is not as high as LCD monitors but the refresh rate is much higher:

    This is done in realtime and pixelvalues are recalculated before display.

    This is still too fast so i had to add 30 ms delay between the frames or we would not perceive it as a fluid animation but rather just blinking bright light.


<iframe width="790" height="593" src="https://www.youtube.com/embed/VX14pmky07Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
