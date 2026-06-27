n = int(input("Input: "))

sum = 0

for i in range(1,n + 1):
    if n%i == 0:
        sum = sum + i
print("Sum =",sum)
        