"""
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number
"""

n = input("Input a number: ")
l = len(n)
temp = n
d = 1

for i in range(1,l+1):
    if i == l:
        d = int(n)%10
    n = int(n)//10

if '0' in temp and d != 0:
    print("Duck Number")
else:
    print("Not a Duck Number")
