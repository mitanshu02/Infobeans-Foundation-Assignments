p = int(input("Enter the principal amount: "))
r = float(input("Enter the rate of intrest: "))
t = int(input("Enter time in years: "))

SI = (p*r*t)/100

print(f"Principal = ₹{p}")
print(f"Rate = {r}%")
print(f"Time = {t} years")
print(f"Simple Intrest = ₹{SI}")