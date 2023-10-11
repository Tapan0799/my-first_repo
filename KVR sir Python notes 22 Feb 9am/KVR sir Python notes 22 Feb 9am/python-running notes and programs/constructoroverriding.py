# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:19:37 2021

@author: Kiran
"""

class A:
   def __init__(self):
       print("in parent class constructor")

class B(A):
    def __init__(self):
        super().__init__() # this will invoke the parent class constructor
       print("in child  class constructor")
      

b = B()