"""
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime

"""

n= int(input("Input: "))
EC = 0
OC = 0
for i in range(len(str(n))):
    d = n%10
    if d%2 == 0:
        EC += 1
    elif d%2 != 0:
        OC += 1
    else:
        continue
    n = n//10

diff = abs(EC - OC)
print("Even Count =",EC)
print("Odd Count =",OC)
print("Difference =",diff)

if diff <= 1:
    print("Not Prime")
elif diff == 2:
    print("Prime Number")
else:
    i = 2
    while i <= int(math.sqrt(diff)):
        if diff % i == 0:
            print("Not Prime Number")
            break
        i = i+1
    else:
        print("Prime Number")
  