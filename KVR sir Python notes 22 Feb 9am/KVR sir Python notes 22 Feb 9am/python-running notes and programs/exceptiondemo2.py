# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:40:16 2021

@author: Kiran
"""

a = 2
b = 0
b2 = 1
try :
    c = a/b 
    b1 = a/b
    c2 = a/b2;
    print("b1", b1)
except ZeroDivisionError:
    print("divide by zero error") # this execption will be supressed (remove)
except TypeError:
    print("provide int value")
finally:
     print("in finally")
d = 3
e = 5
f = d+e
print(f)