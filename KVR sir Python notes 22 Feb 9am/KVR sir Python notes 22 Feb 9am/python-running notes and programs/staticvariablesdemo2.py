# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:40:13 2021

@author: Kiran
"""
#write a python program to get the number of objects created
#for this class DataDemo
class DataDemo:
    numberofobjects = 0 # static or class variable
    
    #this is constructor, this gets called when an object
    #of this class is executed
    def __init__(self):
        DataDemo.numberofobjects =  DataDemo.numberofobjects+1
        
    @classmethod
    def printNumberOfObjects(cls):
        print("The number of objects created for DataDemo class ",cls.numberofobjects)
        
    @staticmethod
    def add(x,y):
        c=x+y
        print(c)
        
dataDemo1 = DataDemo() # creating first object

dataDemo2 = DataDemo()  # creating second object

DataDemo.printNumberOfObjects()