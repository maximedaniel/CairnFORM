#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import RPi.GPIO as GPIO


class MotionController:
    MAX_TIME = 10 #seconds
    hats = [0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67]
    #switches = [4, 17, 18, 27, 22, 23, 24,  5,  6, 12, 13, 16]
    #hats = [0x66, 0x67]
    switches =  [21,19, 20, 16, 13,  6, 12, 5, 25, 23, 24, 22]
    maps = [0,  2,  1,  3,  4,  6,  5, 7,  8, 10,  9, 11]
    
    @staticmethod
    def rpm(duration, steps):
        return (steps * 1.8 / 360) * (60 / duration)

    def __init__(self):
        self.hats = []
        self.switch_maps = []
        GPIO.setmode(GPIO.BCM)
        # Detect plugged hats
        for index, hat in enumerate(MotionController.hats):
            try:
                self.hats.append(Adafruit_MotorHAT(hat))
            except:
                print('An error occured while processing Adafruit_MotorHAT at I2C address ' + str(hat))
        print(self.hats)
        for index, motor_hat in enumerate(self.hats):
            try:
                motor1 = motor_hat.getStepper(200, 1)
                motor1.setSpeed(30)
                switch1 = MotionController.switches[index * 2]
                GPIO.setup(switch1, GPIO.IN)
                start = time.time()
                elapse = time.time() - start
                while elapse < MotionController.MAX_TIME and GPIO.input(switch1) == 0:
                    motor1.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                    elapse = time.time() - start
                if elapse < MotionController.MAX_TIME:
                    print('Switch ', switch1, ' answered to motor ', hat, ':', 1)
                    self.switch_maps.append(MotionController.maps[index * 2])
                else :
                    print('Switch ', switch1, ' did not answered to motor ', hat, ':', 1)
                motor_hat.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
                
                # Second motor test
                
                motor2 = motor_hat.getStepper(200, 2)
                motor2.setSpeed(30)
                switch2 = MotionController.switches[index * 2 + 1]
                GPIO.setup(switch2, GPIO.IN)
                start = time.time()
                elapse = time.time() - start 
                while elapse < MotionController.MAX_TIME and GPIO.input(switch2) == 0:
                    motor2.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.DOUBLE)
                    elapse = time.time() - start
                if elapse < MotionController.MAX_TIME:
                    print('Switch ', switch2, ' answered to motor ', hat, ':', 2)
                    self.switch_maps.append(MotionController.maps[index * 2] + 1)
                else :
                    print('Switch ', switch2, ' did not answered to motor ', hat, ':', 2)
                motor_hat.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
                
            except:
                print('An error occured while processing Adafruit_MotorHAT at I2C address ' + str(hat))
                
        self.positions = [ 0 for x in range(len(self.switches))]

    #TODO add ring autodetection
    def reset(self):
        for (address, switch_map) in enumerate(self.switch_maps):
            switch = MotionController.switches[switch_map]
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



