from random import *
from driver.StackController import StackController
from driver.Transition import Transition
import json
from pprint import pprint

stack = StackController()
# stack.push([address<0:STACK_SIZE>,  R<0:255>,    G<0:255>,  B<0:255>, POSITION<0:200>, DELAY<0:Inf>, DURATIONDELAY<0:Inf>, TRANSITION<0:Inf>])
stack.push([0,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([1,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([2,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
stack.push([3,  20,    20,  20, 100, 0, 2, 'EASE_IN_OUT_QUINT'])
