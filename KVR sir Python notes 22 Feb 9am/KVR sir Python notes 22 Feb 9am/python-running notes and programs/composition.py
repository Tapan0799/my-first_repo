# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:27:05 2021

@author: Kiran
"""

class Employee:
    def __init__(self,department,name):
       self.deptName = department.deptName
       self.name = name

    def getEmployeeDetails(self):
        print("employee department ", self.deptName)
        print("employee name", self.name)


class Department:
    def __init__(self,deptname):
       self.deptName = deptname
   
department = Department("software engineering department")
employee = Employee(department,"Ravi kumar")
employee.getEmployeeDetails()