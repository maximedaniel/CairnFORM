#!/usr/bin/python
import threading
from Transition import Transition
import numpy as np
import time


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
        self.s = [0, 0, 0, 0]
        self.delay_completion = 0
        self.duration_completion = 0
        self.instructions = []
        
    def reset(self):
        self.light.reset(self.address)
        self.motion.reset(self.address)
        self.s = [0, 0, 0, 0]
        
    def push(self, instruction):
        self.instructions.append(instruction)
        if not self.thread.isAlive():
            self.thread = threading.Thread(target=self.run, args=[self.rlock])
            self.thread.start()

    def run(self, rlock):
        while len(self.instructions):
            instruction = self.instructions.pop(0)
            target = instruction[:4]
            delay, duration, mode = instruction[4:]

            self.delay_completion = 0
            self.duration_completion = 0

            for elapse_time in np.arange(0.0, delay + RingController.FREQ, RingController.FREQ):
                self.delay_completion = int(elapse_time / delay * 100) if delay else 0
                time.sleep(RingController.FREQ)

            s_diff = np.array(target) - np.array(self.s)
            print(self.address,':',s_diff)
            for elapse_time in np.arange(0.0, duration + RingController.FREQ, RingController.FREQ):
                print('s_current transition with elapse_time: ', elapse_time, ' and s_diff: ', s_diff)
                s_current = Transition.transition(mode, elapse_time, 0, s_diff, duration)
                print('s_next transition with elapse_time: ', elapse_time + RingController.FREQ, ' and s_diff: ', s_diff)
                s_next = Transition.transition(mode, elapse_time + RingController.FREQ, 0, s_diff, duration)
                s_delta = s_next - s_current
                print('s_delta = s_next - s_current = ', s_delta)
                # Calling controllers
                rlock.acquire()
                self.s += s_delta
                self.s[self.s < 0] = 0
                print('self.s = ', self.s)
                #print(self.s)
                self.light.set(self.address, int(self.s[0]), int(self.s[1]), int(self.s[2]))
                self.motion.set(self.address, int(self.s[3]), RingController.FREQ)
                self.duration_completion = int(elapse_time / duration * 100) if duration else 0
                #time.sleep(RingController.FREQ)
                rlock.release()

            self.delay_completion = 0
            self.duration_completion = 0

