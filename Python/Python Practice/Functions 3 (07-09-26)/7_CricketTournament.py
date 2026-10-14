"""
Assignment 7: Cricket Tournament � Highest Run Scorer

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input:
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]

Expected Output:
Highest Run Scorer: Rohit
"""
from functools import reduce

players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]

highest = reduce(lambda x,y:x if x[1]>y[1] else y,players)

print("Highest Run Scorer:",highest[0])