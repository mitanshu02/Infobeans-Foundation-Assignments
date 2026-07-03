'''
2.
Perfect Number Analyzer

A mathematics research system analyzes special numbers within a given range.
The user enters a starting number and ending number.
The system checks every number in that range and displays all Perfect Numbers using nested loops.

(A Perfect Number is a number whose sum of proper divisors is equal to the number itself.)

Input:
Enter starting number: 1
Enter ending number: 1000

Output:
Perfect Numbers are:
6
28
496

'''

s = int(input("Enter starting number:"))
e = int(input("Enter ending number:"))

print("Perfect Numbers are:")

while s<=e:
    total = 0
    i = 1
    while i <= s//2:
        if s%i == 0:
            total = total + i
        i = i+1
    if total == s:
        print(s)
    s = s+1
    