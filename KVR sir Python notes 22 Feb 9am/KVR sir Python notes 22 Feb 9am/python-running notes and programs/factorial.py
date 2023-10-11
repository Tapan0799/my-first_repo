# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:21:12 2021

@author: Kiran
"""

def factorial(num):
       result = 1
       while num>=1:
           result = result*num
           num=num-1
       return result
factorialvalue = factorial(7)
print(factorialvalue)