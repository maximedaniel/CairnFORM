#!/usr/bin/python
import sys
import atexit
import struct
import math
import numpy as np
from Transition import Transition
POSITION_MAX = 450

class Ring:
    
    def __init__(self, address, debug=False):
        self.color = (-1,-1,-1)
        self.pos = -1
        self.debug = debug
        