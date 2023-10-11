# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:07:14 2021

@author: Kiran
"""

from abc import *
class A:
   @abstractmethod
   def method1(self):
     pass
class B(A):
    def method1(self):
        print("in method1")

a = B()
a.method1()
