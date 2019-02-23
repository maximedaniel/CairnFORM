  #!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from driver.Adafruit_MotorHAT import Adafruit_MotorHAT
  import RPi.GPIO as GPIO
from serial import *
import time
  import atexit
import struct

NUM_EIR = 10
arduino = Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1)
time.sleep(2)

### LEDS ###

def changeColor(arduino, address, r, g, b):
    if arduino.isOpen():
        arduino.flush() 
        package = [address, r, g, b]
        for i in package :
            arduino.write(struct.pack('B',i))
    else :
        print("arduino is closed !")

def resetColor():
    for j in range(10):
        changeColor(arduino, j, 0, 0, 0);
         
        
GPIO.setmode(GPIO.BCM)
switches = [4,17,18,27,22,23,24,5,6,12]

def setupSwitches(switches):
    for switch in switches:
        print(switch)
        GPIO.setup(switch,GPIO.IN)
        
# create a default object, no changes to I2C address or frequency
mh01 = Adafruit_MotorHAT(addr=0x61)
mh23 = Adafruit_MotorHAT(addr=0x62)
mh45 = Adafruit_MotorHAT(addr=0x63)
mh67 = Adafruit_MotorHAT(addr=0x64)
mh89 = Adafruit_MotorHAT(addr=0x65)


motor_hats = [mh01, mh23, mh45, mh67, mh89]
# recommended for auto-disabling motors on shutdown!
def turnOffMotors():    
    for i in range(len(motor_hats)):
        motor_hats[i].getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        motor_hats[i].getMotor(2).run(Adafruit_MotorHAT.RELEASE)    
atexit.register(turnOffMotors)
def turnOffLeds():    
    for address in range(len(switches)):
        changeColor(arduino, address, 0, 0, 0)
        
def getColorHue(percent, roof=100):
    return [roof-int(roof*percent),roof-int(roof*percent),roof]

def moveForwardBy(address, distance, motor_speed=90, color_factor=2):
    mh = motor_hats[int(address/2)]
    m = mh.getStepper(200, int(address%2)+1)  # 200 steps/rev, motor port #1
    m.setSpeed(motor_speed)
    for delta in range(distance):
        factor = delta/50.0
        m.step(5, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
        c = getColorHue(factor, roof=int(255*factor))
        changeColor(arduino, address, c[0],c[1],c[2])
    mh.getMotor(int(address%2)+1).run(Adafruit_MotorHAT.RELEASE)
    
def micromoveForwardBy(address, distance, motor_speed=90, color_factor=2):
    mh = motor_hats[int(address/2)]
    m = mh.getStepper(200, int(address%2)+1)  # 200 steps/rev, motor port #1
    m.setSpeed(motor_speed)
    for value in range(150):
        changeColor(arduino, address, 0, 0, value)
    m.step(distance, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
    mh.getMotor(int(address%2)+1).run(Adafruit_MotorHAT.RELEASE)
    
def reset(address, motor_speed=90):
    mh = motor_hats[int(address/2)]
    m = mh.getStepper(200, int(address%2)+1)  # 200 steps/rev, motor port #1
    m.setSpeed(motor_speed)
    GPIO.setup(switches[address],GPIO.IN)
    changeColor(arduino, address, 150, 0, 0)
    while GPIO.input(switches[address]) == 0:
        m.step(5, Adafruit_MotorHAT.BACKWARD,  Adafruit_MotorHAT.INTERLEAVE)
    mh.getMotor(int(address%2)+1).run(Adafruit_MotorHAT.RELEASE)
    changeColor(arduino, address, 0, 0, 0)

def resetAll():
    for i in range(NUM_EIR):
        reset(i)

def moveAll():
    moveForwardBy(0, 40)
    moveForwardBy(1, 30)
    moveForwardBy(2, 20)
    moveForwardBy(3, 10)
    moveForwardBy(4, 5)
    moveForwardBy(5, 10)
    moveForwardBy(6, 20)
    moveForwardBy(7, 10)
    moveForwardBy(8, 40)
    moveForwardBy(9, 30)

def changeColorFromTo0():
    for address in range(10):
        changeColor(arduino, address, 0, 0, 100)
        
    for address in range(10):
        changeColor(arduino, address, 0, 100, 0)
        time.sleep(0.1)
        changeColor(arduino, address, 0, 0, 100)
    for address in range(10):
        changeColor(arduino, 9-address, 0, 100, 0)
        time.sleep(0.1)
        changeColor(arduino, 9-address, 0, 0, 100)

def changeColorFromTo1():
    for address in range(10):
        changeColor(arduino, address, 0, 0, 50)
        
    for i in range(50):
        for address in range(10):
            changeColor(arduino, address, 0, 0, 49-i)
            
    for i in range(50):
        for address in range(10):
            changeColor(arduino, address, 0, 0, i)
    for i in range(50):
        for address in range(10):
            changeColor(arduino, address, 0, 0, 49-i)
    for i in range(50):
        for address in range(10):
            changeColor(arduino, address, 0, 0, i)
    for i in range(50):
        for address in range(10):
            changeColor(arduino, address, 0, 0, 49-i)
            
def changeColorFromTo1(address):
        changeColor(arduino, address, 0, 0, 50)
        for i in range(50):
            changeColor(arduino, address, 0, 0, 49-i)
        for i in range(50):
            changeColor(arduino, address, 0, 0, i)
        for i in range(50):
            changeColor(arduino, address, 0, 0, 49-i)
        for i in range(50):
            changeColor(arduino, address, 0, 0, i)
        for i in range(50):
            changeColor(arduino, address, 0, 0, 49-i)



    
def dataSet1():
    resetAll()
    moveForwardBy(0, 50)
    moveForwardBy(1, 50)
    moveForwardBy(2, 50)
    moveForwardBy(3, 50)
    moveForwardBy(4, 50)
    moveForwardBy(5, 50)
    moveForwardBy(6, 50)
    moveForwardBy(7, 50)
    moveForwardBy(8, 50)
    moveForwardBy(9, 50)


def dataSet1Color():
    c = getColorHue(0.1, roof=int(255*0.1))
    changeColor(arduino, 0, c[0], c[1], c[2])
    c = getColorHue(0.2, roof=int(255*0.2))
    changeColor(arduino, 1, c[0], c[1], c[2])
    c = getColorHue(0.4, roof=int(255*0.4))
    changeColor(arduino, 2, c[0], c[1], c[2])
    c = getColorHue(0.6, roof=int(255*0.6))
    changeColor(arduino, 3, c[0], c[1], c[2])
    c = getColorHue(0.8, roof=int(255*0.8))
    changeColor(arduino, 4, c[0], c[1], c[2])
    c = getColorHue(1.0, roof=255)
    changeColor(arduino, 5, c[0], c[1], c[2])
    c = getColorHue(0.9, roof=int(255*0.9))
    changeColor(arduino, 6, c[0], c[1], c[2])
    c = getColorHue(0.7, roof=int(255*0.7))
    changeColor(arduino, 7, c[0], c[1], c[2])
    c = getColorHue(0.5, roof=int(255*0.5))
    changeColor(arduino, 8, c[0], c[1], c[2])
    c = getColorHue(0.3, roof=int(255*0.3))
    changeColor(arduino, 9, c[0], c[1], c[2])
    
def animation1():
    for address in range(10):
        changeColor(arduino, address, int(255*address/9), 0, 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, 9-address, 0, int(255*address/9), 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, address, 0, 0, int(255*address/9))
        time.sleep(0.2)
    
    dataSet1Color()    
    time.sleep(60)
    animation1()
    
def dataSet2():
    resetAll()
    moveForwardBy(0, 10)
    moveForwardBy(1, 15)
    moveForwardBy(2, 25)
    moveForwardBy(3, 35)
    moveForwardBy(4, 30)
    moveForwardBy(5, 20)

def dataSet2Color():
    c = getColorHue(0.1, roof=int(255*0.1))
    changeColor(arduino, 0, c[0], c[1], c[2])
    c = getColorHue(0.2, roof=int(255*0.2))
    changeColor(arduino, 1, c[0], c[1], c[2])
    c = getColorHue(0.4, roof=int(255*0.4))
    changeColor(arduino, 2, c[0], c[1], c[2])
    c = getColorHue(0.6, roof=int(255*0.6))
    changeColor(arduino, 3, c[0], c[1], c[2])
    c = getColorHue(0.5, roof=int(255*0.5))
    changeColor(arduino, 4, c[0], c[1], c[2])
    c = getColorHue(0.3, roof=int(255*0.3))
    changeColor(arduino, 5, c[0], c[1], c[2])
    changeColor(arduino, 6, 0,0,0)
    changeColor(arduino, 7, 0,0,0)
    changeColor(arduino, 8, 0,0,0)
    changeColor(arduino, 9, 0,0,0)
    
def animation2():
    for address in range(10):
        changeColor(arduino, address, int(255*address/9), 0, 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, 9-address, 0, int(255*address/9), 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, address, 0, 0, int(255*address/9))
        time.sleep(0.2)
    
    dataSet2Color()    
    time.sleep(60)
    animation2()

  
def dataSet3():
    resetAll()
    moveForwardBy(6, 5)
    moveForwardBy(7, 15)
    moveForwardBy(8, 10)

def dataSet3Color():
    changeColor(arduino, 0, 0,0,0)
    changeColor(arduino, 1, 0,0,0)
    changeColor(arduino, 2, 0,0,0)
    changeColor(arduino, 3, 0,0,0)
    changeColor(arduino, 4, 0,0,0)
    changeColor(arduino, 5, 0,0,0)
    c = getColorHue(0.1, roof=int(255*0.1))
    changeColor(arduino, 6, c[0], c[1], c[2])
    c = getColorHue(0.3, roof=int(255*0.3))
    changeColor(arduino, 7, c[0], c[1], c[2])
    c = getColorHue(0.2, roof=int(255*0.2))
    changeColor(arduino, 8, c[0], c[1], c[2])
    changeColor(arduino, 9, 0,0,0)
    
def animation3():
    for address in range(10):
        changeColor(arduino, address, int(255*address/9), 0, 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, 9-address, 0, int(255*address/9), 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, address, 0, 0, int(255*address/9))
        time.sleep(0.2)
    
    dataSet3Color()    
    time.sleep(60)
    animation3()

def dataSetDemo():
    resetAll()
    moveForwardBy(2, 10)
    moveForwardBy(3, 20)
    moveForwardBy(4, 35)
    moveForwardBy(5, 25)
    moveForwardBy(6, 15)
    
def dataSetDemoColor():
    changeColor(arduino, 0, 0,0,0)
    changeColor(arduino, 1, 0,0,0)
    c = getColorHue(10/50., roof=int(255*(10/50.)))
    changeColor(arduino, 2, c[0], c[1], c[2])
    c = getColorHue(20/50., roof=int(255*(20/50.)))
    changeColor(arduino, 3, c[0], c[1], c[2])
    c = getColorHue(35/50., roof=int(255*(35/50.)))
    changeColor(arduino, 4, c[0], c[1], c[2])
    c = getColorHue(25/50., roof=int(255*(25/50.)))
    changeColor(arduino, 5, c[0], c[1], c[2])
    c = getColorHue(15/50., roof=int(255*(15/50.)))
    changeColor(arduino, 6, c[0], c[1], c[2])
    changeColor(arduino, 7, 0,0,0)
    changeColor(arduino, 8, 0,0,0)
    changeColor(arduino, 9, 0,0,0)
    
def animationDemo():
    for address in range(10):
        changeColor(arduino, address, int(255*address/9), 0, 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, 9-address, 0, int(255*address/9), 0)
        time.sleep(0.2)
    for address in range(10):
        changeColor(arduino, address, 0, 0, int(255*address/9))
        time.sleep(0.2)
    
    dataSetDemoColor()    
    time.sleep(60)
    animationDemo()
    
#resetAll()
turnOffMotors()
turnOffLeds()
    
#dataSetDemo()
#animationDemo()

#dataSet1()
#animation1()
    
#dataSet2()
#animation2()
    
#dataSet3()
#animation3() 
    
#resetColor()
#changeColorFromTo0()
#changeColorFromTo1()
#turnOffLeds()
            
#time.sleep(5)

#micromoveForwardBy(9, 260)

#reset(9)
#moveForwardBy(9,40)
#changeColorFromTo1(9)
#reset(9)
#time.sleep(5)
#          
#turnOffMotors()
#turnOffLeds()  
