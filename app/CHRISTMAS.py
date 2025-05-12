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

stack.push([11,	9,82,40,	0, 		0 * delay,  duration, mode])
stack.push([10, 9,82,40, 	23, 	1 * delay,  duration, mode])
stack.push([9, 	9,82,40, 	46, 	2 * delay,  duration, mode])
stack.push([8, 	9,82,40,	69, 	3 * delay,  duration, mode])
stack.push([7,  9,82,40, 	92, 	4 * delay, duration, mode])
stack.push([6,  9,82,40,  	115, 	5 * delay, duration, mode])
stack.push([5,  9,82,40, 	138, 	6 * delay, duration, mode])
stack.push([4,  9,82,40,	161, 	7 * delay, duration, mode])
stack.push([3, 	9,82,40,	184,  	8 * delay, duration, mode])
stack.push([2,  9,82,40, 	207, 	9 * delay, duration, mode])
stack.push([1,  9,82,40, 	230, 	10 * delay, duration, mode])
stack.push([0,  9,82,40,	250, 	11 * delay, duration, mode])


while not stack.isEmpty():
	time.sleep(180);
	continue;

stack.push([11,	9,255,40,	0, 		0,  duration, mode])
stack.push([10, 9,255,40, 	23, 	0,  duration, mode])
stack.push([9, 	9,255,40, 	46, 	0,  duration, mode])
stack.push([8, 	9,255,40,	69, 	0,  duration, mode])
stack.push([7,  9,255,40, 	92, 	0, duration, mode])
stack.push([6,  9,255,40,  	115, 	0, duration, mode])
stack.push([5,  9,255,40, 	138, 	0,  duration, mode])
stack.push([4,  9,255,40,	161, 	0, duration, mode])
stack.push([3, 	9,255,40,	184,  	0, duration, mode])
stack.push([2,  9,255,40, 	207, 	0, duration, mode])
stack.push([1,  9,255,40, 	230, 	0, duration, mode])
stack.push([0,  9,255,40,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([11,	9,82,40,	0, 		0,  duration, mode])
stack.push([10, 9,82,40, 	23, 	0,  duration, mode])
stack.push([9, 	9,82,40, 	46, 	0,  duration, mode])
stack.push([8, 	9,82,40,	69, 	0,  duration, mode])
stack.push([7,  9,82,40, 	92, 	0, duration, mode])
stack.push([6,  9,82,40,  	115, 	0, duration, mode])
stack.push([5,  9,82,40, 	138, 	0, duration, mode])
stack.push([4,  9,82,40,	161, 	0, duration, mode])
stack.push([3, 	9,82,40,	184,  	0, duration, mode])
stack.push([2,  9,82,40, 	207, 	0, duration, mode])
stack.push([1,  9,82,40, 	230, 	0, duration, mode])
stack.push([0,  9,82,40,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(90);
	continue;

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

