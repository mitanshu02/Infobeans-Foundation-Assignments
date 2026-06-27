n = int(input("Input: "))

square = n**2
sum = 0

for i in range(len(str(square))):
    sum = sum + square%10
    square = square//10

if sum == n:
    print("Glowing Success! You've found the Neon Number")
else:    
    print("Try again! Not quite glowing yet")
