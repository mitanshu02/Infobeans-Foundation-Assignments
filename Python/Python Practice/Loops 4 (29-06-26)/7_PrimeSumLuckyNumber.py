"""
7.
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number

"""
import math

num = int(input("Input: "))
n = 0
while num>0:
    n = n + (num%10)
    num = num//10 

print("Sum =",n)


if n <= 1:
    print("Normal Number")
elif n == 2:
    print("Lucky Number")
else:
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            print("Normal Number")
            break
        i = i+1
    else:
        print("Lucky Number")