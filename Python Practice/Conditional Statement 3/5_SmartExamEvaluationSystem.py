marks = int(input("Marks = "))
attendance = int(input("Attendance = "))
internal = int(input("Internal = "))

if marks >= 40:
    if attendance >= 75:
        if internal >= 20:
            print("Result = Pass")
        else:
            print("Result = Grace Pass")
    else:
        print("Result = Detained")
else:
    if marks >= 35:
        if internal >= 25:
            print("Result = Reappear")
        else:
            print("Result = Fail")
    else:
        print("Result = Fail")