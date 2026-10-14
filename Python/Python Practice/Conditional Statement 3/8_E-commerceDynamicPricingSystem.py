demand = int(input("Demand = "))
stock = int(input("Stock = "))
UT = input("User Type = ").lower()
festival = input("Festival = ").lower()

if demand >= 80:
    if stock < 50:
        if UT == "premium":
            if festival == "yes":
                print("Discount = 20%")
            else:
                print("Discount = 10%")
        else:
            print("Discount = No Discount")
    else:
        print("Discount = 5%")
elif 40 <= demand <= 79:
    if festival == "yes":
        print("Discount = 10%")
    else:
        print("Discount = No Discount")
else:
    if stock > 200:
        print("Discount = 15%")
    else:
        print("Discount = No Discount")