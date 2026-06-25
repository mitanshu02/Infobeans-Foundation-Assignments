cf,dt = map(int, input("Enter (Current floor, destination): ").split(","))

if cf < dt:
    while cf < dt:
        print(cf,"->", end = " ")
        cf = cf + 1
    print(dt)

elif cf > dt:
    while cf > dt:
        print(cf,"->", end = " ")
        cf = cf - 1
    print(dt)

else:
    print("Already on the same floor")
