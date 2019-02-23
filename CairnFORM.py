import paho.mqtt.client as mqtt

class CairnFORM:

    def __init__(self):
        self.driver = Driver()
        self.mqtt = mqtt.Client()
        client.on_connect = on_connect
        client.connect("iot.eclipse.org", 1883, 60)
        client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        self.mqtt.subscribe("cairnform/log")
        for ring in self.driver.rings:-
            self.mqtt.subscribe("cairnform/input/"+ring)
            self.mqtt.message_callback_add("cairnform/input/"+ring, lambda x, y, z: self.driver.morph())


CairnFORM()
