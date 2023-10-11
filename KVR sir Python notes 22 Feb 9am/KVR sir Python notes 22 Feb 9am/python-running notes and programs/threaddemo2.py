# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:58:00 2021

@author: Kiran
"""

from threading import *
from time import *
class MyThread(Thread):
    
    def run(self):
        for i in range(5):
            print(i)
            sleep(0.1)

thread1 = MyThread()
thread2 = MyThread()
thread1.start() # this will start the thread and call
                # the run method automatically
thread2.start()
    