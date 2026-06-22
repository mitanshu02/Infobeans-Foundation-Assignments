mobilePrice = int(input("Mobile Price = "))
downPayment = int(input("Down Payment = "))
intrestRate = float(input("Intrest rate = "))
months = int(input("Months = "))

remainingAmount = mobilePrice - downPayment
total = remainingAmount + (remainingAmount*(intrestRate/100))

print(f"Remaining Amount = {remainingAmount}")
print(f"Total With Intrest = {int(total)}")
print(f"Monthly EMI = {total/months}")