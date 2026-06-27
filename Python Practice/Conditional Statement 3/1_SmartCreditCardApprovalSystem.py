income = int(input("Income = "))
CS = int(input("Credit Score = "))
employment = input("Employment = ").lower()
debt = int(input("Debt = "))

if income >= 50000:
    if CS >= 750:
        if debt < 20000:
            print("Card Type = Premium Card")
        else:
            print("Card Type = Gold Card")
    else:
        if employment == "government":
            if CS >= 650:
                print("Card Type = Gold Card")
            else:
                print("Rejected")
        else:
            print("Rejected")
else:
    if income >= 30000:
        if CS >= 700:
            print("Card Type = Silver Card")
        else:
            print("Rejected")
    else:
        print("Rejected")