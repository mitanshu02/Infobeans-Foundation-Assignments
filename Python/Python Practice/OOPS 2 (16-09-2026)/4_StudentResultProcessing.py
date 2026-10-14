"""
Question 4: Student Result Processing System

Scenario:
A college wants to automate result generation by calculating total marks, percentage, and grade.

Requirements:
Create a class named Student with:
- roll_number
- student_name
- marks1
- marks2
- marks3

Initialize the values using a constructor.

Calculations:
Total = Marks1 + Marks2 + Marks3
Percentage = Total / 3

Grade Criteria:
90 and above: A
75 to 89: B
60 to 74: C
Below 60: D

Sample Input:
Enter Roll Number : 101
Enter Student Name : Priya Sharma
Enter Marks in Subject 1 : 85
Enter Marks in Subject 2 : 90
Enter Marks in Subject 3 : 88

Sample Output:
------ Student Result ------
Roll Number      : 101
Student Name     : Priya Sharma
Total Marks      : 263
Percentage       : 87.67
Grade            : B
"""

class Student:

    def __init__(self, roll_number, student_name, marks1, marks2, marks3):
        self.roll_number = roll_number
        self.student_name = student_name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def calculate_total(self):
        return self.marks1 + self.marks2 + self.marks3

    def calculate_percentage(self):
        return self.calculate_total() / 3

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A"
        elif percentage >= 75:
            return "B"
        elif percentage >= 60:
            return "C"
        else:
            return "D"

    def display_result(self):
        print("------ Student Result ------")
        print("Roll Number      :", self.roll_number)
        print("Student Name     :", self.student_name)
        print("Total Marks      :", self.calculate_total())
        print("Percentage       :", round(self.calculate_percentage(), 2))
        print("Grade            :", self.calculate_grade())


roll_number = int(input("Enter Roll Number : "))
student_name = input("Enter Student Name : ")
marks1 = float(input("Enter Marks in Subject 1 : "))
marks2 = float(input("Enter Marks in Subject 2 : "))
marks3 = float(input("Enter Marks in Subject 3 : "))

student = Student(roll_number, student_name, marks1, marks2, marks3)

student.display_result()
