#!/usr/bin/python
import sys
import atexit
import struct
import math
import numpy as np
from Transition import Transition
import random
import time
import sys
import threading
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import RPi.GPIO as GPIO
POSITION_MAX = 450
GRANULARITY = 0.1

def getRPM(duration, steps):
    return (steps*1.8/ 360)* (60/duration)

class Ring:
    
    def __init__(self, address, parent, debug=False):
        self.parent = parent
        self.address = address
        self.light = np.array([-1.,-1.,-1.])
        self.next_light = self.light
        self.motion = -1.
        self.next_motion = self.motion
        self.motion_sign = 0
        self.light_sign = np.array([0.,0.,0.])
        self.debug = debug
        self.lightmorphing = []
        self.motionmorphing = []


    def isUnknow(self):
        ret=False
        if self.light[0] < 0 or self.light[1] < 0 or self.light[2] < 0 or self.motion < 0:
            ret = True
        if self.debug:
            print('R'+str(self.address)+'\t'*self.address, ret)
        return ret

    def reset(self, lock, r=0., g=0., b=0.):
        self.light = self.next_light = np.array([r,g,b])
        lock.acquire()
        self.parent.lightController.changeColor(self.address, r, g, b)
        lock.release()
        mh = self.parent.motionController.get(self.address)
        m = mh.getStepper(200, int(self.address%2)+1)  # 200 steps/rev, motor port #1
        m.setSpeed(30)
        GPIO.setup(self.parent.switches[self.address],GPIO.IN)
        while GPIO.input(self.parent.switches[self.address]) == 0:
            m.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
        lock.acquire()
        self.parent.motionController.release(self.address)
        lock.release()
        self.motion = self.next_motion = 0

        if self.debug:
            print('R'+str(self.address)+'\t'*self.address, self.light)
            
        ghost_pos = random.randint(1, 250)
        while ghost_pos>0:
            if self.debug:
                print('R'+str(self.address)+'\t'*self.address, ghost_pos)
            ghost_pos -= 5
            time.sleep(0.1)
        self.motion = self.next_motion = 0
        if self.debug:
            print('R'+str(self.address)+'\t'*self.address, self.position)

    def setLight(self, light, duration, mode=Transition.LINEAR):
        duration = float("{0:.1f}".format(duration))
        diff_light = np.array(light)-np.array(self.next_light)
        if duration < GRANULARITY:
            self.lightmorphing.append(diff_light)
            self.next_light = light
            return
        for elapse_time in np.arange(0.0, duration, GRANULARITY):
            current_light = Transition.transition(mode, elapse_time, 0, diff_light, duration)
            forward_light = Transition.transition(mode, elapse_time+GRANULARITY, 0, diff_light, duration)
            delta_light = forward_light-current_light
            self.lightmorphing.append(delta_light)
        self.next_light = light

    def setMotion(self, motion, duration, mode=Transition.LINEAR):
        #self.motion_sign = np.sign(motion-self.motion)
        duration = float("{0:.1f}".format(duration))
        diff_motion = motion-self.next_motion
        remaining = 0
        if duration < GRANULARITY:
            self.motionmorphing.append((diff_motion,getRPM(GRANULARITY, diff_motion)))
            self.next_motion = motion
            return
        for elapse_time in np.arange(0.0, duration, GRANULARITY):
            current_motion = Transition.transition(mode, elapse_time, 0, diff_motion, duration)
            next_motion = Transition.transition(mode, elapse_time+GRANULARITY, 0, diff_motion, duration)
            delta_motion = next_motion-current_motion
            remaining, delta_motion =  math.modf(delta_motion + remaining)
            
            self.motionmorphing.append((int(delta_motion),int(getRPM(GRANULARITY, delta_motion))))
        self.next_motion = motion

    def morph(self, lock):
        mh = self.parent.motionController.get(self.address)
        m = mh.getStepper(200, int(self.address%2)+1)  # 200 steps/rev, motor port #1
        remaining = 0
        for delta_light, delta_motion in zip(self.lightmorphing, self.motionmorphing):
            self.motion += delta_motion[0]
            self.light += delta_light
            lock.acquire()
            self.parent.lightController.changeColor(self.address, self.light[0], self.light[1], self.light[2])
            lock.release()
            sign = (3+np.sign(delta_motion[0]))%3
            #print("R",self.address, "  motion: ", step_motion)
            if not delta_motion[0]:
                time.sleep(0.1)
            else:
                #print(int(abs(delta_motion[1])), abs(step_motion))
                m.setSpeed(int(abs(delta_motion[1])))
                m.step(abs(delta_motion[0]), sign,  Adafruit_MotorHAT.DOUBLE)
                
        lock.acquire()
        self.parent.motionController.release(self.address)
        lock.release()
        self.lightmorphing = []
        self.motionmorphing = [] 

    def setMorph(self, light, motion, duration, mode=Transition.LINEAR):
        #print('R'+str(self.address)+'\t'*self.address, light, motion, duration, mode)
        self.setLight(light, duration, mode)
        self.setMotion(motion, duration, mode)
        # diff_duration = int(duration/GRANULARITY)

        # diff_light = np.array(light)-np.array(self.light)
        # delta_light = diff_light/diff_duration
        # tmp_light = self.light.astype(float)

        # diff_motion = np.array(motion)-np.array(self.motion)
        # delta_motion = diff_motion/diff_duration

        # for i in range(diff_duration):
        #     tmp_light += delta_light
        #     print('R'+str(self.address)+'\t'*self.address, tmp_light.astype(int))
        #     time.sleep(GRANULARITY)
        # self.light = tmp_light.astype(int)
