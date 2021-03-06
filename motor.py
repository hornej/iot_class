#!/usr/bin/python

import wiringpi as wp
import time

wp.wiringPiSetupGpio()

#configure input and output pins
PWMPin = 18
Standby = 4
AIN1 = 17
AIN2 = 24


wp.pinMode(PWMPin, 2)
wp.pinMode(Standby, 1)
wp.pinMode(AIN1, 1)
wp.pinMode(AIN2, 1)

try:
   ##raw_input("Press any key and enter to exit\n")
   
   while True:
      wp.digitalWrite(Standby, 1)
      wp.digitalWrite(AIN1, 0)
      wp.digitalWrite(AIN2, 1)
      for x in range(0, 800):
         wp.pwmWrite(PWMPin, x) #pwmWrite() takes input values in the range 0 - 1023
         time.sleep(.01)
         
      wp.digitalWrite(Standby, 0)
      wp.digitalWrite(AIN1, 0)
      wp.digitalWrite(AIN2, 0)
      time.sleep(5)

      wp.digitalWrite(Standby, 1)
      wp.digitalWrite(AIN1, 1)
      wp.digitalWrite(AIN2, 0)
      for x in range(0, 800):
         wp.pwmWrite(PWMPin, x) #pwmWrite() takes input values in the range 0 - 1023
         time.sleep(.01)
         
      wp.digitalWrite(Standby, 0)
      wp.digitalWrite(AIN1, 0)
      wp.digitalWrite(AIN2, 0)
      time.sleep(5)
      
      
   
except:
   pass
finally:
   #clean up
   print("\nexiting")
   wp.pinMode(PWMPin, 0)
   exit(0)
