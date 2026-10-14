"""
8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7

"""
n = int(input("Input: "))
count = 0
while n>=100:
    n = n-100
    count = count + 1
print("Notes =",count)