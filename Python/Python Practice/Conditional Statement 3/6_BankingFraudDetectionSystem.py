amount = int(input("Amount = "))
location = input("Location = ").lower()
device = input("Device = ").lower()
transactions = int(input("Transactions = "))
UA = input("Unusual Activity = ").lower()

if amount >= 50000:
    if location == "international":
        if device == "new":
            if transactions > 3:
                print("Risk Level = High Risk (Blocked)")
            else:
                print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Medium Risk")
    else:
        if transactions > 5:
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")
else:
    if UA == "yes":
        if device == "new":
            print("Risk Level = Medium Risk")
        else:
            print("Risk Level = Low Risk")
    else:
        print("Risk Level = Safe")