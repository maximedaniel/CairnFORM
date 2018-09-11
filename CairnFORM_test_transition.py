from RingController import RingController
import time
import paho.mqtt.client as mqtt

from Transition import Transition

ring = RingController(0, debug = True)
ring.reset(r=0, g=0, b=0)
ring.setMorph(200, [0, 200,0], 3.0, 0.05, Transition.EASE_IN_OUT_CIRC, 0)
#ring.morph()
end = time.time()
