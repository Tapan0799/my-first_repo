# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:08:06 2021

@author: Kiran
"""

class NumberProcessor:
       def __init__(self):
            print("constructor with no args")

       def __init__(self,a):
             print("constructor with one argument")

       def __init__(self, a, b):
                print("constructor with two arguments")

#processor = NumberProcessor()
#processor = NumberProcessor(10)
processor = NumberProcessor(10,20)