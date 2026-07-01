"""
6. Composite Number Detector – Risk Version

A product company marks composite numbers as risky.

User enters a number.
System must:

- Check Composite or Not
- Count total factors
- Print smallest factor other than 1

Input:
12

Output:
Composite Number
Factors Count = 6
Smallest Factor = 2

"""

import math

n= int(input("Input: "))
isComposite = False

if n<=1:
    print("Not a composite Number")
else:
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            print("Composite Number")
            isComposite = True
            break
        i = i+1
    else:
        print("Not a Composite Number")
   
if isComposite:
    count = 1
    smallest = 1
    i = 2
    while i<=n:
        if n%i == 0:
            count = count+1
            if count == 2:
                smallest = i
        i = i+1
    print("Factors Count =",count)
    print("Smallest Factor =",smallest)


        
    