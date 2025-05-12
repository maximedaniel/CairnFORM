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
	
# OPEN
stack.push([11,	3, 0,  252, 	4, 		0, duration, mode])
stack.push([10, 13, 0,  242, 	13, 	0, duration, mode])
stack.push([9, 	35, 0,  220, 	35, 	0, duration, mode])
stack.push([8, 	76, 0,  179,	74, 	0, duration, mode])
stack.push([7, 	125, 0,  130, 	123, 	0, duration, mode])
stack.push([6,  161, 0,	94, 	158, 	0, duration, mode])
stack.push([5, 	161, 0,	94, 	158, 	0, duration, mode])
stack.push([4, 	125, 0,  130, 	123, 	0, duration, mode])
stack.push([3, 	76, 0,  179, 	74,  	0, duration, mode])
stack.push([2, 	35, 0,  220, 	35, 	0, duration, mode])
stack.push([1,  13, 0,  242, 	13, 	0, duration, mode])
stack.push([0,  3, 0,  252, 	4, 		0, duration, mode])



while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0,0,0,0, 	0, duration, mode])
stack.push([10, 0,0,0,0, 	0, duration, mode])
stack.push([9, 	0,0,0,0, 	0, duration, mode])
stack.push([8, 	0,0,0,0, 	0, duration, mode])
stack.push([7, 	0,0,0,0, 	0, duration, mode])
stack.push([6, 	0,0,0,0, 	0, duration, mode])
stack.push([5, 	0,0,0,0, 	0, duration, mode])
stack.push([4, 	0,0,0,0,    0, duration, mode])
stack.push([3, 	0,0,0,0, 	0, duration, mode])
stack.push([2, 	0,0,0,0, 	0, duration, mode])
stack.push([1, 	0,0,0,0, 	0, duration, mode])
stack.push([0, 	0,0,0,0, 	0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

# SECOND ANIMATION
stack.push([11,	47, 0,  208, 	46,		0, duration, mode])
stack.push([10, 83, 0,  172, 	81, 	0, duration, mode])
stack.push([9, 	129,0,  126, 	126, 	0, duration, mode])
stack.push([8, 	180,0,   75,	176, 	0, duration, mode])
stack.push([7, 	225,0,   30, 	220, 	0, duration, mode])
stack.push([6,  252,0, 	  3, 	246, 	0, duration, mode])
stack.push([5, 	252,0,    3,    246, 	0, duration, mode])
stack.push([4, 	225,0,   30, 	220, 	0, duration, mode])
stack.push([3, 	180,0,   75, 	176,  	0, duration, mode])
stack.push([2, 	129,0,  126, 	126, 	0, duration, mode])
stack.push([1,  83, 0,  172, 	81, 	0, duration, mode])
stack.push([0,  47, 0,  208, 	46,		0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

stack.push([11,	0,0,0,0, 	0, duration, mode])
stack.push([10, 0,0,0,0, 	0, duration, mode])
stack.push([9, 	0,0,0,0, 	0, duration, mode])
stack.push([8, 	0,0,0,0, 	0, duration, mode])
stack.push([7, 	0,0,0,0, 	0, duration, mode])
stack.push([6, 	0,0,0,0, 	0, duration, mode])
stack.push([5, 	0,0,0,0, 	0, duration, mode])
stack.push([4, 	0,0,0,0,    0, duration, mode])
stack.push([3, 	0,0,0,0, 	0, duration, mode])
stack.push([2, 	0,0,0,0, 	0, duration, mode])
stack.push([1, 	0,0,0,0, 	0, duration, mode])
stack.push([0, 	0,0,0,0, 	0, duration, mode])

