from random import *
from driver.StackController import StackController
from driver.Transition import Transition
import json
from pprint import pprint

stack = StackController()
stack.push([0,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([1,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([2,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([3,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
