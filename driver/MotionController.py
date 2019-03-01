#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO


class MotionController:
    MAX_TIME = 10 #seconds

    @staticmethod
    def rpm(duration, steps):
        return (steps * 1.8 / 360) * (60 / duration)

    def __init__(self):
        self.hats = [Adafruit_MotorHAT(addr=0x61),
                     Adafruit_MotorHAT(addr=0x62),
                     Adafruit_MotorHAT(addr=0x63),
                     Adafruit_MotorHAT(addr=0x64),
                     Adafruit_MotorHAT(addr=0x65),
                     Adafruit_MotorHAT(addr=0x66)]
        self.positions = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.switches  = [ 4, 17, 18, 27, 22, 23, 24,  5,  6, 12, 13, 16]
        GPIO.setmode(GPIO.BCM)
        self.reset()

    #TODO add ring autodetection
    def reset(self):
        for (address, switch) in enumerate(self.switches):
            port = int(address % 2)
            hat = self.hats[port]
            motor = hat.getStepper(200, port + 1)
            motor.setSpeed(30)
            GPIO.setup(switch, GPIO.IN)
            start = time.time()
            elapse = start
            while elapse < MotionController.MAX_TIME and GPIO.input(switch) == 0:
                motor.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                elapse = time.time() - start
            if elapse < MotionController.MAX_TIME:
                self.positions[address] = 0
            hat.getMotor(port + 1).run(Adafruit_MotorHAT.RELEASE)
            hat.getMotor(port + 2).run(Adafruit_MotorHAT.RELEASE)

    def set(self, address, position, duration):
        # if motor position unknow do nothing
        if self.positions[address] < 0:
            return
        
        # if motor position targeted not in range do nothinh
        if not (0 < position < 200):
            return
        
        steps = position - self.position[address]
        direction = Adafruit_MotorHAT.FORWARD if (steps > 0) else Adafruit_MotorHAT.BACKWARD
        steps = abs(steps)
        speed = MotionController.rpm(duration, steps)
        
        port = int(address % 2)
        hat = self.hats[port]
        motor = hat.getStepper(200, port + 1)
        
        motor.setSpeed(speed)
        motor.step(steps, direction, Adafruit_MotorHAT.DOUBLE)
        self.positions[address] = position
        hat.getMotor(port + 1).run(Adafruit_MotorHAT.RELEASE)
        hat.getMotor(port + 2).run(Adafruit_MotorHAT.RELEASE)



