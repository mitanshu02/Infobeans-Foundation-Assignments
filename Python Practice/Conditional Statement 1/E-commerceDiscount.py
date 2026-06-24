cv = int(input("Cart Value = "))
ut = input("User Type (premium/regular) = ").lower()

if cv >= 5000:
    if ut == "premium":
        print(f"Final Amount = {cv - (cv*0.2)}")
    else:
        print(f"Final Amount = {cv - (cv*0.1)}")
else:
    if cv >= 2000:
        print(f"Final Amount = {cv - (cv*0.05)}")
    else:
        print(f"Final Amount = {cv}")
    
