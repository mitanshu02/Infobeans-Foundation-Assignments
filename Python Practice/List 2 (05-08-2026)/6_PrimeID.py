'''
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''
import math
n = [int(x) for x in input("Enter n: ").split()]

for x in n[:]:
    for i in (2,math.sqrt(x)):
        if x%i == 0:
            n.remove(x)
            break
print("Prime IDs = ",n)
print("Sum = ",sum(n))
print("Max = ",max(n)) if n else print("Max = ",-1)
print("Count =",len(n))
