from random import *
from driver.StackController import StackController
from driver.Transition import Transition
import json
import time
from pprint import pprint

stack = StackController()

mode = 'EASE_IN_OUT_QUINT'

## OPEN

t = 0
delay = 2
duration = 2

# FIRST ANIMATION
stack.push([11,	0, 255,  255,  250, 	0 * delay, duration, mode])
stack.push([10,	71, 255,  255,	 180, 	1 * delay, duration, mode])
stack.push([9, 	170, 255,  255,	 83, 	2 * delay, duration, mode])
stack.push([8, 	241, 255,  255,	 14, 	3 * delay, duration, mode])
stack.push([7, 	255, 255,  255,	 0, 	4 * delay, duration, mode])
stack.push([6, 	227, 255,  255,	27, 	5 * delay, duration, mode])
stack.push([5, 	213, 255,  255,	41, 	6 * delay, duration, mode])
stack.push([4, 	170, 255,  255, 83, 	7 * delay, duration, mode])
stack.push([3,	99, 255,  255, 152,  	8 * delay, duration, mode])
stack.push([2,	28, 255,  255, 222, 	9 * delay, duration, mode])
stack.push([1,	156, 255,  255, 97, 	10 * delay, duration, mode])
stack.push([0,	184, 255,  255, 69,	11 * delay, duration, mode])


while not stack.isEmpty():
	time.sleep(5)
	continue

# FIRST ANIMATION
stack.push([11,	0, 0,  0, 	0, 	0 * delay, duration, mode])
stack.push([10,	0, 0,  0,	0, 	1 * delay, duration, mode])
stack.push([9, 	0, 0,  0,	0, 	2 * delay, duration, mode])
stack.push([8, 	0, 0,  0,	0,  3 * delay, duration, mode])
stack.push([7, 	0, 0,  0,	0,  4 * delay, duration, mode])
stack.push([6, 	0, 0,  0,	0, 	5 * delay, duration, mode])
stack.push([5, 	0, 0,  0,	0, 	6 * delay, duration, mode])
stack.push([4, 	0, 0,  0, 	0, 	7 * delay, duration, mode])
stack.push([3,	0, 0,  0, 	0, 	8 * delay, duration, mode])
stack.push([2,	0, 0,  0,   0, 	9 * delay, duration, mode])
stack.push([1,	0, 0,  0,   0, 	10 * delay, duration, mode])
stack.push([0,	0, 0,  0, 	0,	11 * delay, duration, mode])
