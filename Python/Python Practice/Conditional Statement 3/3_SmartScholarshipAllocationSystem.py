marks = int(input("Marks = "))
income = int(input("Income = "))
category = input("Category = ").lower()

if marks >= 85:
    if income <= 300000:
        if category != "general":
            print("Scholarship = Full Scholarship")
        else:
            print("Scholarship = 75% Scholarship")
    else:
        print("Scholarship = 50% Scholarship")
elif 70 <= marks <= 84:
    if income <= 200000:
        print("Scholarship = 50% Scholarship")
    else:
        print("Scholarship = 25% Scholarship")
else:
    print("No Scholarship")