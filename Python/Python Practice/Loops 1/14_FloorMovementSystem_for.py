cf,dt = map(int, input("Enter (Current floor, destination): ").split(","))

if cf < dt:
    for i in range(cf,dt):
        print(i,"->", end = " ")
    print(dt)

elif cf > dt:
    for i in range(cf,dt,-1):
        print(i,"->", end = " ")
    print(dt)

else:
    print("Already on the same floor")

