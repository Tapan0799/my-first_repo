# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:53:55 2021

@author: Kiran
"""

class A:
    def method1(self):
         print("in A")
class B:
     def method2(self):
         print("in B")
class C:
     def method1(self):
         print("in C")

def function1(obj):
     if hasattr(obj,"method1"):
        obj.method1()
     elif hasattr(obj,"method2"):
         obj.method2()

myobjectlist =[A(), B(), C()] # List of objects
for obj in myobjectlist:
       function1(obj)