# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:33:12 2021

@author: Kiran
"""

class A:
    x = 25 #static or class variable
    def __init__(self):
        self.y = 30 # instance variable
        self.z = 55
        
    def method1(self):
       self.z1 = 47
       
    @staticmethod
    def method3():
         print("in parent class static method")
         
    @classmethod
    def method2(cls):
           print("in parent class class method")
 

class B(A): # B is extended or derived or inherited from A
     k = 15
     def __init__(self):
          self.y = 76
          self.z = 64
          super().__init__() # this class parent class constructor
          
     def method1(self):
       super().method1() # this calls parent class method1
       super().method3()
       super().method2()
      # self.z1 = 57
       #print(super().z1) # gives error
       #print(super().y) # gives error
       #print(super().z) # gives error
       print("in method1 parent class static variable value", super().x)
       print("in method1 parent class instance variable value", self.z1)
      
     @classmethod
     def method2(cls):
         super().method3()
          
     
     
b = B()
print(b.x)
print(b.y)
print(b.z)
b.method1()
b.method2()
print(b.z1)
#print(b.k)
#print(b.m)