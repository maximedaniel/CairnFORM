#!/usr/bin/python
import threading
from Transition import Transition
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import numpy as np
import time
np.set_printoptions(precision=3)


# Control the light and motion of an addressed ring
class RingController:
    FREQ = 0.2

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
                self.delay_completion = int(
                    elapse_time / delay * 100) if delay else 0
                time.sleep(RingController.FREQ)

            s_diff = np.array(target) - np.array(self.s)
            s_diff_abs = np.absolute(s_diff)
            s_diff_sign = np.sign(s_diff)

            time_range = np.arange(0.0, duration, RingController.FREQ)
            i = 0
            s_current = np.array([0., 0., 0., 0.])
            while True:
                s_next = Transition.transition(
                    mode, time_range[i] + RingController.FREQ, 0, s_diff_abs, duration)
                s_next *= s_diff_sign
                s_delta = s_next - s_current
                self.s += s_delta
                self.s[:3] = np.clip(self.s[:3], 0., 255.)
                self.s[3] = np.clip(self.s[3], 0., 200.)
                self.light.set(rlock, self.address, int(
                    self.s[0]), int(self.s[1]), int(self.s[2]))
                self.motion.set(rlock, self.address, int(
                    self.s[3]), RingController.FREQ)
                i = i + 1
                if i >= len(time_range):
                    break
                s_current = Transition.transition(
                    mode, time_range[i], 0, s_diff_abs, duration)
                s_current *= s_diff_sign