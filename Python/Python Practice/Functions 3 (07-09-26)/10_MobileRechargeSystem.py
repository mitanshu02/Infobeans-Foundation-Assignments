"""
Assignment 10: Mobile Recharge System

Write a recursive function to determine whether a given number is prime.

Input:
Enter Coupon Number:
29

Output:
Prime Number
"""

n = int(input("Enter Coupon Number: "))

def checkPrime(n,num=2):
    if num == n:
        return True
    else:
        if n%num == 0:
            return False
        else:
            return checkPrime(n,num+1)


if checkPrime(n):
    print("Prime Number")
else:
    print("Not Prime Number")
