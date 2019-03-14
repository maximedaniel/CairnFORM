#!/usr/bin/python
import threading
from Transition import Transition
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import numpy as np
import time
np.set_printoptions(precision=3)


class RingController:
    FREQ = 0.1

    def __init__(self, address, rlock, light, motion):
        # props
        self.address = address
        self.rlock = rlock
        self.light = light
        self.motion = motion

        # Thread
        self.thread = threading.Thread(target=self.run, args=[self.rlock])

        # states
        self.s = [0., 0., 0., 0.]
        self.delay_completion = 0
        self.duration_completion = 0
        self.instructions = []
        
    def reset(self):
        self.light.reset(self.rlock, self.address)
        self.motion.reset(self.rlock, self.address)
        self.s = [0., 0., 0., 0.]
        
    def push(self, instruction):
        self.instructions.append(instruction)
        if not self.thread.isAlive():
            self.thread = threading.Thread(target=self.run, args=[self.rlock])
            self.thread.start()

    def run(self, rlock):
        while len(self.instructions):
            instruction = self.instructions.pop(0)
            target = np.array(instruction[:4]).astype(float)
            delay, duration = np.array(instruction[4:-1]).astype(float)
            mode = instruction[-1]

            self.delay_completion = 0
            self.duration_completion = 0

            for elapse_time in np.arange(0.0, delay + RingController.FREQ, RingController.FREQ):
                self.delay_completion = int(elapse_time / delay * 100) if delay else 0
                time.sleep(RingController.FREQ)

            s_diff = np.array(target) - np.array(self.s)
            s_diff_abs = np.absolute(s_diff)
            s_diff_sign = np.sign(s_diff)
            
            
            ### OPTIMZING ?
            #red_timeline = np.linspace(0.0, duration, num=s_diff_abs[0])
            #green_timeline = np.linspace(0.0, duration, num=s_diff_abs[1])
            #blue_timeline = np.linspace(0.0, duration, num=s_diff_abs[2])
            #position_timeline = np.linspace(0.0, duration, num=s_diff_abs[3])
            #timeline = np.concatenate([red_timeline, green_timeline, blue_timeline, position_timeline]).ravel()
            #timeline = np.unique(timeline)
            #morph = np.array([[int(t in red_timeline), int(t in green_timeline), int(t in blue_timeline), int(t in position_timeline)]*s_diff_sign for t in timeline])
            #delta_timeline = np.append(np.diff(timeline), 0)
            #for delta_m, delta_t in zip(morph, delta_timeline):
                #self.s += delta_m
                #self.s[:3] = np.clip(self.s[:3], 0., 255.)
                #self.s[3] = np.clip(self.s[3], 0., 200.)
                #rlock.acquire()
                #self.light.set(self.address, int(self.s[0]), int(self.s[1]), int(self.s[2]))
                #if(delta_m[-1] > 0) :
                    #self.motion.moveBy(self.address, 1, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE, delta_t)
                #else:
                    #self.motion.moveBy(self.address, 1, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE, delta_t)
                #rlock.release()
            
            time_range = np.arange(0.0, duration, RingController.FREQ)
            i = 0
            s_current = np.array([0., 0., 0., 0.]) 
            while True:
                s_next = Transition.transition(mode, time_range[i] + RingController.FREQ, 0, s_diff_abs, duration)
                s_next *= s_diff_sign
                s_delta = s_next - s_current
                self.s += s_delta
                self.s[:3] = np.clip(self.s[:3], 0., 255.)
                self.s[3] = np.clip(self.s[3], 0., 200.)
                self.light.set(rlock, self.address, int(self.s[0]), int(self.s[1]), int(self.s[2]))
                self.motion.set(rlock, self.address, int(self.s[3]), RingController.FREQ)
                self.duration_completion = int(time_range[i] / duration * 100) if duration else 0
                i = i + 1
                if i >= len(time_range):
                    break
                s_current = Transition.transition(mode, time_range[i], 0, s_diff_abs, duration)
                s_current *= s_diff_sign



                

