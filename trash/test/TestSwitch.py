#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO


class TestSwitch:
    MAX_TIME = 30

    def __init__(self):
        switches = [21, 20, 19, 16, 13, 12, 6, 5, 25, 23, 24, 22]
        GPIO.setmode(GPIO.BCM)
        start = time.time()
        elapse = time.time() - start
        for switch in switches:
            GPIO.setup(switch, GPIO.IN)
        while elapse < TestSwitch.MAX_TIME:
            os.system('cls' if os.name == 'nt' else 'clear')
            print([GPIO.input(switch) for switch in switches])
            elapse = time.time() - start


TestSwitch()
