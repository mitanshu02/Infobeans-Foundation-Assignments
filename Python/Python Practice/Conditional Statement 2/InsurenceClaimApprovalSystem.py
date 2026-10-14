PA = int(input("Policy Age = "))
CA = int(input("Claim Amount = "))
AT = input("Accident Type = ").lower()

if PA >= 2:
    if CA <= 50000:
        if AT == "minor":
            print("Claim Status = Approved")
        else:
            print("Claim Status = Approved with inspection")
    elif 50000 < CA <= 200000:
        if AT == "major":
            print("Claim Status = Approve with investigation")
        else:
            print("Claim Status = Rejected")
    else:
        print("Claim Status = Rejected")
else:
    if AT == "minor":
        print("Claim Status = Rejected")
    else:
        print("Claim Status = Pending Review")

