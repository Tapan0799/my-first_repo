# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:31:49 2021

@author: Kiran
"""

a = 2
b = 1
b2 = "hello"
try :
    c = a/b 
    
    b1 = a/(b-1)#because of ZeroDivisionError, the control is not moving to the next line
    c2 = a/b2;
    print("b1", b1)
except ZeroDivisionError:
    print("divide by zero error") # this execption will be supressed (remove)
except TypeError:
    print("provide int value")
d = 3
e = 5
f = d+e
print(f)