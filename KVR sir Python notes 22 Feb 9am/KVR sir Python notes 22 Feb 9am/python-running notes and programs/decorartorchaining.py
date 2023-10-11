# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:39:22 2021

@author: Kiran
"""
def add(func):
    def innerFunction():
        x = func()
        return x+x
    return innerFunction

def multiply(func):
    def innerFunction():
        x = func()
        return x*x
    return innerFunction

#@add #outer will work -- as x is 400 , the result is 800
#@multiply #first this will work -- x = 400

@multiply
@add
def myfunction1():
    return 20

print(myfunction1())