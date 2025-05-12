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
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 0, 0, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([1,	0, 0, 0, 	0, 0, duration, mode])
stack.push([0,	255, 0, 0, 63, 0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([1,	0, 0, 0, 	0, 0, duration, mode])
stack.push([0,	0, 0, 255, 63, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 	0, 0, duration, mode])
stack.push([1,	0, 0, 0, 	0, 0, duration, mode])
stack.push([0,	255, 0, 0, 63, 0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 0, 0, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	255, 0, 0, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	255, 0, 0, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 255, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	255, 0, 0, 63, 0, duration, mode])
stack.push([1,	0, 0, 255, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 255, 63, 0, duration, mode])
stack.push([1,	0, 0, 255, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	255, 0, 0, 63, 0, duration, mode])
stack.push([1,	0, 0, 255, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 255, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	255, 0, 0, 125, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 255, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	255, 0, 0, 188, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 0, 0, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	255, 0, 0, 63, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 255, 63, 0, duration, mode])


while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	255, 0, 0, 63, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;
	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 255, 63, 0, duration, mode])

while not stack.isEmpty():
	time.sleep(5);
	continue;

	
stack.push([3, 	0, 0, 0, 0, 0, duration, mode])
stack.push([2, 	0, 0, 0, 0, 0, duration, mode])
stack.push([1,	0, 0, 0, 0, 0, duration, mode])
stack.push([0,	0, 0, 0, 0, 0, duration, mode])
