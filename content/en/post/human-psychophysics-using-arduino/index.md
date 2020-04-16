---
title: Human psychophysics using Arduino
authors: ['André Maia Chagas']
layout: post

---
This is an example of what can be done with an arduino and python code running on a computer.

In this specific case, a version of [Posner&#8217;s test](http://en.wikipedia.org/wiki/Posner_cueing_task) using exogenous cues.

Due to time limitations, I refer the installation of the Arduino, Python and its necessary libraries (in this case I think only pySerial is needed as extra) to other sources ([arduino](http://arduino.cc/en/Guide/HomePage), [python](http://www.python.org/getit/), and [pySerial](http://pyserial.sourceforge.net/pyserial.html)).

Hardware:

Arduino UNO (other versions can be used, depending on the demand)

5 LEDs

5 220 Ohms resistors

1 push button

1 10 kOhms resistor

the schematics on how to connect all together can be found [here.](http://openeuroscience.wordpress.com/tutorials/human-psychophysics-using-arduino/schematics-posner-test/ "schematics Posner test")

Software:

[One script](http://openeuroscience.wordpress.com/tutorials/human-psychophysics-using-arduino/arduino-script-posner-test/ "Arduino script posner test") running on the arduino IDE

One [python script](http://openeuroscience.wordpress.com/tutorials/human-psychophysics-using-arduino/python-posner-test/ "Python record script posner test") (written in version 2.7) running on the PC/raspberry Pi

Overall explanation:

The script running on the arduino IDE, which controls LEDs, used as fixation point, exogenous cues and targets and monitors a button press. The script controls the task and sends via serial port some data: trial number, if the trial was aborted or not (due to improper button press), LED cue side, delay between onset of fixation point and onset of cue, LED target side, delay between cue LED offset and target LED onset and reaction time (delay between target LED onset and button press).

A python script running on the computer which creates a folder and a file with the subjects name and opens the serial port to record the data being sent from the arduino. The data read is stored as readable strings in a text file.

Afterwards, the files can be read in your favorite programming language/data analyses software for further analyses (I intend to put some code for data analyses of this task as well).
