#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO


class MotionController:
    MAX_TIME = 10 #seconds
    hats = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67]
    switches =  [21,19, 20, 16, 13,  6, 12, 5, 25, 23, 24, 22]
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

        for index, motor_hat in enumerate(self.hats):
            try:
                for port in range(2):
                    motor = motor_hat.getStepper(200, port + 1)
                    motor.setSpeed(30)
                    switch = MotionController.switches[index * 2 + port]
                    GPIO.setup(switch, GPIO.IN)
                    start = time.time()
                    elapse = time.time() - start
                    while elapse < MotionController.MAX_TIME and GPIO.input(switch) == 0:
                        motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                        elapse = time.time() - start
                    if elapse < MotionController.MAX_TIME:
                        print('Switch ', switch, ' answered to motor ', hat, ':', port)
                        self.maps[self.addresses[index * 2 + port]] = [switch, motor_hat, port + 1]
                    else :
                        print('Switch ', switch, ' did not answered to motor ', hat, ':', port)
                    motor_hat.getMotor(port + 1).run(Adafruit_MotorHAT.RELEASE)
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
            hat.getMotor(port).run(Adafruit_MotorHAT.RELEASE)
    
    def reset(self, address):
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
        hat.getMotor(port).run(Adafruit_MotorHAT.RELEASE)
        
    def set(self, address, position, duration):
        # if motor position unknow do nothing
        if self.positions[address] < 0:
            return
            
        # if motor hat and switch unknow do nothing
        if not self.maps[address]:
            return
        
        # if motor position targeted not in range do nothinh
        if not (0 < position < 200):
            return
        
        if not duration:
            return
        
        steps = position - self.positions[address]
        
        if not steps:
            return 0
            
        direction = Adafruit_MotorHAT.FORWARD if (steps > 0) else Adafruit_MotorHAT.BACKWARD
        steps = abs(steps)
        speed = MotionController.rpm(duration, steps)
        switch, hat, port = self.maps[address]
        motor = hat.getStepper(200, port)
        motor.setSpeed(speed)
        motor.step(steps, direction, Adafruit_MotorHAT.DOUBLE)
        self.positions[address] = position
        hat.getMotor(port).run(Adafruit_MotorHAT.RELEASE)



