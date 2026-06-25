n = int(input("Input: "))
rev = 0

for i in range(len(str(n))):
    rev = rev*10 + n%10
    n = n//10

print("Output:",rev)
    