#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO

MAX_TIME = 10 #seconds
HATS = [str(0x61), str(0x62), str(0x63), str(0x64), str(0x65), str(0x66)]

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
# loop through user input if q then stop loop else move stepper motor given direction and number of steps
# forward = 1
# backward = 2 
# 0 0 1 5
while True:
	try:
		user_input = input('Enter a command (q to quit): ')
		if user_input == 'q':
			break
		else:
			user_input = user_input.split()
			if len(user_input) != 4:
				print('Invalid command. Please enter a command in the format: <hat> <port> <direction> <steps>')
				continue
			hat_id = user_input[0]
			port_id = int(user_input[1])
			direction = int(user_input[2])
			steps = int(user_input[3])
			if hat_id not in HATS:
				print('Invalid hat id. Please enter a valid hat id.')
				continue
			hat = hats[hat_id]
			motor = hat.getStepper(200, port_id + 1)
			motor.setSpeed(30)
			motor.step(steps, direction, Adafruit_MotorHAT.DOUBLE)
			 
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('An error occured: ' + str(e))



for i, hat in enumerate(hats):
	try:
		for port in range(2):
			motor = hat.getStepper(200, port + 1)
			motor.setSpeed(30)
			start = time.time()
			elapse = 0
			while elapse < MAX_TIME:
				motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
				elapse = time.time() - start
			hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
			hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
	except:
		print('An error occured while processing a port of an Adafruit_MotorHAT')

