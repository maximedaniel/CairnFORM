import RPi.GPIO as GPIO

class SwitchController:
    def __init__(self, switches):
        self.switches = switches
        GPIO.setmode(GPIO.BCM)
        for switch in self.switches:
            GPIO.setup(switch,GPIO.IN)

    def isPressed(self, address):
        return GPIO.input(self.switches[address])
