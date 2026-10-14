"""
1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime

"""
import math

n = int(input("Input: "))
m = n
s = 0
rev = 0

while n>0:
    d = n%10
    rev = rev*10 + d
    
    s = s+d
    n = n//10

diff = abs(m - rev)

print("Sum of Digits =",s)
print("Reverse =",rev)
print("Difference =",diff)

s = s + diff
print("Final Result =",s)

if s<=1:
    print("Not Prime")
if s == 2:
    print("Prime Number")
else:
    i = 2
    while i<=int(math.sqrt(s)):
        if s%i == 0:
            print("Not Prime")
            break
        i = i+1
    else:
        print("Prime Number")

 

 
