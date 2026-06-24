income = int(input("Enter annual income: "))

if income <= 250000:
    payable = 0
elif income > 250000 and income <=500000:
    payable = ((income - 250000)*0.05)
elif income > 500000 and income <=1000000:
    payable = (250000 * 0.05) + ((income - 500000)*0.2)
else:
    payable = (250000 * 0.05) + (500000 * 0.2) + ((income - 1000000)*0.3)

print("Tax Payable: ₹",payable)