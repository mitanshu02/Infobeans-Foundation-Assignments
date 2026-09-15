"""
Assignment 5: Student Registration System � Longest Name

Write a Python program to identify the student with the longest name from the list of registered students using the reduce() function along with a lambda expression.

Input:
students = ["Riya", "Christopher", "Aman", "Neha", "Siddharth"]

Expected Output:
Student with the longest name: Christopher
"""
from functools import reduce

students = [x for x in input("Enter names seperated by space: ").split()]

smallest = reduce(lambda x,y:x if len(x)>len(y) else y,students)

print("Student with the longest name:",smallest)