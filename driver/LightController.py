#!/usr/bin/python
from serial import *
import time
import struct

# Control the brightness and the color of an addressed ring
class LightController:
    def __init__(self):
        self.arduino = Serial(port="/dev/ttyACM0",
                              baudrate=9600, timeout=10, writeTimeout=10)
        time.sleep(2)

    def reset(self, rlock, address):
        self.set(rlock, address, 0, 0, 0)

    def set(self, rlock, address, r, g, b):
        if self.arduino.isOpen():
            self.arduino.flush()
            package = [address, r, g, b]
            #print('writing ', package)
            rlock.acquire()
            for i in package:
                self.arduino.write(struct.pack('B', i))
            rlock.release()
        else:
            print("arduino is closed !")
