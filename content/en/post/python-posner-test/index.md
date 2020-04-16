---
title: Python record script posner test
authors: ['André Maia Chagas']
layout: post

---
This is the script to be run in the computer, after the arduino has already been hooked up.

In linux the way to run this is to copy the text below in a new file with name ending in &#8220;.py&#8221; and running &#8220;path-to-file/filename.py&#8221; in a terminal:

&nbsp;

\# script to generate a file for storing data from the posner test run in arduino:

#written by Andre Maia Chagas 24.06.2013

#contact: openeuroscience(at)gmail.com

#distributed under Creative Commons Attribution-ShareAlike 3.0 Unported License.

#this script opens the serial port and reads data coming from an arduino UNO.

#it also creates a folder and a file to store the read data, in case they don&#8217;t

#exist.

#import necessary libraries:

import os #library that enables system operations

import datetime #library to get the current date

import serial #import library to read/write serial port

#serial port address

portName=&#8221;/dev/ttyACM1&#8243;

#check to see if there are any devices connected to the serial port:

if os.path.exists(portName):

#create the serial comm object (first par is the serial port and the second,

#the baud rate, in this case 115200 bits per second)

ser = serial.Serial(portName, 115200)

serFlag=1

else:

serFlag=0

print(&#8220;no serial devices connected!&#8221;)

print(&#8220;continuing without serial communication \n&#8221;)

#get the current date

tmpNow=str(datetime.datetime.now())

#path of the file to open

folderPath=&#8221;/home/andre/Documents/code/Posner\_test\_micros/test/&#8221;

#set the subject name

subjectName=&#8217;test1&#8242;

#set the name of the file

print tmpNow[0:10]+&#8221;_&#8221;+subjectName+&#8221;.txt&#8221;

fileName=tmpNow[0:10]+&#8221;_&#8221;+subjectName+&#8221;.txt&#8221;

print fileName

#check to see if the folder where you want to create

#the file exists. if it doesn&#8217;t exist, create it:

if not os.path.exists(folderPath):

os.makedirs(folderPath)

#create/open file in the specified folder in append mode:

newFile=open(folderPath+fileName,&#8221;a+&#8221;)

#write the date and the subject name at the beggining of the appended part

newFile.write(tmpNow[0:19]+&#8221;_&#8221;+subjectName+&#8221; \n&#8221;)

#if there is a serial device connected:

if serFlag==1:

ardCheck=0

#write one byte to the arduino

ser.write(&#8220;1&#8221;)

#wait for a specific signal from the arduino

while ardCheck<0:

ardCheck=ser.readline(1)

#now that one received the signal from the arduino,

#reset the &#8220;ardCheck&#8221; flag

ardCheck=0

print &#8220;device connected&#8221;

#now make python read data undefinetly untill a &#8220;break&#8221; command is called:

while True:

tmpVar=ser.readline()

newFile.write(tmpVar+&#8221;\n&#8221;)

#if the termination flag &#8220;\*999\**&#8221; is found, send the break command

if tmpVar==&#8221;\*999\**\n&#8221;:

print &#8220;test done!&#8221;

break

else:

print &#8220;no serial port connected!&#8221;

newFile.write(&#8220;no serial port connected!&#8221;)

#Close the file

newFile.close()
