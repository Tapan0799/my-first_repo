# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 16:23:12 2021

@author: Kiran
"""

def function(n):
    if n==0:
       return 1
    print(n)
    function(n-1)
    
function(4)