"""
2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17

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
            print("Next Prime =",i)
            break
        i = i+1
        