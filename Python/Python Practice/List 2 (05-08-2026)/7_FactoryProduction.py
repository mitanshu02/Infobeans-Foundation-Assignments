'''
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''
n = [int(x) for x in input("Enter n: ").split()]

for i in range(len(n)):

    j = n[i]
    fact = 1
    while j > 0:
        fact = fact * j
        j -= 1
    n[i] = fact
    
print(n)
print("Sum =",sum(n))
print("Max =",max(n))
c = 0
for ch in n:
    if ch%2 == 0:
        c += 1
print("Even Count =",c)