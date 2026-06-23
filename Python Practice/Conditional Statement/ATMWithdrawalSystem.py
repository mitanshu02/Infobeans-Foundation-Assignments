balance = int(input("Balance = "))
withdrawal = int(input("Withdrawal Amount = "))
pin = input("PIN = ").lower()

if balance >= withdrawal:
    if withdrawal <= 10000:
        if pin == "correct":
            print("Transaction Successful")
        else:
            print("Invalid PIN")
    else:
        print("Limit Exceeded")
else:
    print("Insufficient Balance")