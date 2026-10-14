p = int(input("Principal = "))
r = float(input("Rate = ").replace("%",""))
t = int(input("Time = ").replace("years",""))

ci = p * (1 + r/100) ** t
print(f"Amount After Intrest = {ci}")
