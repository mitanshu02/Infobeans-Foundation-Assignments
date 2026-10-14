n = int(input("Input: "))
temp = n
sum = 0 

for i in range(len(str(n))):
    sum = sum + (n%10)**3
    n = n//10

if sum == temp:
    print("Output: Armstrong")
else:
    print("Output: Not Armstrong")