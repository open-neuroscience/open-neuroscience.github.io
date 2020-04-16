---
title: Arduino script posner test
date: 2013-06-24T23:22:21+00:00
authors: ['André Maia Chagas']
layout: post

---
This script is to be run on the Arduino IDE

Everything below this line should be copied and pasted into the IDE space and then sent to the arduino board:

// Program to run a Posner&#8217;s test task using exogenous cues

//created by Andre Maia Chagas 25/06/2013

//shared under: Creative Commons Attribution-ShareAlike 3.0 Unported License

<pre>//outputs
 int leftTarBit=3, leftCueBit=4, midLedBit=5, rightCueBit=6, rightTarBit=7;
 //inputs
 int buttonBit=9;
 //variable to store temporary data
 long dummie=0;
 //variable with the number of trials
 int trials=100,trialNum=0;
 //simple counter
 int count=0;
 //variable to store the reaction time in each trial
 unsigned long reactionTime=0;
 //variables to store the passage of time in microseconds
 unsigned long time1=0;
 unsigned long time2=0;
 unsigned long interval=200000;
 //array to store the cue side - somehow defining the size with another variable eg trials, doesn't work
 unsigned long cueSide[100];
 //cue duration in microseconds
 long cueDuration=50000;
 //array to store the intervals to be used for the targets
 unsigned long tarTimes[4]={200000,400000,600000,800000};
 //array to store the target side
 unsigned long tarSide[100];
 //array to store target delay
 unsigned long tarDelay[100];
 //declare variables to be used for button debounce
 long debDelay=50000;
 //variable to store the buttons last state (high or low)
 int buttonRead=0;
 byte aborted=0;
void setup(){
 //start the serial port with velocity of 115200 bits per second.
 Serial.begin(115200);
 //here a note: The arduino board resets everytime the PC serial port opens and connects.
 //therefore to use this setup one should connect the arduino to the PC via USB and then run
 //the python script.
//setup the random seed so that everytime the program is run,
 //the same intervals will be used for different subjects
 randomSeed(0);
 //setup the arrays with the cue and target sides.
 for (count=0;count&lt;trials;count++) {
 tarDelay[count]=tarTimes[random(0,4)];
 //get random number in between 1 and 10
 dummie=random(1,11);
 //50% of targets should be left and 50% right side
 if(dummie&gt;5){
 tarSide[count]=leftTarBit;
 // on 80% of the cases the cue indicates the same side of the target
 if (dummie&gt;8){cueSide[count]=rightCueBit;}
 // on 20% the opposite side
 else {cueSide[count]=leftCueBit;}
 }
 //same thing for the other side
 if(dummie&lt;=5){
 tarSide[count]=rightTarBit;
 if (dummie&gt;8){cueSide[count]=leftCueBit;}
 else{cueSide[count]=rightCueBit;}
 }
 }
//setup the inputs and outputs
 pinMode(leftTarBit,OUTPUT);
 pinMode(leftCueBit,OUTPUT);
 pinMode(midLedBit,OUTPUT);
 pinMode(rightCueBit,OUTPUT);
 pinMode(rightTarBit,OUTPUT);
 pinMode(buttonBit,INPUT);
 }
void loop() {
//ITI
 //set everything to zero
 reactionTime=0;
 aborted=0;
 //turn everything off(could also be done in a "for" loop) and wait for 2 seconds
 time2=micros();
 digitalWrite(leftTarBit,LOW);
 digitalWrite(leftCueBit,LOW);
 digitalWrite(midLedBit,LOW);
 digitalWrite(rightCueBit,LOW);
 digitalWrite(rightTarBit,LOW);
 time1=time2;
 //here 2000000 is two seconds in microseconds
 while (time2-time1&lt;(2000000)) {time2=micros();}
//NAW
 time1=time2 ;
 //turn on the central fixation LED
 digitalWrite(midLedBit,HIGH);
 //start counting time and after the minimum is reached, turn on the cue light
 //if there was a lever press start the trial again
 while(time2-time1&lt;interval){
 time2=micros();
 //read the button to see if it was pressed on the wrong moment
 //the function for this is called "debounce" and is defined in the end of the script
 aborted=debounce(buttonBit,debDelay);
 if (aborted==1){aborted=0; goto fim;}}
//turn the cue led on
 digitalWrite(cueSide[trialNum],HIGH);
 time1=time2;
 //count the time the cue light should be on, and turn it off afterwards
 while(time2-time1&lt;cueDuration){
 time2=micros();
 //read the button to see if it was pressed on the wrong moment
 //the function for this is called "debounce" and is defined in the end of the script
 aborted=debounce(buttonBit,debDelay);
 if (aborted==1){aborted=0; goto fim;}}
 //once the time is passed turn off the cue light
 digitalWrite(cueSide[trialNum],LOW);
 time1=time2;
//start counting the time between cue light off and target light on
 while(time2-time1&lt;tarDelay[trialNum]){
 time2=micros();
 //read the button to see if it was pressed on the wrong moment
 //the function for this is called "debounce" and is defined in the end of the script
 aborted=debounce(buttonBit,debDelay);
 if (aborted==1){aborted=0; goto fim;}
}
//target
 time1=micros();
 digitalWrite(tarSide[trialNum],HIGH);
 //keep reading the button bit and as soon as it is HIGH,
 //break the while loop and read the time.
 while(digitalRead(buttonBit)==LOW){}
 //after the button is pressed, measure time to see the reaction time
 time2=micros();
 //turn off the the target LED
 digitalWrite(tarSide[trialNum],LOW);
 //turn off the central LED
 digitalWrite(midLedBit,LOW);
 //get the reaction time
 reactionTime=(time2-time1);
 trialNum=trialNum+1;
 //Serial.println('trial: ');
 //Serial.println(trialNum);
 fim:
 //send all things to the serial port:
 //this follows the format *xxxx** where the stars are tags for the read out program.
 //The stars are used to know where one variable begins and ends.
 //the trial number
 Serial.print("*Trial**");
 Serial.print(trialNum-1);
 Serial.print("\n"); //this prints in a new line
 //wether a trial was aborted or not
 Serial.print("*Aborted**");
 Serial.print(aborted);
 Serial.print("\n");
 //which cue led lit up
 Serial.print("*CueSide**");
 Serial.print(cueSide[trialNum-1]);
 Serial.print("\n");
 //the duration of the cue (in this example 50ms in all trials)
 Serial.print("*CueDur**");
 Serial.print(cueDuration);
 Serial.print("\n");
 //the time delay in between the offset of the cue led and the onset of the target
 Serial.print("*TarDel**");
 Serial.print(tarDelay[trialNum-1]);
 Serial.print("\n");
 //which target led lit up
 Serial.print("*TarSide**");
 Serial.print(tarSide[trialNum-1]);
 Serial.print("\n");
 //the reaction time, aka time between target led onset and lever press
 Serial.print("*ReacTime**");
 Serial.print(reactionTime);
 Serial.print("\n");
 //the final tag once the subject complets 50 trials
 if(trialNum-1==50){Serial.print("*999**\n");}
 //wait for all the data to be transmitted
 Serial.flush();
}
byte debounce(int buttonBit,long debDelay){
 byte test=0;
 //measure time
 long timeOne=micros();
 long timeTwo=micros();
 //read the button state
 int buttonRead=digitalRead(buttonBit);
 //count time untill debounce delay is met
 while((timeTwo-timeOne)&lt;debDelay) {timeTwo=micros();}
 //if the button is "still pressed" after the delay set the flag to one
 if(digitalRead(buttonBit)==HIGH && buttonRead==HIGH){test=1;}
 //return the flag
 return test;
 }</pre>
