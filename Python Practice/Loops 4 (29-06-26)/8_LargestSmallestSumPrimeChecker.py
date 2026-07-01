"""
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime

"""
import math

num = int(input("Input:"))

sm = 9
lg = 0

while num>0:
    d = num % 10
    if d > lg:
        lg = d
    if d < sm:
        sm = d
    num = num//10

n = sm + lg
print("Largest =",lg)
print("Smallest =",sm)
print("Sum =",n)

if n <= 1:
    print("Not Prime")
elif n == 2:
    print("Prime")
else:
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            print("Not Prime")
            break
        i = i+1
    else:
        print("Prime")

