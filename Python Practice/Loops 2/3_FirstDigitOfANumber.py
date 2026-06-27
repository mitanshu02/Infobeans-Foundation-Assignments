n = int(input("Input: "))

l = len(str(n))

for i in range(l):
    if i == l-1:
        print("First Digit =",n%10)
    n = n//10