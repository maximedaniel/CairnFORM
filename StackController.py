import threading

from RingController import RingController


class StackController:

    def __init__(self):
        self.rlock = threading.RLock()
        self.rings = [RingController(self.rlock) for address in range(10)]

    def push(self, instruction):
        self.rings[instruction[0]].push(instruction[1:])