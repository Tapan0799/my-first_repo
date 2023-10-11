# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:43:52 2021

@author: Kiran
"""

#global variable
x=20
def function1():
    global x
    y=100
    x=40 #modifying the global variable
    print(x)
    print(y)
def function2():
      print(x)

def function3():
    x=55 # local variable
    print(x)
    print(globals()['x'])

#function1()
#function2()
function3()