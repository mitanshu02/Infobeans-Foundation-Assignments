n = int(input("Input: "))

largest = 0

for i in range(len(str(n))):
    d = n % 10
    if d > largest:
        largest = d
    n = n//10

print("Largest Digit =",largest)