import paho.mqtt.client as mqtt
import json
from pynput.keyboard import Key, Listener
import sys


def on_press(key):
    key_press = key
    print("PRESSED", key_press)
    if key_press == Key.space:
        msg = json.dumps({"0": {'from': [10, 150, 200, 50], 'to': [255, 255, 255, 20], 'with': [2.0, 10, 'LINEAR']},
                          "4": {'from': [255, 255, 255, 50], 'to': [255, 255, 255, 100], 'with': [2.0, 3, 'LINEAR']}})
        print(msg)
        mqtt.publish("mqtt/cairnform", msg)
    if key_press == Key.esc:
        sys.exit(0)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    mqtt.subscribe("mqtt/cairnform")
    with Listener(on_press=on_press) as listener:
        listener.join()


mqtt = mqtt.Client()
mqtt.on_connect = on_connect
mqtt.connect("test.mosquitto.org", 1883, 60)
mqtt.loop_forever()