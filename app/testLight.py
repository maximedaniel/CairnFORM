#!/usr/bin/python
from serial import *
import time
import struct

arduino = Serial(port="/dev/ttyACM0", baudrate=9600, timeout=10, writeTimeout=10)
time.sleep(2)

def test(address, r_value, g_value, b_value, duration):
        if arduino.isOpen():
                arduino.flush() 
                package = [address, r_value, g_value, b_value]
                for i in package:
                        arduino.write(struct.pack('B', i))
                else:
                        print("arduino is closed !")
                time.sleep(duration)
                arduino.flush() 
                package = [address, 0, 0, 0]
                for i in package:
                        arduino.write(struct.pack('B', i))
                else:
                        print("arduino is closed !")
                time.sleep(0.2)       
# 0 255 255 255
while True:
	try:
		user_input = raw_input("Enter q to quit or a command <ring[0:11]> <r[0:255]> <g[0:255] <b[0:255]>")
		if user_input == "q":
			break
                
		else:
			user_input = user_input.split()
                        if len(user_input) == 4:
                                address = int(user_input[0])
                                r_value = int(user_input[1])
                                g_value = int(user_input[2])
                                b_value = int(user_input[3])
                                print("valid command: %d %d %d %d" %(address, r_value, g_value, b_value))
                                test(address, r_value, g_value, b_value, 0.2)
                        elif len(user_input) == 1:
                                address = int(user_input[0])
                                print("valid command: %d" %(address))
                                test(address, 255, 255, 255, 10)
                        else:
                                print("Invalid command.")
                                continue
                                
			
	except KeyboardInterrupt:
		break

            

