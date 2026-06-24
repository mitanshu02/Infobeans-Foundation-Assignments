distance = int(input("Enter distance: "))
tc = input("Enter class: ").lower()

if distance <= 100:
    if tc == "Sleeper":
        print("Total Fare: ₹100")
    else:
        print("Total Fare: ₹200")
elif 101 <= distance <= 500:
    if tc == "Sleeper":
        print("Total Fare: ₹300")
    else:
        print("Total Fare: ₹600")
else:
    if tc == "Sleeper":
        print("Total Fare: ₹500")
    else:
        print("Total Fare: ₹1000")