#!/usr/bin/python
from serial import *
import time
import struct

arduino = Serial(port="/dev/ttyACM0", baudrate=9600, timeout=10, writeTimeout=10)
time.sleep(2)
nbRing = 12

for address in range(nbRing):
        if arduino.isOpen():
                arduino.flush() 
                package = [address, 255, 255, 255]
                for i in package:
                        arduino.write(struct.pack('B', i))
        else:
                print("arduino is closed !")
        time.sleep(0.2)
for address in range(nbRing):
        if arduino.isOpen():
                arduino.flush() 
                package = [address, 0, 0, 0]
                for i in package:
                        arduino.write(struct.pack('B', i))
        else:
                print("arduino is closed !")
        time.sleep(0.2)


            

