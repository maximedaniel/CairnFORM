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
delay = 3
duration = 2

stack.push([11,	255, 255,  255, 	0, 		0 * delay, duration, mode])
stack.push([10,	255, 255,  255, 	0, 		1 * delay, duration, mode])
stack.push([9, 	0, 255,  0, 	200, 	2 * delay, duration, mode])
stack.push([8, 	0, 255,  0,		200, 	3 * delay, duration, mode])
stack.push([7, 	0, 255,  0, 	200, 	4 * delay, duration, mode])
stack.push([6, 	0, 255,  0, 	200, 	5 * delay, duration, mode])
stack.push([5, 	0, 255,  0, 	200, 	6 * delay, duration, mode])
stack.push([4, 	0, 255,  0, 	200, 	7 * delay, duration, mode])
stack.push([3,	0, 255,  0, 	200,  	8 * delay, duration, mode])
stack.push([2,	0, 255,  0, 	200, 	9 * delay, duration, mode])
stack.push([1,	0, 255,  0, 	200, 	10 * delay, duration, mode])
stack.push([0,	0, 255,  0, 	200,	11 * delay, duration, mode])


while not stack.isEmpty():
	time.sleep(5)
	continue
	
stack.push([11,	0, 	0,  0, 	0, 	0 * delay,  duration, mode])
stack.push([10, 0, 	0,  0, 	0, 	1 * delay,  duration, mode])
stack.push([9, 	0, 	0,  0, 	0, 	2 * delay,  duration, mode])
stack.push([8, 	0, 	0,  0,	0, 	3 * delay,  duration, mode])
stack.push([7, 	0, 	0,  0, 	0, 	4 * delay, duration, mode])
stack.push([6, 	0, 	0,  0, 	0, 	5 * delay, duration, mode])
stack.push([5, 	0, 	0,  0, 	0, 	6 * delay, duration, mode])
stack.push([4, 	0, 	0,  0, 	0, 	7 * delay, duration, mode])
stack.push([3, 	0, 	0,  0, 	0,  8 * delay, duration, mode])
stack.push([2, 	0, 	0,  0, 	0, 	9 * delay, duration, mode])
stack.push([1,  0, 	0,  0, 	0, 	10 * delay, duration, mode])
stack.push([0,  0,	0,  0, 	0, 	11 * delay, duration, mode])



