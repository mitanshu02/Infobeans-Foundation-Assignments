n = int(input("Input: "))

smallest = 9

for i in range(len(str(n))):
    d = n % 10
    if d < smallest:
        smallest = d
    n = n//10

print("Largest Digit =",smallest)