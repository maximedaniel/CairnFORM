from random import *
from driver.StackController import StackController
from driver.Transition import Transition
import json
from pprint import pprint

stack = StackController()

mode = 'LINEAR'

## OPEN

t = 0
delay = 2
duration = 1

# FIRST ANIMATION
stack.push([11,	0, 0,  0, 0, 	0 * delay, duration, mode])
stack.push([10,	0, 0,  0, 0, 	0 * delay, duration, mode])
stack.push([9,	0, 66, 0, 	66, 	1 * delay, duration, mode])
stack.push([8, 	0, 150, 0, 	150, 	2 * delay, duration, mode])
stack.push([7, 	0, 186, 0, 	186, 	3 * delay, duration, mode])
stack.push([6, 	0, 227, 0, 	227, 	4 * delay, duration, mode])
stack.push([5, 	0, 247, 0, 	247, 	5 * delay, duration, mode])
stack.push([4, 	0, 250, 0, 	250, 	6 * delay, duration, mode])
stack.push([3, 	0, 239, 0,  239, 	7 * delay, duration, mode])
stack.push([2,	0, 217, 0,  217,  	8 * delay, duration, mode])
stack.push([1,	0, 177, 0,  177, 	9 * delay, duration, mode])
stack.push([0,	0, 116, 0,  116, 	10 * delay, duration, mode])
