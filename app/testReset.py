#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO
import threading


class MotionController:
    MAX_TIME = 10 #seconds
    hats = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66]
    switches = [21, 19, 20, 16, 13,  6, 12, 5, 25, 24, 23, 22]
    addresses = [0,  2,  1,  3,  4,  6,  5, 7,  8, 10,  9, 11]
    
    @staticmethod
    def rpm(duration, steps):
        return (steps * 1.8 / 360) * (60 / duration)

    def __init__(self):
        self.hats = []
        self.maps = {}
        GPIO.setmode(GPIO.BCM)
        # Detect plugged hats
        for hat in list(MotionController.hats):
            try:
                self.hats.append(Adafruit_MotorHAT(hat))
            except:
                MotionController.hats.remove(hat)
                print('An error occured while processing Adafruit_MotorHAT at I2C address ' + str(hat))
        print(self.hats)

        for index, hat in enumerate(self.hats):
            try:
                for port in range(2):
					switch = MotionController.switches[index * 2 + port]
					hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
					hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
					self.maps[self.addresses[index * 2 + port]] = [switch, hat, port + 1]
            except:
                print('An error occured while processing a port of an Adafruit_MotorHAT')
                
        self.positions = [ 0 for x in range(len(self.maps))]
        print(self.maps)


    def reset(self):
        for address in self.maps:
            switch, hat, port = self.maps[address]
            #print(address, switch, hat, port)
            motor = hat.getStepper(200, port)
            motor.setSpeed(30)
            GPIO.setup(switch, GPIO.IN)
            start = time.time()
            elapse = start
            while elapse < MotionController.MAX_TIME and GPIO.input(switch) == 0:
                motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                elapse = time.time() - start
            if elapse < MotionController.MAX_TIME:
                self.positions[address] = 0
            hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
            hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
    
    def reset(self, rlock, address):
        # if motor position unknow do nothing
        if self.positions[address] < 0:
            return
            
        # if motor hat and switch unknow do nothing
        if not self.maps[address]:
            return
        
        switch, hat, port = self.maps[address]
        motor = hat.getStepper(200, port)
        motor.setSpeed(30)
        GPIO.setup(switch, GPIO.IN)
        while GPIO.input(switch) == 0:
            motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
        
        rlock.acquire()    
        hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
        hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
        rlock.release()
        print("motor reseted")

               
    def set(self, rlock, address, position, duration):
        # if motor position unknow do nothing
        if self.positions[address] < 0:
            return
            
        # if motor hat and switch unknow do nothing
        if not self.maps[address]:
            return
        
        # if motor position targeted not in range do nothinh
        if not (0 <= position <= 255):
            return
        
        if not duration:
            return
        
        steps = position - self.positions[address]
        
        if steps == 0:
            time.sleep(duration)
            return
        
        if position == 0:
            self.reset(rlock, address)
            return
            
        
            
        direction = Adafruit_MotorHAT.FORWARD if (steps > 0) else Adafruit_MotorHAT.BACKWARD
        steps = abs(steps)
        speed = MotionController.rpm(duration, steps)
        switch, hat, port = self.maps[address]
        motor = hat.getStepper(200, port)
        motor.setSpeed(speed)
        motor.step(steps, direction, Adafruit_MotorHAT.DOUBLE)
        self.positions[address] = position
        
        rlock.acquire()   
        hat.getMotor((port-1) * port + 1).run(Adafruit_MotorHAT.RELEASE)
        hat.getMotor((port-1) * port + 2).run(Adafruit_MotorHAT.RELEASE)
        rlock.release()


rlock = threading.RLock()
mc = MotionController()

# 0 0 1 5
while True:
	try:
		user_input = raw_input("Enter q to quit or a command <ring[0:11]>")
		if user_input == "q":
			break
		else:
			user_input = user_input.split()
			if len(user_input) != 1:
				print("Invalid command. Please enter a command in the format: <ring[0:11]>")
				continue
			ring_id = int(user_input[0])
			print("valid command: %d" %(ring_id))
			mc.reset(rlock, ring_id)
					
	except KeyboardInterrupt:
		break




