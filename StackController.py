import threading

from RingController import RingController


class StackController:

    def __init__(self):
        self.rlock = threading.RLock()
        self.rings = [RingController(self.rlock) for address in range(10)]

    def setMorph(self, c_address, c_from, c_to, c_with):
        self.rings[c_address].setMorph(c_from, c_to, c_with)

    def morph(self):
        for ring in self.rings:
            ring.morph()