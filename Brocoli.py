import paho.mqtt.client as mqtt
import json
import datetime
import numpy as np
import time
from CairnFORM import CairnFORM

class Brocoli(mqtt.Client):

    cairnform = None
    mqttc = None
    size = 0
    
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))


    def on_message(self, mqttc, obj, msg):
        print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        if len(msg.payload):
            try:
                m_decode = str(msg.payload.decode("utf-8","ignore"))
                target = json.loads(m_decode)
                if 'morph' in target:
                    self.cairnform.setMorph(target['morph'])
                    self.cairnform.morph()
                if 'reset' in target:
                    self.cairnform.reset()
            except:
                pass


    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))


    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))


    def on_log(self, mqttc, obj, level, string):
        print(string)

    def run(self, size):
        #self.now = datetime.datetime.now()
        #self.hour_range = hour_range
        #datetime_start = self.now.replace(hour=hour_start,minute=0, second=0, microsecond=0)
        #self.timestamps = [datetime_start + datetime.timedelta(hours=i) for i in range(hour_range)]
        #self.productions =  [0 for i in range(hour_range)]
        #self.consumptions = [0 for i in range(hour_range)]
        self.size = size
        self.cairnform = CairnFORM(self.size, debug=False)
        self.cairnform.reset()
        isConnected = False
        while not isConnected:
            try:
                self.connect("192.168.0.1", 1883, 3600)
                isConnected = True
            except Exception as e:
                print(e)
                print("Retrying...")
            
        self.subscribe('mqtt/cairnform')
        self.loop_forever()
        

# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.

# Uncomment to enable debug messages
# mqttc.on_log = on_log

time.sleep(30)
Brocoli().run(10)

    
