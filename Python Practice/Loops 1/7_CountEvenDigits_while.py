n = int(input("Input: "))
count = 0

while n>0:
    digit = n%10
    
    if digit % 2 == 0 and digit != 0:
         count = count + 1
    
    n = n//10

print("Output: Even digits count =", count)