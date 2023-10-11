# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:20:54 2021

@author: Kiran
"""

class DataDemo:
    def method1(self):
        x=200 #local variable
        print(x)
    def method2(self):
        y=300 # local variable
        print(y)
    def sum(self, n):
        total = 0
        for i in range(1,n+1):
            total = total+i
        print("sum",total)

dataDemo = DataDemo()
dataDemo.sum(10)
dataDemo.method1()
dataDemo.method2()