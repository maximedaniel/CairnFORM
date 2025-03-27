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
exit()
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

