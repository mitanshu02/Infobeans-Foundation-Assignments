n = int(input("Number = "))
digit = int(input("digit = "))

count = 0

while n>0:
    if n%10 == digit:
        count= count + 1
    n = n//10

print(count)