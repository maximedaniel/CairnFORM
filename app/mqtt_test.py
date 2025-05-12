from random import *
import paho.mqtt.client as mqtt
import json

hats = [0x66, 0x67]
topic = 'CairnFORM:'+ ":".join("{:02x}".format(hat) for hat in hats) + '/input'
print(topic)
mqtt = mqtt.Client("MaximeDaniel")


def description(client, userdata, msg):
	print('description TOPIC')
	try:
		m_decode = msg.payload.decode('utf-8', 'ignore')
		m_in = json.loads(m_decode)
		print(m_in)
	except Exception as ex:
		print(ex)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    #mqtt.subscribe('+/desc')
    #mqtt.message_callback_add('+/desc', description)
    #mqtt.publish('+/desc', 'desc')
    instructions = [[] for i in range(4)]
    #instructions[0] = [0, randrange(255),  randrange(255), randrange(255), 0, 1, 4, 'EASE_IN_OUT_QUINT']
    #instructions[1] = [1, randrange(255),  randrange(255), randrange(255), 0, 1, 4, 'EASE_IN_OUT_QUINT']
    instructions[0] = [0,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT']
    instructions[1] = [1,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT']
    instructions[2] = [2,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT']
    instructions[3] = [3,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT']
    #for i in range(len(instructions)):
    #	instructions[i] = [randrange(2), randrange(255),  randrange(255), randrange(255), 0, randrange(2)+1, randrange(4)+1, 'EASE_IN_OUT_QUINT']
    payload = {'instructions': instructions}
    print(payload)
    mqtt.publish(topic, json.dumps(payload))

def on_disconnect(client, userdata, rc):
    print("Disconnected with result code "+str(rc))
   

mqtt.on_connect = on_connect
mqtt.on_disconnect = on_disconnect
mqtt.connect("mqtt.estia.fr", 1883, 60)
mqtt.loop_forever()
            
