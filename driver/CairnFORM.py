from driver.Ring import Ring
import threading
import random
from driver.Transition import Transition
from Tkinter import *
from colour import Color
from driver.LightController import LightController
from driver.MotionController import MotionController
import RPi.GPIO as GPIO
import numpy as np

class CairnFORM:
    
    def __init__(self, stackSize, debug=False):
        #self.master = Tk()
        #self.width = 1024
        #self.height = 720
        #self.offset = 5
        #self.h = 20
        #self.w = Canvas(self.master, width=self.width, height=self.height)
        #self.w.pack()
        self.debug = debug
        self.stackSize = stackSize
        self.rings = []
        self.threads = []
        self.rlock = threading.RLock()
        self.lightController = LightController()
        self.motionController = MotionController()
        GPIO.setmode(GPIO.BCM)
        self.switches = [4,17,18,27,22,23,24,5,6,12]
        for address in range(self.stackSize):
            self.rings.append(Ring(address, self, self.debug))
        if self.isUnknow():
            self.reset()

    def isUnknow(self):
        if self.debug:
            print('\t'.join([str(ring.address) for ring in self.rings]))
        for ring in self.rings:
            if ring.isUnknow():
                return True
        return False

    #def display(self):
    #    if self.debug:
    #        self.w.delete('all')
    #        for i, ring in enumerate(self.rings):
    #            color = '#'+''.join(format(x, '02x') for x in ring.light.round().astype(int))
    #            #print("R",i," ", ring.light.round().astype(int))
    #            self.w.create_rectangle(self.width/2 - ring.motion, i*(self.offset+self.h), self.width/2 + ring.motion, i*(self.offset+self.h)+self.h, fill=color, outline=color)
    #        self.master.after(100, self.display)

    def reset(self):
        if not len(self.threads):
            if self.debug:
                print('\t'.join([str(ring.address) for ring in self.rings]))
            for ring in self.rings:
                ring.reset(self.rlock)
            #    t = threading.Thread(target=ring.reset, args=[self.rlock])
            #    self.threads.append(t)
            #    t.start()
            #for t in self.threads:
            #    t.join()
            #self.threads=[]

    def setMorph(self, morphings):
        for morphing in morphings:
            self.rings[morphing[0]].setMorph(morphing[1], morphing[2], morphing[3], morphing[4])

    def morph(self):
        if not len(self.threads):
            for ring in self.rings:
                t = threading.Thread(target=ring.morph, args=[self.rlock])
                self.threads.append(t)
                t.start()
            #if self.debug:
            #    self.master.after(0, self.display) 
            #    self.master.mainloop()
            for t in self.threads:
                t.join()
            self.threads=[]

    def random(self, duration, mode):
        target= []
        start_color = (0,0,0)
        nb = len(self.rings)
        c1 = Color('red')
        c2 = Color('blue')
        colors = list(c1.range_to(c2, nb))
        random.shuffle(colors)
        
        values = [float(random.randint(25,250)) for x in range(nb)]
        max_value = int(max(values))
        for i in range(nb):
            f_c = int(values[i]/max_value * 255)
            target_color = (np.array(colors[i].rgb)*f_c).astype(int)
            animation0 = [i, start_color, 0, 0, Transition.LINEAR]
            target.append(animation0)
            animation0 = [i, target_color, values[i], duration, mode]
            target.append(animation0)
        self.setMorph(target)
        
    def variation(self, color1, duration, values, mode):
        target= []
        start_color = (0,0,0)
        nb = len(self.rings)
        c1 = Color(color1)
        c2 = Color(color1)
        max_value = int(max(values))
        colors = list(c1.range_to(c2, max_value))
        for i in range(nb):
            i_c = max(int(values[i]-1),0)
            f_c = int(values[i]/max_value * 255)
            target_color = (np.array(colors[i_c].rgb)*f_c).astype(int)
            animation0 = [i, start_color, 0, 0, Transition.LINEAR]
            target.append(animation0)
            animation0 = [i, target_color, values[i], duration, mode]
            target.append(animation0)
        self.setMorph(target)
        
##    def sandglass(self, max_value, duration, delay, mode):
##        target= []
##        start_color = (0,0,0)
##        nb = len(self.rings)
##        m_nb = (nb+1)/2.
##        d = (nb+1)%2
##        step_value = max_value/(int(m_nb-1))
##        values = np.linspace(0., max_value, num=int(m_nb)).astype(int)
##        target_color = (Color('yellow').rgb*255).astype(int)
##        for i in range(nb):
##            animation0 = [i, start_color, 0, 0, Transition.LINEAR]
##            target.append(animation0)
##            _i = int(m_nb-(i+1))
##            if _i < 0:
##                animation0 = [i, target_color, values[abs(_i)], duration, mode]
##                target.append(animation0)
##            else:
##                animation0 = [i, start_color, values[abs(_i)], duration, mode]
##                target.append(animation0)
##            animation0 = [i, target_color, values[abs(_i)], (delay * (m_nb - abs(_i)), Transition.LINEAR]
##            target.append(animation0)
##            if _i < 0:
##                animation0 = [i, start_color, values[abs(_i)], delay, mode]
##                target.append(animation0)
##            else:
##                animation0 = [i, target_color, values[abs(_i)], delay, mode]
##                target.append(animation0)
##
##        self.setMorph(target)   

    
    def wave(self, amplitude, color1, color2, duration, delay, direction, mode):
        target= []
        start_color = (0,0,0)
        nb = len(self.rings)
        red = Color(color1)
        blue = Color(color2)
        colors = list(red.range_to(blue, nb))

        if not direction :
            for i in range(nb):
                target_color = (np.array(colors[i].rgb)*255).astype(int)
                animation1 = [i, start_color, 0, delay*i, Transition.LINEAR]
                animation2 = [i, target_color, amplitude, duration, mode]
                animation3 = [i, start_color, 0, duration, mode]
                animation4 = [i, start_color, 0, (delay * (nb-1 - i)), Transition.LINEAR]
                target.append(animation1)
                target.append(animation2)
                target.append(animation3)
                target.append(animation4)

        else:
            for i in range(nb-1, -1, -1):
                target_color = (np.array(colors[nb-1-i].rgb)*255).astype(int)
                animation1 = [i, start_color, 0, delay*(nb-1-i), Transition.LINEAR]
                animation2 = [i, target_color, amplitude, duration, mode]
                animation3 = [i, start_color, 0, duration, mode]
                animation4 = [i, start_color, 0, (delay * i), Transition.LINEAR]
                target.append(animation1)
                target.append(animation2)
                target.append(animation3)
                target.append(animation4)

        self.setMorph(target)

#cf = CairnFORM(10, debug=False)

#cf.wave(100, 'blue', 'lime', 3 ,2, 1, Transition.LINEAR)
#cf.wave(100, 'lime', 'red', 3 ,2, 0, Transition.LINEAR)
#cf.wave(100, 'red', 'lime', 3 ,2, 1, Transition.LINEAR)
#cf.wave(100, 'lime', 'blue', 3 ,2, 0, Transition.LINEAR)
#cf.morph()
#cf.reset()

#cf.wave(100, 'blue', 'lime', 3 ,2, 0, Transition.LINEAR)
#cf.morph()
#time.sleep(2)
#cf.reset()

#values_9h = [0.,50.,100.,150.,200.,250.,225.,175.,125.,75.]
#values_6h = [50.,75.,125.,175., 150.,100.,0.,0.,0.,0.]
#values_3h = [0.,0.,25.,75.,50., 0.,0.,0.,0.,0.]

#cf.variation('blue', 3, values_3h, Transition.LINEAR)
#cf.morph()
#time.sleep(2)
#cf.reset()
#time.sleep(2)
#cf.random(10, Transition.LINEAR)
#cf.morph()
#cf.reset()
#time.sleep(2)
#cf.random(10, Transition.LINEAR)
#cf.morph()
#cf.reset()
#time.sleep(2)
#cf.random(10, Transition.LINEAR)
#cf.morph()
#cf.reset()
#cf.morph()

#cf.reset()
# for v in range(nb):

#     x= v+1
#     i = 0
#     step = int(x/2)
#     if x/2 - step:
#         i = int(nb/2)+step
#     else:
#         i= int(nb/2)-step

#     target_color = (np.array(colors[i].rgb)*255).astype(int)

#     print(i)
#     animation1 = [i, start_color, 0, delay*v, Transition.LINEAR]
#     animation2 = [i, target_color, 50-v*5, duration, Transition.LINEAR]
#     target.append(animation1)
#     target.append(animation2)
# cf.setMorph(target)
# cf.morph()
#for i in range(10):
#    target.append([i, (random.randint(0,255), random.randint(0,255),random.randint(0,255)), random.randint(1,250), random.randint(1,10), 0])

#for i in range(10):
#    target.append([i, (random.randint(0,255), random.randint(0,255),random.randint(0,255)), random.randint(1,250), random.randint(1,10), 0])

#target.append([0, (0,255,0), 250, 5, 2])


#random.shuffle(target)
#cf.setMorph([[2, (0, 0, 255), 0, 6, 0]])
#cf.morph()
#time.sleep(5)
#cf.reset()
