# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 16:54:37 2021

@author: Kiran
"""

class Student:
   schoolName = ""
   def __init__(self,studentid,studentname):
      self.studentid = studentid
      self.studentname = studentname

   def setAge(self, age):
      self.age = age
   def displayPropertiesa(self):
      print("name ", self.studentname)
      print("id ", self.studentid)
      print("age ", self.age)
      print("gender ",self.gender)

student = Student(101,'ravi')
student.setAge(12)
student.gender = 'male'

print(student.__dict__)

student1 = Student(102,'rajesh')
student1.setAge(11)
student1.gender = 'male'
print(student1.__dict__)
Student.schoolName = 'abc school'
print(Student.schoolName)