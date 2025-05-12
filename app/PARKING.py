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
stack.push([5,	12, 243,  0, 	237, 	0 * delay, duration, mode])
stack.push([4, 66, 189,  0,		185, 	1 * delay, duration, mode])
stack.push([3, 	107, 148, 0,	145,    2 * delay, duration, mode])
stack.push([2, 	148, 107, 0,	105, 	3 * delay, duration, mode])
stack.push([1,	207,  48, 0, 	47,  	4 * delay, duration, mode])
stack.push([0,	237,  17, 0, 	17, 	5 * delay, duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue

# FIRST ANIMATION
stack.push([5,	0,  0,  0, 	0, 	0 * delay, duration, mode])
stack.push([4,	0, 0,  0,	0, 	1 * delay, duration, mode])
stack.push([3, 	0, 0,  0,	0, 	2 * delay, duration, mode])
stack.push([2, 	0, 0,  0,	0,  3 * delay, duration, mode])
stack.push([1, 	0, 0,  0,	0,  4 * delay, duration, mode])
stack.push([0, 	0, 0,  0,	0, 	5 * delay, duration, mode])
