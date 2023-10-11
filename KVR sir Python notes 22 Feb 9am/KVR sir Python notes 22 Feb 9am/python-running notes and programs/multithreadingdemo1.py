# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 16:12:48 2021

@author: Kiran
"""
from threading import *
from time import *
class Truck:
    def __init__(self,str):
        self.str = str
        
    def processGoods(self):
        for i in range(1,6):
            print(self.str,":i",i)
            sleep(0.1) #pause for some time between loading and unloading

obj1 = Truck("unloading") 
obj2 = Truck("loading") 

thread1 = Thread(target=obj1.processGoods)#person1 is unloading the good from the truck
thread2 = Thread(target=obj2.processGoods)# person2 is loading the goods into factory

thread1.start() # starts unloading process
thread2.start() # starts loading process