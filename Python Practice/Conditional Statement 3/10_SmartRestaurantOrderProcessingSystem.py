OA = int(input("Order Amount = "))

if OA >= 2000:
    CT = input("Customer Type = ").lower()

    if CT == "vip":
        PM = input("Payment Method = ").lower()

        if PM == "online":
            print("Offer = Free Dessert + 20% Discount")
        else:
            print("Offer = Free Dessert")
    else:
        if OA >= 5000:
            print("Offer = 15% Discount")
        else:
            print("Offer = 10% Discount")
else:
    if 1000 <= OA < 2000:
        CT = input("Customer Type = ").lower()

        if CT == "vip":
            print("Offer = 10% Discount")
        else:
            print("Offer = 5% Discount")
    else:
        print("Offer = No Offer")