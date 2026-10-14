'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''

n = int(input("Input: "))

prod = 1
i=1
while i<=n:
    prod *= i
    i += 2

print("Output:",prod)
     