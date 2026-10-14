"""
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime

"""

n= input("Input: ")
m = int(n)

zc = 0
zc = abs(len(str(m))-len(n))

smallest = 9
s = 0

while m>0:
    d = m%10

    if d == 0:
        zc = zc+1
    else:
        s = s + d
    
    if zc>0:
        smallest = 0
    else:
        if d < smallest:
            smallest = d
    m = m//10

total = s + zc
res = smallest * total

print("Zero Count =",zc)
print("Sum =",s)
print("Smallest Digit =",smallest)
print("Final Result =",res)

if res <= 1:
    print("Not Prime")
elif res == 2:
    print("Prime Number")
else:
    i = 2
    while i <= int(math.sqrt(res)):
        if res % i == 0:
            print("Not Prime Number")
            break
        i = i+1
    else:
        print("Prime Number")



















