# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:15:34 2021

@author: Kiran
"""

class A:
    def __init__(self): #construcotr
      print("parent class constructor")
        
    def method1(self): #instance method
       print("parent class instance method")
       
class B(A):
    @classmethod
    def method2(cls):
        super(B,cls).__init__(cls)
        super(B,cls).method1(cls)
        
    @classmethod
    def method1(self): #instance method
       print("parent class instance method")
        
B.method2()
B.method1()
        