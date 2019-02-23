#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from serial import *
import time
import sys
import struct

class LightController:
    def __init__(self):
        self.arduino = Serial(port="/dev/ttyACM0", baudrate=9600, timeout=10, writeTimeout=10)
        time.sleep(2)
        
    def changeColor(self, address, r, g, b):
            #print(address, r,g,b)
            if self.arduino.isOpen():
                self.arduino.flush() 
                package = [address, r, g, b]
                for i in package :
                    self.arduino.write(struct.pack('B',i))
            else :
                print("arduino is closed !")

