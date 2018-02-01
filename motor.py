#!/usr/bin/python

import wiringpi as wp

wp.wiringPiSetupGpio()

#configure input and output pins
PWMPin = 18
Standy = 4
AIN1 = 17
AIN2 = 24


wp.pinMode(PWMPin, 1)
wp.pinMode(Standy, 1)
wp.pinMode(AIN1, 1)
wp.pinMode(AIN2, 1)

try:
   wp.pwmWrite(PWMPin, 250) #pwmWrite() takes input values in the range 0 - 1023
   raw_input("Press any key and enter to exit\n")
   
except:
   pass
finally:
   #clean up
   print("\nexiting")
   wp.pinMode(PWMPin, 0)
   wp.pinMode(DirectionPin, 0)
   exit(0)
