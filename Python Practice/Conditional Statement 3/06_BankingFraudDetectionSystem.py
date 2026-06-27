TA = int(input("Transaction Amount = "))
location = input("Location = ").lower()

if TA >= 10000:
    if location == "international":
        OTP = input("OTP Verification = ").lower()

        if OTP == "verified":
            print("Transaction Status = Allowed")
        else:
            print("Transaction Status = Blocked")
    else:
        if TA >= 50000:
            AA = int(input("Account Age = "))

            if AA >= 2:
                print("Transaction Status = Allowed")
            else:
                print("Transaction Status = Flagged")
        else:
            print("Transaction Status = Allowed")
else:
    UA = input("Unusual Activity = ").lower()

    if UA == "yes":
        print("Transaction Status = Flagged")
    else:
        print("Transaction Status = Allowed")