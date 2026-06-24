salary = int(input("Salary = "))
CS = int(input("Credit Score = "))
EL = int(input("Existing Loans = "))

if salary >= 30000:
    if CS >= 750:
        if EL == 0:
            print("Risk Level = Low Risk")
        elif 0 < EL <= 2:
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = High Risk")
    else:
        if salary >= 50000:
            if CS >= 650:
                print("Risk Level = Medium Risk")
            else:
                print("Risk Level = High Risk")
else:
    print("Not Eligible")