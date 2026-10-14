"""
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors. Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number

"""
import math

n= int(input("Input: "))

if n==1:
    print("Not a composite Number")
else:
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            print("Composite Number")
            break
        i = i+1
    else:
        print("Not a Composite Number")
        
    