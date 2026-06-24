temperature = int(input("Enter temperature: "))

if temperature < 0:
    print("Weather Condition: Freezing")
elif 0 <= temperature <= 20:
    print("Weather Condition: Cold")
elif 21 <= temperature <= 35:
    print("Weather Condition: Warm")
else:
    print("Weather Condition: Hot")