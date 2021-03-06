---
title: 'openEyeTrack - An open source high-speed eyetracker'
date: 2021-03-13
authors: ['admin']
layout: post
categories: ['Software','Hardware','Behaviour','Computers']
tags: ['Software','Hardware','Behaviour','Computers']
---
Vision is one of the primary senses, and tracking eye gaze can offer insight into the cues that affect decision-making behavior. Thus, to study decision-making and other cognitive processes, it is fundamentally necessary to track eye position accurately. However, commercial eye trackers are 1) often very expensive, and 2) incorporate proprietary software to detect the movement of the eye. Closed source solutions limit the researcher’s ability to be fully informed regarding the algorithms used to track the eye and to incorporate modifications tailored to their needs. Here, we present our software solution, openEyeTrack, a low-cost, high-speed, low-latency, open-source video-based eye tracker. Video-based eye trackers can perform nearly as well as classical scleral search coil methods and are suitable for most applications.

openEyeTrack is a video-based eye-tracker that takes advantage of OpenCV, a low-cost, high-speed infrared camera and GigE-V APIs for Linux provided by Teledyne DALSA, the graphical user interface toolkit QT5 and cvui, the OpenCV based GUI. All of the software components are freely available. The only costs are from the hardware components such as the camera (Genie Nano M640 NIR, Teledyne DALSA, ~$450, ~730 frames per second) and infrared light source, an articulated arm to position the camera (Manfrotto: $130), a computer with one or more gigabit network interface cards, and a power over ethernet switch to power and receive data from the camera.

By using the GigE-V Framework to capture the frames from the DALSA camera and the OpenCV simple blob detector, openEyeTrack can accurately estimate the position and area of the pupil. We include pupil size calculations because of its putative link to arousal levels and emotions of the subject.
## Project Author(s)
Chandramouli Chandrasekaran; Jorge Paolo Casas
## Project Links
https://github.com/chand-lab/openEyeTrack
***
This post was automatically generated by
Chandramouli Chandrasekaran
***
