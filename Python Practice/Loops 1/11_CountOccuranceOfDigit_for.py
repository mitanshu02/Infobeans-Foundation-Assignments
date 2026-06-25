n = int(input("Number = "))
digit = int(input("digit = "))

count = 0

for i in range(len(str(n))):
    if n%10 == digit:
        count= count + 1
    n = n//10

print(count)