from random import *
import paho.mqtt.client as mqtt
from driver.StackController import StackController
import json
from CUI import CUI


class CairnFORM:

    def __init__(self):
        self.stack = StackController()
        #try:
        #    self.cui = CUI(self.stack)
        #except (KeyboardInterrupt, SystemExit):
        #    print('\n! Received keyboard interrupt, quitting threads.\n')

        #self.mqtt = mqtt.Client("CairnFORM")
        #self.mqtt.on_connect = self.on_connect
        #self.mqtt.connect("test.mosquitto.org", 1883, 60)
        #self.mqtt.loop_forever()
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
        self.mqtt.subscribe("mqtt/cairnform")
        self.mqtt.message_callback_add("mqtt/cairnform", self.process)

        instructions = [[] for i in range(randrange(10, 20))]
        for i in range(len(instructions)):
            instructions[i] = [randrange(len(self.stack.rings)), randrange(255), randrange(255), randrange(255), randrange(100), randrange(5)+1, randrange(5)+1, 'EASE_IN_OUT_QUINT']

        payload = {'instructions':instructions}
        self.mqtt.publish("mqtt/cairnform", json.dumps(payload))

    def process(self, client, userdata, msg):
        try:
            print(msg.payload)
            m_decode = msg.payload.decode("utf-8", "ignore")
            m_in = json.loads(m_decode)  # decode json data
            instructions = m_in['instructions']
            for instruction in instructions:
                    self.stack.push(instruction)
                    # s_address = int(header)
                    # c_address = (0 <= s_address < len(self.stack.rings))
                    # s_from = body['from']
                    # c_from = (0 <= s_from[0] <= 255 and 0 <= s_from[1] <= 255  and 0 <= s_from[2] <= 255 and 0 <= s_from[3] <= 100)
                    # s_to = body['to']
                    # c_to = (0 <= s_to[0] <= 255 and 0 <= s_to[1] <= 255  and 0 <= s_to[2] <= 255 and 0 <= s_to[3] <= 100)
                    # s_with = body['with']
                    # c_with = (s_with[0] >= 0 and s_with[1] > 0 and isinstance(s_with[2], str))
                    # if c_address and c_from and c_to and c_with:
                    #     self.stack.setMorph(s_address, s_from, s_to, s_with)
                    # else :
                    #     print('[ERROR] json with bad structure')
        except Exception as ex:
            print('[ERROR]', ex)
            pass


CairnFORM()
