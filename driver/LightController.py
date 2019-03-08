#!/usr/bin/python
from serial import *
import time
import struct


class LightController:
    def __init__(self):
        self.arduino = Serial(port="/dev/ttyACM0", baudrate=9600, timeout=10, writeTimeout=10)
        time.sleep(2)
        
    def set(self, address, r, g, b):
            if self.arduino.isOpen():
                self.arduino.flush() 
                package = [address, int(r), int(g), int(b)]
                print('writing ', package)
                for i in package:
                    self.arduino.write(struct.pack('B', i))
            else:
                print("arduino is closed !")

