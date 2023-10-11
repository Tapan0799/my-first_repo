# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:50:55 2021

@author: Kiran
"""
from threading import *
def function1():
    print("hello my name is function1")

for i in range(5):
    t = Thread(target=function1) # the thread calls function1
    t.start() # this will start the thread