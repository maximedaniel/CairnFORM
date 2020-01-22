#!/usr/bin/python
from serial import *
import time
import struct


class TestLight:
    def __init__(self):
        self.arduino = Serial(port="COM13", baudrate=9600, timeout=10, writeTimeout=10)
        time.sleep(2)
        for address in range(1):
            self.set(address,200,200,200)
            time.sleep(10)
            
        for address in range(1):
            self.set(address,0,0,0)
            time.sleep(1)
        
    def set(self, address, r, g, b):
            if self.arduino.isOpen():
                self.arduino.flush() 
                package = [address, int(r), int(g), int(b)]
                print('writing ', package)
                for i in package:
                    self.arduino.write(struct.pack('B', i))
            else:
                print("arduino is closed !")


TestLight()
