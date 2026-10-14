dist = float(input("Enter distance in km: "))
mileage = int(input("Enter the Mileage: "))
petrolPrice = float(input("Enter the Price of Petrol : ₹"))

fuelUsed = dist/mileage

print(f"cost = ₹{round(fuelUsed * petrolPrice ,2)}")