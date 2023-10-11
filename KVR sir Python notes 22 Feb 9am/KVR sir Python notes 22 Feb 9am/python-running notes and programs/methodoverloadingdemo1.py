# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 17:09:56 2021

@author: Kiran
"""

class NumberProcessor:
     def add(self,a,b):
          c = a+b
          print(c,"obtained from 2 arg addition")

     def add(self,a,b,c):
           d = a+b+c
           print(d,"obtained from 3 arg addition")

processor = NumberProcessor()
#processor.add(2,3)
processor.add(2,3,5)