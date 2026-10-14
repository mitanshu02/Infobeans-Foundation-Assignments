"""
5.Number Stability Analyzer


A science lab studies whether digits are in increasing order.


Write a program using for-else loop:


- If every next digit is greater than previous print Stable Number

- Else Unstable Number


Input:

12359


Output:

Stable Number
"""

n = int(input("Input: "))
rev = 0
pd = 10
while n>0:
    d = n%10
    if d>=pd :
        print("Unstable Number")
        break
    n = n//10
    pd = d
else:
    print("Stable Number")
