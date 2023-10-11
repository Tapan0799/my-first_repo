# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:00:48 2021

@author: Kiran
"""

def function(n):
    if n<=2:
         return
    print("*")
    function(n//2)
    function(n//2)
    print("*")

function(20)