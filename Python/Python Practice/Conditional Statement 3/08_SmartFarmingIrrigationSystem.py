SM = int(input("Soil Moisture = "))

if SM <= 30:
    temperature = int(input("Temperature = "))

    if temperature >= 35:
        crop = input("Crop = ").lower()

        if crop == "wheat":
            print("Irrigation = High Water Supply")
        else:
            print("Irrigation = Moderate Supply")
    else:
        print("Irrigation = Moderate Supply")
else:
    if 31 <= SM <= 60:
        rainfall = input("Rainfall = ").lower()

        if rainfall == "yes":
            print("Irrigation = Delay Irrigation")
        else:
            print("Irrigation = Light Irrigation")
    else:
        print("Irrigation = No Irrigation")