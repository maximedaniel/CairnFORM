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

stack.push([11,	0, 0,  0,	0, 		0 * delay,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	1 * delay,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	2 * delay,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	3 * delay,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	4 * delay, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	5 * delay, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	6 * delay, duration, mode])
stack.push([4, 	0, 0,  0, 	161, 	7 * delay, duration, mode])
stack.push([3, 	0, 0,  0, 	184,  	8 * delay, duration, mode])
stack.push([2, 	0, 0,  0, 	207, 	9 * delay, duration, mode])
stack.push([1,  0, 0,  0, 	230, 	10 * delay, duration, mode])
stack.push([0,  0, 0,  0, 	250, 	11 * delay, duration, mode])

while not stack.isEmpty():
	time.sleep(120);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	0, duration, mode])
stack.push([4, 	0, 0,  0, 	161, 	0, duration, mode])
stack.push([3, 	0, 0,  0, 	184,  	0, duration, mode])
stack.push([2, 	0, 0,  0, 	207, 	0, duration, mode])
stack.push([1,  0, 0,  0, 	230, 	0, duration, mode])
stack.push([0, 255,255, 50,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	0, duration, mode])
stack.push([4, 	0, 0,  0, 	161, 	0, duration, mode])
stack.push([3, 	0, 0,  0, 	184,  	0, duration, mode])
stack.push([2, 	0, 0,  0, 	207, 	0, duration, mode])
stack.push([1,  255,255,50, 	230, 	0, duration, mode])
stack.push([0, 255,255, 50,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	0, duration, mode])
stack.push([4, 	0, 0,  0, 	161, 	0, duration, mode])
stack.push([3, 	0, 0,  0, 	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	0, duration, mode])
stack.push([4, 	0, 0,  0, 	161, 	0, duration, mode])
stack.push([3, 	 255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0, 255, 255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5, 	0, 0,  0, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	 255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0, 255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  0, 0,  0, 	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7, 	0, 0,  0, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	0, 0,  0,	69, 	0,  duration, mode])
stack.push([7,  255,255, 50, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	0, 0,  0, 	46, 	0,  duration, mode])
stack.push([8, 	 255,255, 50,	69, 	0,  duration, mode])
stack.push([7,  255,255, 50, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 0, 0,  0, 	23, 	0,  duration, mode])
stack.push([9, 	255,255, 50, 	46, 	0,  duration, mode])
stack.push([8, 	255,255, 50,	69, 	0,  duration, mode])
stack.push([7,  255,255, 50, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0, 0,  0,	0, 		0,  duration, mode])
stack.push([10, 255,255, 50, 	23, 	0,  duration, mode])
stack.push([9, 	255,255, 50, 	46, 	0,  duration, mode])
stack.push([8, 	255,255, 50,	69, 	0,  duration, mode])
stack.push([7,  255,255, 50, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	255,255, 50,	0, 		0,  duration, mode])
stack.push([10, 255,255, 50, 	23, 	0,  duration, mode])
stack.push([9, 	255,255, 50, 	46, 	0,  duration, mode])
stack.push([8, 	255,255, 50,	69, 	0,  duration, mode])
stack.push([7,  255,255, 50, 	92, 	0, duration, mode])
stack.push([6,  255,255, 50,  	115, 	0, duration, mode])
stack.push([5,  255,255, 50, 	138, 	0, duration, mode])
stack.push([4,  255,255, 50,	161, 	0, duration, mode])
stack.push([3, 	255,255, 50,	184,  	0, duration, mode])
stack.push([2,  255,255, 50, 	207, 	0, duration, mode])
stack.push([1,  255,255, 50, 	230, 	0, duration, mode])
stack.push([0,  255,255, 50,	250, 	0, duration, mode])


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

