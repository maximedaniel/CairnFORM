#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import os

switches = [21, 19, 20, 16, 13,  6, 12, 5, 25, 24, 23, 22]
addresses = [0,  2,  1,  3,  4,  6,  5, 7,  8, 10,  9, 11]

GPIO.setmode(GPIO.BCM)

for switch in switches:
    GPIO.setup(switch, GPIO.IN)
 
while True:
    os.system('clear')
    msg = ''
    for address in addresses:
        msg+= str(GPIO.input(switches[address])) + ' '
    print(msg)
    time.sleep(0.1)
