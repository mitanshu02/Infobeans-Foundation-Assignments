"""
ASSIGNMENT 2 — BANK ACCOUNT MANAGEMENT SYSTEM

A bank provides different types of accounts.

Create the following hierarchy:

Account
|
+-------- SavingsAccount
|
+-------- PremiumSavingsAccount

REQUIREMENTS:

1. Create a parent class Account.

Attributes:
- account_number
- customer_name
- balance

2. SavingsAccount should inherit from Account.

Additional attribute:
- interest_rate

3. PremiumSavingsAccount should inherit from SavingsAccount.

Additional attribute:
- cashback_percentage

4. Parent-class data must be initialized using super().

5. Create the following methods:
display_account()
deposit()
withdraw()

6. Override display_account() in SavingsAccount.

7. Override display_account() again in PremiumSavingsAccount.

8. Each overridden method must call the parent method using super().

9. Demonstrate multilevel inheritance.

10. Balance must be encapsulated using:

@property
@balance.setter
@balance.deleter

11. Balance cannot be negative.

12. Read all data from the user.

INPUT:

Enter Account Number:
Enter Customer Name:
Enter Initial Balance:
Enter Account Type:

1. Savings Account
2. Premium Savings Account

For Savings Account:
Enter Interest Rate:

For Premium Savings Account:
Enter Interest Rate:
Enter Cashback Percentage:

Then ask:

Enter amount to deposit:
Enter amount to withdraw:

SAMPLE INPUT:

Enter Account Number: 1001
Enter Customer Name: Amit
Enter Initial Balance: 25000
Enter Account Type: 2
Enter Interest Rate: 7
Enter Cashback Percentage: 2
Enter amount to deposit: 5000
Enter amount to withdraw: 3000

EXPECTED OUTPUT:

## Account Details

Account Number: 1001
Customer Name: Amit
Balance: 25000

Account Type: Premium Savings Account
Interest Rate: 7%
Cashback Percentage: 2%

After Deposit:
Balance: 30000

After Withdrawal:
Balance: 27000
"""

class Account:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance

    def display_account(self):
        print("----- Account Details -----")
        print()
        print("Account Number : ", self.account_number)
        print("Customer Name  : ", self.customer_name)
        print("Balance        : ", self.__balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Amount deposited successfully: ₹{amount}")
        else:
            print("Enter a valid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Amount withdrawn successfully: ₹{amount}")
        elif amount <= 0:
            print("Enter a valid withdrawal amount.")
        else:
            print("Insufficient balance.")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print(f"Balance set to {amount}")
        else:
            print("Balance cannot be negative.")

    @balance.deleter
    def balance(self):
        del self.__balance
        print("Balance deleted successfully.")


class SavingsAccount(Account):
    def __init__(self, account_number, customer_name, balance, interest_rate):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate

    def display_account(self):
        super().display_account()
        print("Interest Rate  : ", self.interest_rate, "%")
        print()


class PremiumSavingsAccount(SavingsAccount):
    def __init__(
        self,
        account_number,
        customer_name,
        balance,
        interest_rate,
        cashback_percentage
    ):
        super().__init__(
            account_number,
            customer_name,
            balance,
            interest_rate
        )
        self.cashback_percentage = cashback_percentage

    def display_account(self):
        super().display_account()
        print("Cashback       : ", self.cashback_percentage, "%")
        print()


account_number = input("Enter account number: ")
customer_name = input("Enter customer name: ")
balance = float(input("Enter balance: "))

print("Account Type: ")
print("1. Savings Account")
print("2. Premium Savings Account")

n = int(input("Select: "))

if n == 1:
    interest_rate = float(input("Enter interest rate: "))

    a1 = SavingsAccount(account_number,customer_name,balance,interest_rate)

elif n == 2:
    interest_rate = float(input("Enter interest rate: "))
    cashback_percentage = float(input("Enter cashback percentage: "))

    a1 = PremiumSavingsAccount(account_number,customer_name,balance,interest_rate,cashback_percentage)

else:
    print("Invalid account type.")
    exit()

a1.display_account()

deposit_amount = float(input("Enter amount to deposit: "))
a1.deposit(deposit_amount)

print()
a1.display_account()

withdraw_amount = float(input("Enter amount to withdraw: "))
a1.withdraw(withdraw_amount)

print()
a1.display_account()