n = int(input("Input: "))
count = 0

for i in range(len(str(n))):
    digit = n%10
    
    if digit % 2 != 0 :
         count = count + 1
    
    n = n//10

print("Output: Odd digits count =", count)