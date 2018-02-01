#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

#configure input and output pins
PWMPin = 12
DirectionPin = 11
PushBtn1 = 13
PushBtn2 = 15
PushBtn3 = 16

wp.pinMode(PWMPin, 2)
wp.pinMode(DirectionPin, 1)
wp.pinMode(PushBtn1, 0)
wp.pinMode(PushBtn2, 0)
wp.pinMode(PushBtn3, 0)

try:
   wp.pwmWrite(PWMPin, 250) #pwmWrite() takes input values in the range 0 - 1023
   raw_input("Press any key and enter to exit\n")
except:
   pass
finally:
   #clean up
   print "\nexiting"
   wp.pinMode(PWMPin, 0)
   wp.pinMode(DirectionPin, 0)
   exit(0)
