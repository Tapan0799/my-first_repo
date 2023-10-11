# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:11:52 2021

@author: Kiran
"""

class NumberProcessor:
      def __init__(self, *a): #This constructor multiple arguments
            print("constructor with variable number of arguments")


processor = NumberProcessor()
processor = NumberProcessor(10)
processor = NumberProcessor(10,20)