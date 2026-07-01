"""
5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3

"""
import math
n = int(input("Input: "))

if n<=1:
    print("Next Prime = 2")
    next_prime = 2
else:
    i = n+1
    while True:
        root = int(math.sqrt(i))
        while root>=2:
            if i % root == 0:
                break
            root = root - 1
        else:
            print("Next Prime ID =",i)
            break
        i = i+1

if n<= 1:
    print("Gap =",2 - n)
else:        
    print("Gap =", i - n)