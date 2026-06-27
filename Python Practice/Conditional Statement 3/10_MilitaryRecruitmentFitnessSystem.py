age = int(input("Age = "))
BMI = int(input("BMI = "))
RT = int(input("Running Time = "))
medical = input("Medical = ").lower()

if 18 <= age <= 25:
    if 18 <= BMI <= 25:
        if RT <= 15:
            if medical == "fit":
                print("Selection Status = Selected")
            else:
                print("Selection Status = Medical Reject")
        else:
            print("Selection Status = Physical Fail")
    else:
        print("Selection Status = BMI Fail")
elif 26 <= age <= 30:
    if RT <= 14:
        if medical == "fit":
            print("Selection Status = Conditional Selection")
        else:
            print("Selection Status = Rejected")
    else:
        print("Selection Status = Rejected")
else:
    print("Selection Status = Not Eligible")
