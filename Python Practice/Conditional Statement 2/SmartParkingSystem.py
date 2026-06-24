vehicle = input("Enter vehicle type: ")
hours = int(input("Enter hours parked: "))

if vehicle == "Bike":
    total = hours * 10
elif vehicle == "Car":
    total = hours * 20
else:
    total = hours * 50

if hours > 5:
    total = total + 100

print("Total Parking Fee: ₹", total)