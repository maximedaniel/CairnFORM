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

## OPEN
stack.push([11, 255,255,255,	0, 	 0 * delay,  duration, mode])
stack.push([10, 255,255,255,	0, 	 1 * delay,  duration, mode])
stack.push([9,  255,255,255,	0, 	 2 * delay,  duration, mode])
stack.push([8,  255,255,255,	250, 3 * delay,  duration, mode])
stack.push([7,  255,255,255, 	187, 4 * delay, duration, mode])
stack.push([6,  255,255,255, 	125, 5 * delay, duration, mode])
stack.push([5, 	255,255,255, 	62,  6 * delay, duration, mode])
stack.push([4, 	255,255,255, 	0,   7 * delay, duration, mode])
stack.push([3, 	0, 0,     0, 	0,   8 * delay, duration, mode])
stack.push([2, 	0, 0,     0, 	0, 	 9 * delay, duration, mode])
stack.push([1,  255,255,255,	250, 10 * delay, duration, mode])
stack.push([0, 	255,255,255,	250, 11 * delay, duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue
	
stack.push([11,   0,  0,  0, 	0,   0,  duration, mode])
stack.push([10, 255,255,255, 	0,   0,  duration, mode])
stack.push([9,  255,255,255, 	0,   0,  duration, mode])
stack.push([8,  255,255,255,	0, 	 0,  duration, mode])
stack.push([7,  255,255,255,	250, 0,  duration, mode])
stack.push([6,  255,255,255, 	187, 0,  duration, mode])
stack.push([5,  255,255,255, 	125, 0,  duration, mode])
stack.push([4, 	255,255,255, 	62,  0,  duration, mode])
stack.push([3, 	255,255,255, 	0,   0,  duration, mode])
stack.push([2, 	0, 0,     0, 	0, 	 0,  duration, mode])
stack.push([1,  255,255,255,	250, 0,  duration, mode])
stack.push([0, 	255,255,255,	250, 0,  duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue
	
stack.push([11,   0,  0,  0, 	0, 	 0,  duration, mode])
stack.push([10,   0,  0,  0, 	0,   0,  duration, mode])
stack.push([9,  255,255,255, 	0,   0,  duration, mode])
stack.push([8,  255,255,255, 	0,   0,  duration, mode])
stack.push([7,  255,255,255,	0, 	 0,  duration, mode])
stack.push([6,  255,255,255,	250, 0,  duration, mode])
stack.push([5,  255,255,255, 	187, 0,  duration, mode])
stack.push([4,  255,255,255, 	125, 0,  duration, mode])
stack.push([3, 	255,255,255, 	62,  0,  duration, mode])
stack.push([2, 	255,255,255, 	0,   0,  duration, mode])
stack.push([1,  255,255,255,	250, 0,  duration, mode])
stack.push([0, 	255,255,255,	250, 0,  duration, mode])


while not stack.isEmpty():
	time.sleep(5)
	continue
	
stack.push([11,   0,  0,  0, 	0,   0,  duration, mode])
stack.push([10, 255,255,255, 	0,   0,  duration, mode])
stack.push([9,  255,255,255, 	0,   0,  duration, mode])
stack.push([8,  255,255,255,	0, 	 0,  duration, mode])
stack.push([7,  255,255,255,	250, 0,  duration, mode])
stack.push([6,  255,255,255, 	187, 0,  duration, mode])
stack.push([5,  255,255,255, 	125, 0,  duration, mode])
stack.push([4, 	255,255,255, 	62,  0,  duration, mode])
stack.push([3, 	255,255,255, 	0,   0,  duration, mode])
stack.push([2, 	0, 0,     0, 	0, 	 0,  duration, mode])
stack.push([1,  255,255,255,	250, 0,  duration, mode])
stack.push([0, 	255,255,255,	250, 0,  duration, mode])

while not stack.isEmpty():
	time.sleep(5)
	continue
	
stack.push([11, 255,255,255,	0, 	 0, duration, mode])
stack.push([10, 255,255,255,	0, 	 0, duration, mode])
stack.push([9,  255,255,255,	0, 	 0, duration, mode])
stack.push([8,  255,255,255,	250, 0, duration, mode])
stack.push([7,  255,255,255, 	187, 0, duration, mode])
stack.push([6,  255,255,255, 	125, 0, duration, mode])
stack.push([5, 	255,255,255, 	62,  0, duration, mode])
stack.push([4, 	255,255,255, 	0,   0, duration, mode])
stack.push([3, 	0, 0,     0, 	0,   0, duration, mode])
stack.push([2, 	0, 0,     0, 	0, 	 0, duration, mode])
stack.push([1,  255,255,255,	250, 0, duration, mode])
stack.push([0, 	255,255,255,	250, 0, duration, mode])

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




