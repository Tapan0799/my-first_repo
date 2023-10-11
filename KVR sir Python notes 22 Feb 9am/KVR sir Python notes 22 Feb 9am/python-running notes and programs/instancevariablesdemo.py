# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:30:44 2021

@author: Kiran
"""

class Student:
    def __init__(self,studentid,studentname):
      self.studentid = studentid
      self.studentname = studentname

    def setAge(self, age):
      self.age = age
    def displayProperties(self):
      print("name ", self.studentname)
      print("id ", self.studentid)
      print("age ", self.age)
      print("gender ",self.gender)

student = Student(101,'ravi')
student.setAge(12)
student.gender = 'male'

student1 = Student(102,'rajesh')
student1.setAge(11)
student1.gender = 'male'

print(student.__dict__)
print(student1.__dict__)

student.displayProperties()
student1.displayProperties()

student.age=14
print(student.__dict__)
print(student1.__dict__)