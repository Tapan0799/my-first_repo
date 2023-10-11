# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:31:42 2021

@author: Kiran
"""

class A:
    x = 25
    def __init__(self):
        self.y = 30
    def method1(self):
        print("in parent class instance method1")
 

    @classmethod
    def method2(cls):
           print("in parent class class method")


    @staticmethod
    def method3():
           print("in parent class static method")

class B(A): # B is extended or derived or inherited from A
     pass   # just do nothing

b = B() # B object
print(b.x)
print(b.y)
b.method1()
b.method2()
b.method3()