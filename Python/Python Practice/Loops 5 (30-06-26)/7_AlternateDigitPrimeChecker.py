"""
7.

 Alternate Digit Prime Checker


A math lab adds alternate digits from right side.


Write a program to:


- Find sum of alternate digits

- Check whether sum is Prime or Not


Input:

12345


Output:

Alternate Sum = 9

Not Prime
"""
import math

n = int(input("Input: "))

l = len(str(n))
s = 0

if l%2 == 0:
    n = n//10

while n>0:
    d = n%10
    s = s+d
    n = n//100

print("Alternate Sum =",s)

if s <= 1:
    print("Not Prime")
elif s == 2:
    print("Prime Number")
else:
    i = 2
    while i <= int(math.sqrt(s)):
        if s%i == 0:
            print("Not Prime")
            break
        i = i+1
    else:
        print("Prime Number")
    
