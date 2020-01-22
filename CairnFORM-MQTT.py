from random import *
import paho.mqtt.client as mqtt
from driver.StackController import StackController
from driver.Transition import Transition
import json
from pprint import pprint
from CUI import CUI
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni


class CairnFORM:

    def __init__(self):
        self.stack = StackController()
        self.mqtt = mqtt.Client(self.stack.name)
        self.mqtt.username_pw_set(username="a0685b26", password="a31d5cfd03af338b")
        self.topic_output = self.stack.name + "/output"
        self.topic_input = self.stack.name + "/input"
        self.mqtt.on_connect = self.on_connect
        self.mqtt.on_disconnect = self.on_disconnect

        self.mqtt.connect("broker.shiftr.io", 1883, 60)
        self.mqtt.loop_forever()

                   
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.mqtt.subscribe(self.topic_input)
        print("Subscribed to ", self.topic_input)
        self.mqtt.message_callback_add(self.topic_input, self.input)

    def on_disconnect(self, client, userdata, rc):
        print("Disconnected with result code "+str(rc))

    def output(self, msg):
        addr = ni.ifaddresses('eth0')[AF_INET][0]['addr'] or ni.ifaddresses('l0')[AF_INET][0]['addr']
        payload = {'vnc': addr, 'message': msg}
        self.mqtt.publish(self.topic_output, json.dumps(payload))
            
    def input(self, client, userdata, msg):
        try:
            m_decode = msg.payload.decode("utf-8", "ignore")
            m_in = json.loads(m_decode)  # decode json data
            instructions = m_in['instructions']
            for instruction in instructions:
                    if not (len(instruction) == 8):
                        raise Exception("assertion failed for  (len(instruction) == 8)")
                        
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
            self.output("ok")
        except Exception as ex:
            self.output(str(ex))
            pass

CairnFORM()
