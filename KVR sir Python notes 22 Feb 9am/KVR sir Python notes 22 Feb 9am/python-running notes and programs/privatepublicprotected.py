# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 16:14:55 2021

@author: Kiran
"""

class Student:
    schoolname = 'little flower school'
    __course = 'maths'
    
    def getData(self):
        print("course name ",Student.__course)


student = Student()
print(student.schoolname) # public variable or attribute
student.getData()
#print(Student.__course) # private attribute cannot be accessed
                        # outside the class