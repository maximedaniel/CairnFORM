from random import *
from driver.StackController import StackController
from driver.Transition import Transition
import json
import time
from pprint import pprint

stack = StackController()

mode = 'EASE_IN_OUT_QUINT'


t = 0
delay = 2
duration = 2

# OPEN
stack.push([8, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([7, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([6, 	0, 	255,  0, 	255, 0, duration, mode])
stack.push([5, 	0, 	255,  0, 	255, 0, duration, mode])
stack.push([4, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([3, 	0, 	255,  0, 	0, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

## VALIDATE
stack.push([8, 	255, 	255,  255, 	0, 0, duration, mode])
stack.push([7, 	255, 	255,  255, 	0, 0, duration, mode])
stack.push([6, 	255, 	255,  255, 	255, 0, duration, mode])
stack.push([5, 	255, 	255,  255, 	255, 0, duration, mode])
stack.push([4, 	255, 	255,  255, 	0, 0, duration, mode])
stack.push([3, 	255, 	255,  255, 	0, 0, duration, mode])
stack.push([8, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([7, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([6, 	0, 	255,  0, 	255, 0, duration, mode])
stack.push([5, 	0, 	255,  0, 	255, 0, duration, mode])
stack.push([4, 	0, 	255,  0, 	0, 0, duration, mode])
stack.push([3, 	0, 	255,  0, 	0, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue

# CLOSE
stack.push([8, 	0, 	0,  0, 	0, 0, duration, mode])
stack.push([7, 	0, 	0,  0, 	0, 0, duration, mode])
stack.push([6, 	0, 	0,  0, 	0, 0, duration, mode])
stack.push([5, 	0, 	0,  0, 	0, 0, duration, mode])
stack.push([4, 	0, 	0,  0, 	0, 0, duration, mode])
stack.push([3, 	0, 	0,  0, 	0, 0, duration, mode])



