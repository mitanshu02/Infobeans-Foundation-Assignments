'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''
import math

n= int(input("Input: "))

if n<=1:
    print("Access is denied")
else:
    root = math.sqrt(n)
    while root >= 2:
        if n % root == 0:
            print("Access is denied")
            break
        root -= 1
    else:
        print("Access is granted")