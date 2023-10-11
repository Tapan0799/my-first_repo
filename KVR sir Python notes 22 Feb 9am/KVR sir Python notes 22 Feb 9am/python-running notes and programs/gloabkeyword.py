# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:06:56 2021

@author: Kiran
"""

x=20 # global variable
def function1():
    y=15 # this is local variable
    global x
    x=40
    print("function1",x)
    print("function1",y)

def function2():
    print("function2",x)

function1()
function2()