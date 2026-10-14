salary = int(input("Salary = "))
cs = int(input("Credit Score = "))
el = int(input("Existing Loans = "))

if salary >= 30000:
    if cs >= 750:
        print("Loan Status = Approve")
    else:
        if el <= 2:
            print("Loan Status = Conditionally approval")
        else:
            print("Loan Status = Rejected")
else:
    print("Loan Status = Rejected")