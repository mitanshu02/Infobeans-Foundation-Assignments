amount = int(input("Enter bill amount: "))

if amount <= 1000:
    total = amount + (amount * 0.05)
elif 1001 <= amount <= 5000:
    total = amount + (amount * 0.12)

    if amount > 3000:
        total = total + 200
else:
    total = amount + (amount * 0.18)

    if amount > 3000:
        total = total + 200

print("Final Bill Amount: ₹", total)