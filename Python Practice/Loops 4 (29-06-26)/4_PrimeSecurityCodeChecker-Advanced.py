"""
4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
"""

import math

n = int(input("Input: "))
isPrime = False
if n == 0:
    print("Not a Prime Number \n No Previous Prime Number Exists")
elif n == 1:
    print("Not a Prime Number \n No Previous Prime Number Exists")
elif n == 2:
    print("Prime Number")
    isPrime = True 
else:
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            print("Not a Prime Number")
            break
        i = i+1
    else:
        isPrime = True
        print("Prime Number")
if n >= 2:
    if isPrime:
    
        i = n+1
        while True:
            root = int(math.sqrt(i))
            while root>=2:
                if i % root == 0:
                    break
                root = root - 1
            else:
                print("Next Prime =",i)
                break
            i = i+1

    else:
        i = n-1
        while True:
            root = int(math.sqrt(i))
            while root>=2:
                if i % root == 0:
                    break
                root = root - 1
            else:
                print("Previous Prime =",i)
                break
            i = i-1
