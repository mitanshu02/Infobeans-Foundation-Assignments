"""
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4

"""

a,b = map(int,input("Input two Nos: ").split(" "))
count = 0

if a<b:
    while a<=b:
        if a%7 == 0:
            count += 1
        a+=1
else:
    while a>=b:
        if a%7 == 0:
            count += 1
        a-=1

print("Count =",count)