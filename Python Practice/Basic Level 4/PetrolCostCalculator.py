dist = float(input("Distance = ").replace("km",""))
mileage = int(input("Mileage = ").replace("km/litre",""))
petrolPrice = float(input("Petrol price = ").replace("/litre",""))

fuelUsed = dist/mileage

print(f"Petrol Used = {fuelUsed} litres")
print(f"Total cost = {round(fuelUsed * petrolPrice ,1)}")