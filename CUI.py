#rom colorama import init, Style
#from termcolor import colored
import os
import time
import threading
import numpy as np


class CUI:

    def __init__(self, stack):
        self.stack = stack
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        small = 1
        medium = 5
        large = 15
        offset = 5
        large_offset = large - offset
        while(True):
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\033[1;37;40m {0: <{width}}'.format(' ', width=small) + 
                  '\033[1;37;40m {0: <{width}}'.format('QUEUE', width=medium) +
                  '\033[1;37;40m {0: <{width}}'.format('DELAY', width=large) +
                  '\033[1;37;40m {0: <{width}}'.format('DURATION', width=large) +
                  '\033[1;37;40m {0: <{width}}'.format('RED', width=large) +
                  '\033[1;37;40m {0: <{width}}'.format('GREEN', width=large) +
                  '\033[1;37;40m {0: <{width}}'.format('BLUE', width=large) +
                  '\033[1;37;40m {0: <{width}}'.format('DIAMETER', width=large))
            for ring in self.stack.rings:
                m_thread = '\033[1;37;40m {0: <{width}}'.format('\u221E', width=small) if ring.thread.isAlive() else '{0: <{width}}'.format(' ', width=small)
                m_queue = '\033[1;37;40m {0: <{width}}'.format(len(ring.instructions) * u'\u2588', width=medium)
                m_delay = '\033[1;37;40m {0: <{width}}'.format(int(np.round(ring.delay_completion / 100 * large_offset)) * u'\u2588' + str(ring.delay_completion), width=large)
                m_duration =  '\033[1;37;40m {0: <{width}}'.format(int(np.round(ring.duration_completion/100 * large_offset)) * u'\u2588' + str(ring.duration_completion), width=large)
                m_red = '\033[1;31;40m {0: <{width}}'.format(int(np.round(ring.s[0]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[0])), width=large)
                m_green = '\033[1;32;40m {0: <{width}}'.format(int(np.round(ring.s[1]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[1])), width=large)
                m_blue = '\033[1;34;40m {0: <{width}}'.format(int(np.round(ring.s[2]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[2])), width=large)
                m_diameter = '\033[1;36;40m {0: <{width}}'.format(int(np.round(ring.s[3]/100 * large_offset)) * u'\u2588' + str(np.round(ring.s[3])), width=large)
                print(m_thread + m_queue + m_delay + m_duration + m_red + m_green + m_blue + m_diameter)
                
            #print(Style.BRIGHT,
                  #'{0: <{width}}'.format(' ', width=small),
                  #'{0: <{width}}'.format('QUEUE', width=medium),
                  #'{0: <{width}}'.format('DELAY', width=large),
                  #'{0: <{width}}'.format('DURATION', width=large),
                  #'{0: <{width}}'.format('RED', width=large),
                  #'{0: <{width}}'.format('GREEN', width=large),
                  #'{0: <{width}}'.format('BLUE', width=large),
                  #'{0: <{width}}'.format('DIAMETER', width=large))
            #for ring in self.stack.rings:
                #m_thread = '{0: <{width}}'.format('\u221E', width=small) if ring.thread.isAlive() else '{0: <{width}}'.format(' ', width=small)
                #m_queue = colored('{0: <{width}}'.format(len(ring.instructions) * u'\u2588', width=medium), 'white')
                #m_delay = colored('{0: <{width}}'.format(int(np.round(ring.delay_completion / 100 * large_offset)) * u'\u2588' + str(ring.delay_completion), width=large), 'white')
                #m_duration =  colored('{0: <{width}}'.format(int(np.round(ring.duration_completion/100 * large_offset)) * u'\u2588' + str(ring.duration_completion), width=large), 'white')
                #m_red = colored('{0: <{width}}'.format(int(np.round(ring.s[0]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[0])), width=large), 'red')
                #m_green = colored('{0: <{width}}'.format(int(np.round(ring.s[1]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[1])), width=large), 'green')
                #m_blue = colored('{0: <{width}}'.format(int(np.round(ring.s[2]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[2])), width=large), 'blue')
                #m_diameter =colored('{0: <{width}}'.format(int(np.round(ring.s[3]/100 * large_offset)) * u'\u2588' + str(np.round(ring.s[3])), width=large), 'magenta')
                #print(Style.RESET_ALL, m_thread, m_queue, m_delay, m_duration, m_red, m_green, m_blue, m_diameter)
