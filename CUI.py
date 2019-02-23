from colorama import init, Style
from termcolor import colored
import os
import time
import threading
import numpy as np

init()


class CUI:

    def __init__(self, stack):
        self.stack = stack
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        small = 1
        large = 15
        offset = 5
        large_offset = large - offset
        while(True):
            time.sleep(1)
            os.system('cls')
            print(Style.BRIGHT,
                  '{0: <{width}}'.format(' ', width=small),
                  '{0: <{width}}'.format('DELAY', width=large),
                  '{0: <{width}}'.format('DURATION', width=large),
                  '{0: <{width}}'.format('RED', width=large),
                  '{0: <{width}}'.format('GREEN', width=large),
                  '{0: <{width}}'.format('BLUE', width=large),
                  '{0: <{width}}'.format('DIAMETER', width=large))
            for ring in self.stack.rings:
                m_t = '{0: <{width}}'.format('\u221E', width=small) if ring.alive else '{0: <{width}}'.format(' ', width=small)
                m_delay = colored('{0: <{width}}'.format(int(np.round(ring.delay_completion / 100 * large_offset)) * u'\u2588' + str(ring.delay_completion), width=large), 'white')
                m_duration =  colored('{0: <{width}}'.format(int(np.round(ring.duration_completion/100 * large_offset)) * u'\u2588' + str(ring.duration_completion), width=large), 'white')
                m_red = colored('{0: <{width}}'.format(int(np.round(ring.s[0]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[0])), width=large), 'red')
                m_green = colored('{0: <{width}}'.format(int(np.round(ring.s[1]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[1])), width=large), 'green')
                m_blue = colored('{0: <{width}}'.format(int(np.round(ring.s[2]/255 * large_offset)) * u'\u2588' + str(np.round(ring.s[2])), width=large), 'blue')
                m_diameter =colored('{0: <{width}}'.format(int(np.round(ring.s[3]/100 * large_offset)) * u'\u2588' + str(np.round(ring.s[3])), width=large), 'magenta')
                print(Style.RESET_ALL, m_t, m_delay, m_duration, m_red, m_green, m_blue, m_diameter)
