salary = int(input("Salary = "))
age = int(input("Age = "))
CS = int(input("Credit Score = "))
EMI = int(input("EMI = "))

if salary >= 40000:
    if 21 <= age <= 60:
        if CS >= 750:
            if EMI <= salary * 0.40:
                print("Loan Status = Approved at 8%")
            else:
                print("Loan Status = Approved at 10%")
        else:
            if CS >= 650:
                print("Loan Status = Approved at 12%")
            else:
                print("Loan Status = Rejected")
else:
    if salary >= 25000:
        if CS >= 700:
            print("Loan Status = Approved at 13%")
        else:
            print("Loan Status = Rejected")
    else:
        print("Loan Status = Rejected")