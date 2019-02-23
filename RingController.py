import threading

from driver.Transition import Transition
import numpy  as np
import time



class RingController:

    FREQ = 0.1

    def __init__(self, rlock):
        # Threading
        self.alive = False
        self.thread = threading.Thread(target=self.run, args=[rlock])

        # Attributes
        self.s = [0,0,0,0]
        self.s_from = [0,0,0,0]
        self.s_to = [0,0,0,0]
        self.s_with = [0,0,'LINEAR']
        self.delay_completion = 0
        self.duration_completion = 0

    def setMorph(self, s_from, s_to, s_with):
        self.s_from = s_from
        self.s_to = s_to
        self.s_with = s_with

    def morph(self):
        self.alive = True
        self.thread.start()

    def run(self, rlock):
        self.delay_completion = 0
        self.duration_completion = 0
        delay = self.s_with[0]
        duration = self.s_with[1]
        mode = self.s_with[2]
        for elapse_time in np.arange(0.0, delay+RingController.FREQ, RingController.FREQ):
            self.delay_completion = int(elapse_time/delay * 100)
            time.sleep(RingController.FREQ)

        self.s = self.s_from
        s_diff = np.array(self.s_to) - np.array(self.s_from)
        for elapse_time in np.arange(0.0, duration+RingController.FREQ, RingController.FREQ):

            s_current = Transition.transition(mode, elapse_time, 0, s_diff, duration)
            s_next = Transition.transition(mode, elapse_time+RingController.FREQ, 0, s_diff, duration)
            s_delta = s_next - s_current
            rlock.acquire()
            self.s += s_delta
            self.duration_completion = int(elapse_time/duration * 100)
            time.sleep(RingController.FREQ)
            rlock.release()

        self.delay_completion = 0
        self.duration_completion = 0
        self.alive = False
