balance = int(input("Enter account balance: "))

if balance < 1000:
    print("Withdrawal not allowed")
elif 1000 <= balance <= 5000:
    print("Maximum Withdrawal Limit: ₹1000")
else:
    print("Maximum Withdrawal Limit: ₹5000")