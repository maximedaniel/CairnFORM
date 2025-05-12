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

# jeudi 5 septembre 2019 / Biarritz
data = [2.83, 2.11, 1.47, 1.10, 1.13, 1.48, 2.06, 2.72 ,3.28 ,3.61 ,3.66 ,3.44]

# FIRST ANIMATION
stack.push([11,	82,  82,  255, 	168, 	0 * delay, duration, mode])
stack.push([10,	155, 155,  255,	98, 	1 * delay, duration, mode])
stack.push([9, 	219, 219,  255,	36, 	2 * delay, duration, mode])
stack.push([8, 	255, 255,  255,	0, 	    3 * delay, duration, mode])
stack.push([7, 	253, 253,  255,	3, 	    4 * delay, duration, mode])
stack.push([6, 	218, 218,  255,	37, 	5 * delay, duration, mode])
stack.push([5, 	159, 159,  255,	93, 	6 * delay, duration, mode])
stack.push([4, 	93,  93,  255, 	158, 	7 * delay, duration, mode])
stack.push([3,	38,  38,  255, 	212,  	8 * delay, duration, mode])
stack.push([2,	5,   5,  255, 	245, 	9 * delay, duration, mode])
stack.push([1,	0,   0,  255, 	250, 	10 * delay, duration, mode])
stack.push([0,	22,  22,  255, 	228,	11 * delay, duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue

# FIRST ANIMATION
stack.push([11,	0,  0,  0, 	0, 	0 * delay, duration, mode])
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
