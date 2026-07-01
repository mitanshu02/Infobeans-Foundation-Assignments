"""
6.

Next Prime Cabin Number Generator


A luxury hotel gives only prime numbered cabins to VIP guests.


Manager enters the last allotted cabin number.

System must find the next available prime cabin number.


Write a program using loops.


Input:

24


Output:

Next Prime Cabin = 29
"""

import math
n = int(input("Input: "))

if n<=1:
    print("Next Prime = 2")
else:
    i = n+1
    while True:
        root = int(math.sqrt(i))
        while root>=2:
            if i % root == 0:
                break
            root = root - 1
        else:
            print("Next Prime Cabin =",i)
            break
        i = i+1