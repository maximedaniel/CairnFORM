from random import *
import paho.mqtt.client as mqtt
from driver.StackController import StackController
from driver.Transition import Transition
import json
from pprint import pprint
from CUI import CUI


class CairnFORM:

    def __init__(self):
        self.stack = StackController()
        #try:
        #    self.cui = CUI(self.stack)
        #except (KeyboardInterrupt, SystemExit):
        #    print('\n! Received keyboard interrupt, quitting threads.\n')

        self.mqtt = mqtt.Client("CairnFORM")
        self.topic_desc = self.stack.name + "/desc"
        self.topic_input = self.stack.name + "/input"
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
            self.stack.push(instruction)

                   
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.mqtt.subscribe(self.topic_desc)
        print("Subscribed to ", self.topic_desc)
        self.mqtt.message_callback_add(self.topic_desc, self.description)
        self.mqtt.subscribe(self.topic_input)
        print("Subscribed to ", self.topic_input)
        self.mqtt.message_callback_add(self.topic_input, self.process)

        #instructions = [[] for i in range(randrange(10, 20))]
        #for i in range(len(instructions)):
        #    instructions[i] = [randrange(len(self.stack.rings)), randrange(255), randrange(255), randrange(255), randrange(100), randrange(5)+1, randrange(5)+1, 'EASE_IN_OUT_QUINT']

        #payload = {'instructions':instructions}
        #self.mqtt.publish(self.name, json.dumps(payload))

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code "+str(rc))

    def description(self, client, userdata, msg):
        #pprint(vars(client))
        if client._client_id != self.mqtt._client_id:
            payload = {
            'description':'Stack of expandable illuminated ring by Maxime DANIEL',
            'input': "instructions:[[address(0..N), red(0..255), green(0..255), blue(0..255), position(0..200), delay(0..*), duration(0..*), transition(String)], ..]"
                }
            print(payload)
            self.mqtt.publish(self.topic_desc, json.dumps(payload))
            
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

                    if not (0 <= target[0] <= 255 and 0 <= target[1] <= 255  and 0 <= target[2] <= 255 and 0 <= target[3] <= 200):
                        raise Exception("assertion failed for (0 <= red <= 255 and 0 <= green <= 255  and 0 <= blue <= 255 and 0 <= position <= 200)")

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
