n = int(input("Input: "))

smallest = 99999999999999999999999

for i in range(len(str(n))):
    d = n % 10
    if d < smallest:
        smallest = d
    n = n//10

print("Largest Digit =",smallest)