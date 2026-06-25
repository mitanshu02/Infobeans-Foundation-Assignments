n = int(input("Input: "))

mul = 1

for i in range(len(str(n))):
    mul = mul * (n%10)
    n = n//10

print("Output:", mul)