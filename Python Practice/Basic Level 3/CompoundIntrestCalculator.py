p = int(input("Principal = "))
r = float(input("Rate = "))
t = int(input("Time = "))

ci = p*(1+(r/100)**t)

print(f"Amount = ₹{round(p+ci)}")
print(f"Compound intrest = ₹{round(ci)}")