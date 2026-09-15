"""
Assignment 6: Hospital Management System � Oldest Patient

Write a Python program to identify the oldest patient using the reduce() function with a lambda expression.

Input:
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]

Expected Output:
Oldest Patient: Kiran
"""
from functools import reduce

patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]

oldest = reduce(lambda a,b:a if a[1]>b[1] else b,patients)

print("Oldest Patient:",oldest[0])