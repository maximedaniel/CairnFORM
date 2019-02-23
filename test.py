import paho.mqtt.client as mqtt


def on_connect(self, client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    self.mqtt.subscribe("cairnform")
    msg = json.dumps({"0": {'from': [10, 150, 200, 50], 'to': [255, 255, 255, 20], 'with': [2.0, 10, 'LINEAR']},
                      "4": {'from': [255, 255, 255, 50], 'to': [255, 255, 255, 100], 'with': [2.0, 3, 'LINEAR']}})
    self.mqtt.publish("cairnform", msg)


mqtt = mqtt.Client()
mqtt.on_connect = self.on_connect
mqtt.connect("iot.eclipse.org", 1883, 60)
mqtt.loop_forever()