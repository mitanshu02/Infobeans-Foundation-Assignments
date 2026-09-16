"""
Assignment 1: Student Result Calculator

A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

- Student name
- Roll number
- Marks in English
- Marks in Mathematics
- Marks in Science

Create the following methods:

calculate_total() � Calculate the total marks.

calculate_percentage() � Calculate the percentage.

display_result() � Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
"""
class Student:
    def __init__(self,name,roll,english,maths,science):
        self.name = name
        self.roll = roll
        self.eng = english
        self.math = maths
        self.sci = science

    def calculate_total(self):
        self.total = self.eng + self.math + self.sci
        return self.total

    def calculate_percentage(self):
        self.percentage = self.total/3
        return round(self.percentage,2)

    def display_result(self):
        print("Student Name: ",self.name)
        print("Roll Number : ",self.roll)
        print("Total Marks : ",self.total)
        print(f"Percemtage  : {self.percentage:.2f}%")


s = Student("ajay",101,99,87,67)

print(s.calculate_total())
print(s.calculate_percentage())
s.display_result()
