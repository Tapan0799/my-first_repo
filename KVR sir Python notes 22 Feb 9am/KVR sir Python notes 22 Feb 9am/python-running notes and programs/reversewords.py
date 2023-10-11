# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 16:58:24 2021

@author: Kiran
"""

input="The sun raises in the east"
subinput = input.split()
temp = []
counter = len(subinput)-1
print(counter)
while counter>=0:
   temp.append(subinput[counter])
   temp.append(' ')
   counter=counter-1
result=''.join(temp)
print(result)