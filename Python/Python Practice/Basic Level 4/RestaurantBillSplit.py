amount = int(input("Enter total bill amount = "))
gst = float(input("GST = "))
ServiceCharge = float(input("Service Charge = "))
friends = int(input("No. of friends = "))

totalPayable  = amount+(amount*(gst/100))+(amount*(ServiceCharge/100))

print(f"Final Bill = {totalPayable}")
print(f"Each Person Pays = {totalPayable/friends}")