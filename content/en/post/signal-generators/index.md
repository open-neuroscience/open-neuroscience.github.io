---
title: Signal Generators
authors: ['André Maia Chagas']

layout: post
categories: ['Hardware']
tags: ['Hardware']
---


Every lab needs a signal generator once in a while. They are useful to see if your acquisition program is working properly, to test why a certain piece of equipment is not working properly or to generate cues and targets at behavioural paradigms. Listed below are different generators, built using arduinos and other microcontrollers. They have different degrees of complexity and capabilities, so it would be wise to briefly look through them and see what fits you best!


***

[The arduino waveform generator](http://www.instructables.com/id/Arduino-Waveform-Generator/) is a pretty straight forward project that is able to generate four different waveforms from 1Hz to 50kHz. Gain, frequency, modulation and waveform type are controlled by nobs.

<iframe width="800" height="422" src="https://www.youtube.com/embed/gz_gVKWFN8E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

***

[Atmel Xmega USB/Serial Arbitrary Waveform Generator](http://www.instructables.com/id/Atmel-Xmega-USBSerial-Arbitrary-Waveform-Generato/?ALLSTEPS) runs using a boston android XMEGA evaluation board and is able to deliver square, sine, triangular and arbitrary waveforms in between 5Hz and 20kHz. This one is not a stand alone system, which means that to set a new waveform type, one would have to have the board connect to a computer at all times.

<img src="https://i1.wp.com/www.instructables.com/files/deriv/FWF/PWX4/G79D44SM/FWFPWX4G79D44SM.LARGE.jpg?w=800" alt="arbitrary waveform generator" data-recalc-dims="1" />

---

[Simple waveform generator](http://arduino.cc/en/Tutorial/DueSimpleWaveformGenerator) seems to be the most straight forward of all projects, requiring only a potentiometer, a couple of resistors and push buttons. The trade off is that with the present sketch, waveforms of only up to 170Hz can be generated. It generates sawtooth, square, triangular and sine waveforms.

<img src="https://i0.wp.com/arduino.cc/en/uploads/Tutorial/DueSimpleWaveform_fritzing.png?w=800" alt="arduino due waveform generator" data-recalc-dims="1" />
