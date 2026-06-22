amount = int(input("Enter the amount : ₹"))

discount = round(amount*0.1)

print(f"Discount = ₹{discount}")
print(f"Final = ₹{round(amount - discount)}")