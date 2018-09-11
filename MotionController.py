#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
#from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import sys
import atexit
import struct

class MotionController:
    
    def __init__(self):
        mh01 = Adafruit_MotorHAT(addr=0x61)
        mh23 = Adafruit_MotorHAT(addr=0x62)
        mh45 = Adafruit_MotorHAT(addr=0x63)
        mh67 = Adafruit_MotorHAT(addr=0x64)
        mh89 = Adafruit_MotorHAT(addr=0x65)
        self.motor_hats = [mh01, mh23, mh45, mh67, mh89]
    
    def get(self, address):
        mh = self.motor_hats[int(address/2)]
        #print("get motor.")
        #m = mh.getStepper(200, int(address%2)+1)  # 200 steps/rev, motor port #1
        return mh
    
    def release(self, address):
        mh = self.motor_hats[int(address/2)]
        port = int(address%2)
        if not port :
            mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        else :
            mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

        
    def releaseAll(self):
        for address in range(10):
            self.release(address)
