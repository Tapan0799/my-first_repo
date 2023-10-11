# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 16:44:28 2021

@author: Kiran
"""

mylist = list(range(1,100))
evennumberlist = []
counter=0
for x in mylist:
   if x%2==0:
      counter=counter+1
      if(counter<=10):
        evennumberlist.append(x)
      else:
        break
print(evennumberlist)