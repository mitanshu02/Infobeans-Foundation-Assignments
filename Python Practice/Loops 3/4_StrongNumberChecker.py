"""
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
"""

n = int(input("Input: "))
temp = n
sum = 0
while n>0:
    d = n%10
    fact = 1

    while d>=1:
        fact = fact*d
        d = d-1
    sum = sum + fact
    n = n//10

if sum == temp:
    print("Strong Number")
else:
    print("Not Strong Number")