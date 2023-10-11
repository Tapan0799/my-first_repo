# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:44:49 2021

@author: Kiran
"""

mynumbers=[0,2,3,13,17,24,32,45,89,90]
oddnumberlist=[]
for mynumber in mynumbers:
   if mynumber%2!=0:
      oddnumberlist.append(mynumber)
print(oddnumberlist)