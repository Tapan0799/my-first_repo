# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 16:17:47 2021

@author: Kiran
"""

#This function will take 
def advanceddivision(divisionofNumbers):
    def innerFunction(number1, number2):
        if(number2==0):
            print("divide by zero")
            return
        else:
            return divisionofNumbers(number1, number2)
    return innerFunction

@advanceddivision # decorator that adds neew functionality to the division
def divisionofNumbers(number1, number2):
      result = number1/number2
      return result

print(divisionofNumbers(4,2))
