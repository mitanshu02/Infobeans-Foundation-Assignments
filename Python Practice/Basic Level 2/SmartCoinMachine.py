amount = int(input("Enter the amount: "))

tens = amount//10
rem = amount%10
fives = rem//5

print(f"Amount = ₹{amount}")
print(f"₹10 x {tens}, ₹5 x {fives}")
