import threading
from RingController import RingController
from LightController import LightController
from MotionController import MotionController


class StackController:

    def __init__(self):
        self.rlock = threading.RLock()
        self.light = LightController()
        self.motion = MotionController()
        self.rings = []
        for address in range(len(self.motion.switch_maps)):
            self.rings.append(RingController(address, self.rlock, self.light, self.motion))

    def push(self, instruction):
        self.rings[instruction[0]].push(instruction[1:])
