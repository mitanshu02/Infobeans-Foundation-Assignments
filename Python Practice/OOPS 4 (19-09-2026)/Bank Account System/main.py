from models import Account

c1 = Account(1074213141567,"Rohit Singh",15000)
c2 = Account(1074213141568,"Pawan Kumar",19000)
c3 = Account(1074213141569,"Sahara Kaur",74000)
c4 = Account(1074213141570,"Pappu Patel",115000)
c5 = Account(1074213141571,"Karan Roy",2000)

customers = [c1,c2,c3,c4,c5]

while True:
    print("""
1. Display all accounts.
2. Search an account using Account Number.
3. Deposit money into a selected account.
4. Withdraw money from a selected account.
5. Display accounts having balance greater than 50,000.
6. Find the account having the highest balance.
7. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Account Information ----")
        print()
        for cust in customers:
            print(f"{cust.acc_no:20}|{cust.customer_name:20}|{cust.balance:10} ")

    elif n == 2:
        accNo = int(input("Enter account Number: "))

        for cust in customers:
            if cust.acc_no == accNo:
                print(f"{cust.acc_no:20}|{cust.customer_name:20}|{cust.balance:10} ")
                break
        else:
            print("[ Account Not Found ]")

    elif n == 3:
        accNo = int(input("Enter account Number: "))
        
        for cust in customers:
            if cust.acc_no == accNo:
                amount = float(input("Enter amount to deposit: "))

                cust.deposit(amount)
                break
        else:
            print("Account do not exists")

    elif n == 4:
        accNo = int(input("Enter account Number: "))
                
        for cust in customers:
            if cust.acc_no == accNo:
                amount = float(input("Enter amount to withdraw: "))

                cust.withdraw(amount)
                break
        else:
            print("Account do not exists")

    elif n == 5:
        for cust in customers:
            if cust.balance >= 50000:
                print(f"{cust.acc_no:20}|{cust.customer_name:20}|{cust.balance:10} ")

    elif n == 6:
        highest = 0
        accNo = None

        for cust in customers:
            if cust.balance > highest:
                highest = cust.balance
                accNo = cust.acc_no

        for cust in customers:
            if cust.acc_no == accNo:
                print(f"{cust.acc_no:20}|{cust.customer_name:20}|{cust.balance:10} ")
                break
        else:
            print("No maximum balance account found.")
    elif n == 7:
        print("[ Exiting Program ]")
        break
    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue
        

    


