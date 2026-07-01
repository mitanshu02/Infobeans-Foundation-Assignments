"""
2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime

"""

import math

n = int(input("Input: "))
m = n
s = 0
mul = 1

while n>0:
    d = n%10
    mul = mul*d
    s = s+d
    n = n//10

diff = abs(mul - s)

difference = str(diff)
digits = len(str(difference))

res = diff + digits
print("Sum =",s)
print("Product =",mul)
print("Difference =",diff)
print("Digits =",digits)
print("Final Result =",res)

if res<=1:
    print("Not Prime")
if res == 2:
    print("Prime Number")
else:
    i = 2
    while i<=int(math.sqrt(res)):
        if res%i == 0:
            print("Not Prime")
            break
        i = i+1
    else:
        print("Prime Number")


