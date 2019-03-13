from random import *
import paho.mqtt.client as mqtt
from driver.StackController import StackController
from driver.Transition import Transition
import json
from CUI import CUI


class CairnFORM:

    def __init__(self):
        self.stack = StackController()
        #try:
        #    self.cui = CUI(self.stack)
        #except (KeyboardInterrupt, SystemExit):
        #    print('\n! Received keyboard interrupt, quitting threads.\n')

        self.mqtt = mqtt.Client("CairnFORM")
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_disconnect = self.on_disconnect

        self.mqtt.connect("mqtt.estia.fr", 1883, 60)
        self.mqtt.loop_forever()
        #self.test()
    
    def test(self):
        instructions = [[] for i in range(randrange(1, 2))]
        for i in range(len(instructions)):
            instructions[i] = [randrange(len(self.stack.rings)), randrange(255), randrange(255), randrange(255), randrange(100), randrange(5)+1, randrange(5)+1, 'EASE_IN_OUT_QUINT']
        
        for instruction in instructions:
            print("sending ", instruction)
            self.stack.push(instruction)
            
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        print('subscribing to: ', self.stack.name) 
        self.mqtt.subscribe(self.stack.name)
        print('subscribed to: ', self.stack.name) 
        self.mqtt.message_callback_add(self.stack.name, self.process)

        #instructions = [[] for i in range(randrange(10, 20))]
        #for i in range(len(instructions)):
        #    instructions[i] = [randrange(len(self.stack.rings)), randrange(255), randrange(255), randrange(255), randrange(100), randrange(5)+1, randrange(5)+1, 'EASE_IN_OUT_QUINT']

        #payload = {'instructions':instructions}
        #self.mqtt.publish(self.name, json.dumps(payload))

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code "+str(rc))

    def process(self, client, userdata, msg):
        try:
            print(msg.payload)
            m_decode = msg.payload.decode("utf-8", "ignore")
            m_in = json.loads(m_decode)  # decode json data
            instructions = m_in['instructions']
            for instruction in instructions:
                    address = instruction[0]
                    target = instruction[1:5]
                    delay, duration, mode = instruction[5:]

                    if not (0 <= address < len(self.stack.rings)):
                        raise Exception("assertion failed for  (0 <= address < "+len(self.stack.rings)+")")

                    if not (0 <= target[0] <= 255 and 0 <= target[1] <= 255  and 0 <= target[2] <= 255 and 0 <= target[3] <= 100):
                        raise Exception("assertion failed for (0 <= red <= 255 and 0 <= green <= 255  and 0 <= blue <= 255 and 0 <= position <= 100)")

                    if not (0 <= delay):
                        raise Exception("assertion failed for (0 <= delay)")

                    if not (0 <= duration):
                        raise Exception("assertion failed for (0 <= duration)")

                    if not Transition.isMode(mode):
                        raise Exception("assertion failed for (Transition.isMode(mode))")

                    self.stack.push(instruction)
        except Exception as ex:
            print(ex)
            pass


CairnFORM()
