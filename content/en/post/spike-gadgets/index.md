---
title: Spike Gadgets
authors: ['André Maia Chagas']
layout: post
categories: ['Software']
tags: ['Software']
date: 2020-05-06
---
A brief description of their current software (09.Sep.2016) is provided by one of their founders, Mattias Karlsson:

**[State Script:](http://www.spikegadgets.com/software/statescript.html)**

Do you need to control lasers for optogenetics, stimulators, or other TTL-based devices with precise, temporally defined patterns? Do you need to monitor beam breaks, lever presses, or other digital events in real time to define behavioral tasks?  You could program an Arduino, but that’s a lot of work. Or, you can use StateScript, which allows users with minimal programming experience define complex input/output relationships for the most demanding hardware control experiments.


<div>

This open-source project now runs on two available hardware platforms, the MBED LPC1768 micro controller board ($50) and the SpikeGadgets electrophysiology and behavioral control system.  More hardware support in is the works. A software interface, which is part of the Trodes open-source eletrophysiology suite (<a href="http://www.spikegadgets.com/software/trodes.html" target="_blank">http://www.spikegadgets.com/software/trodes.html</a>), allows you to upload scripts and dynamically interact with variables and ports states.

<br>

Anyone is welome to contribute. Here is the [bitbucket repo.](https://bitbucket.org/mkarlsso/statescript)
  
</div>


  <div align="center">

![](https://i2.wp.com/www.spikegadgets.com/images/statescript_screenshot_2.png?resize=800%2C571)


  
  </div>



<div>

**[Trodes:](http://www.spikegadgets.com/software/trodes.html)**

Trodes is a software suite with a focus on data acquisition for extracellular neural recordings.  It has a growing user base and welcomes contributors with open arms! It is built using the ever-popular and powerful Qt C++ framework. While it is specialized to be used with SpikeGadgets’ ephys hardware, it also has built-in support for the Intan demo system and Open-Ephys hardware.



It has some pretty impressive capabilities, including visualization of thousands of channels, spike viewing, online spike sorting, and low latency feedback control.  It has video processing, allowing position tracking that is synchronized to the recording, and integrates powerful environment control (lasers for optogenetics, levers, lights, pumps, etc.) with StateScript.

</div>

<div align="center">

![Trodes interface](https://i1.wp.com/www.spikegadgets.com/images/trodesscreenshot.png?resize=800%2C444) 

<p align="center"> Trodes interface </p>

![Trodes interface](https://i1.wp.com/www.spikegadgets.com/images/trodes_screenshot_cameramod.png?resize=800%2C554) 

<p align="center"> Trodes </p>
  
</div>

