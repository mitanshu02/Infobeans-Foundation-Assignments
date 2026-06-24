attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Status: Eligible")
elif 60 <= attendance <= 74:
    print("Status: Eligible with Warning")
else:
    print("Status: Not Eligible")