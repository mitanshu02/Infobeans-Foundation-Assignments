cp = int(input("Cost Price = "))
sp = int(input("Selling Price = "))

print(f"Profit or Loss = {sp-cp}")
print(f"Profit or Loss Percentage = {round(((sp-cp)/cp)*100,2)}%")