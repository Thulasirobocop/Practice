# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Emp:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.display_details()
        return None
    def display_details(self):
        print(f"The Name of the Employee is {self.name} \n The age of Employee is {self.age} \n The salary of the Employee is {self.salary}")
        return None
emp1=Emp('Thulasiram',24,25000)
emp2=Emp('Yashwanth', 24, 30000)
"""
emp1.get_emp_details('Thulasiram',24,25000)
emp2.get_emp_details('Yashwanth', 24, 30000)
emp1.display_details()
emp2.display_details()"""