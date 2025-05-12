#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO

MAX_TIME = 10 #seconds
HATS = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]

@staticmethod
def rpm(duration, steps):
	return (steps * 1.8 / 360) * (60 / duration)

hats = []
maps = {}
GPIO.setmode(GPIO.BCM)
# Detect plugged hats
for HAT in list(HATS):
	try:
		hats.append(Adafruit_MotorHAT(HAT))
	except:
		HATS.remove(HAT)
		print('An error occured while processing Adafruit_MotorHAT at I2C address ' + str(HAT))
print("detected hats: %s" %hats)

# 0 0 1 5
while True:
	try:
		user_input = raw_input("Enter q to quit or a command <hat[0:5]> <port[0:1]> <direction[1:2] <step[1:X]>")
		if user_input == "q":
			break
		else:
			user_input = user_input.split()
			if len(user_input) != 4:
				print("Invalid command. Please enter a command in the format: <hat[0:5]> <port[0:1] <direction[1:2] <step[1:X]")
				continue
			hat_id = int(user_input[0])
			port_id = int(user_input[1])
			direction = int(user_input[2])
			steps = int(user_input[3])
			print("valid command: %d %d %d %d" %(hat_id, port_id, direction, steps))
			hat = hats[hat_id]
			motor = hat.getStepper(200, port_id + 1)
			motor.setSpeed(30)
			motor.step(steps, direction, Adafruit_MotorHAT.DOUBLE)
			#hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
			
	except KeyboardInterrupt:
		break
#	except Exception as e:
#		print('An error occured: ' + str(e))

#for i, hat in enumerate(hats):
#	try:
#		for port in range(2):
#			motor = hat.getStepper(200, port + 1)
#			motor.setSpeed(30)
#			start = time.time()
#			elapse = 0
#			while elapse < MAX_TIME:
#				motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
#				elapse = time.time() - start
#			hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
#			hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
#	except:
#		print('An error occured while processing a port of an Adafruit_MotorHAT')
