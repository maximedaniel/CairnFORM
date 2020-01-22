import threading
from RingController import RingController
from LightController import LightController
from MotionController import MotionController


# Control a stack of rings
class StackController:

    def __init__(self):
        self.rlock = threading.RLock()
        self.light = LightController()
        self.motion = MotionController()
        self.name = 'CairnFORM_' + \
            "_".join("{:02x}".format(hat) for hat in MotionController.hats)
        self.rings = []
        for address in range(len(self.motion.maps)):
            self.rings.append(RingController(
                address, self.rlock, self.light, self.motion))
        self.reset()

    def reset(self):
        for address in range(len(self.rings)):
            self.rings[address].reset()

    def push(self, instruction):
        self.rings[instruction[0]].push(instruction[1:])
        
    def size(self):
        return len(self.motion.maps)
