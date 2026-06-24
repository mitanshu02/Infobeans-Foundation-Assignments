units = int(input("Units = "))

if units >= 100:
    if units >= 300:
        print("Usage Category = High usage")
    else:
        if units >= 200:
            print("Usage Category = Moderate usage")
        else:
            print("Usage Category = Normal usage")
else:
    print("Usage Category = Low usage")