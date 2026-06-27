n = int(input("Input: "))

count = 0

for i in range(len(str(n))):
    if (n%10)%2 != 0:
        count += 1
    n = n//10

print("Odd Digits Count =",count)