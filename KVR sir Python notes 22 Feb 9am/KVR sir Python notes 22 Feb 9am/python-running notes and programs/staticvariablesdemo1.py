# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:59:07 2021

@author: Kiran
"""

class DataDemo:
    a = 20 # static variable
    def __init__(self):
        self.b = 30 # instance variable
        DataDemo.c = 100 # static variable
        print(self.a)
        print(DataDemo.a) 
        
    def setData(self):
         DataDemo.d = 150 # static variable
         print(self.a)
         print(DataDemo.a) 
         
    @classmethod # class method
    def method1(cls):
        cls.e = 100 # static variable
        DataDemo.f = 120 # static variable
        print(cls.a)
        print(DataDemo.a) 
        
    @staticmethod
    def method2():
        DataDemo.g = 35 # static variable
        print(DataDemo.a) 
        

data1 = DataDemo()
data2 = DataDemo()

print("data1 before :", data1.a,data1.b)
print("data2 before :", data2.a,data2.b)

DataDemo.a = 200
data1.a = 250
data1.b = 150
print("data1 after :", data1.a,data1.b)
print("data2 after :", data2.a,data2.b)
