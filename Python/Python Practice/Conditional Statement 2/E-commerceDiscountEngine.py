amount = int(input("Enter purchase amount: "))

if amount > 5000:
    discount = amount*0.2
elif amount > 2000 and amount <= 5000:
    discount = amount*0.1
else:
    discount = amount*0.05

print(f"Final Amount: ₹",(amount - discount))