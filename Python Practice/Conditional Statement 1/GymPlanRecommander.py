age = int(input("Age = "))
weight = int(input("Weight = "))
goal = input("Goal = ").lower()

if age >= 18:
    if weight >= 80:
        if goal == "weight loss":
            print("Plan = Cardio Plan")
        else:
            print("Plan = Strength Plan")
    else:
        print("Plan = General Fitness Plan")
else:
    print("Not Allowed")