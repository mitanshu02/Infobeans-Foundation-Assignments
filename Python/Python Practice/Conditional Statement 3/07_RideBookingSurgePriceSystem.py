demand = int(input("Demand = "))
time = input("Time = ").lower()

if demand >= 80:
    if time == "peak":
        distance = int(input("Distance = "))

        if distance >= 10:
            print("Fare Multiplier = 2x Fare")
        else:
            print("Fare Multiplier = 1.5x Fare")
    else:
        if demand >= 90:
            print("Fare Multiplier = 1.8x Fare")
        else:
            print("Fare Multiplier = 1.3x Fare")
else:
    if 50 <= demand < 80:
        if time == "peak":
            print("Fare Multiplier = 1.2x Fare")
        else:
            print("Fare Multiplier = Normal Fare")
    else:
        print("Fare Multiplier = Normal Fare")