"""
Assignment 3: Bank Account Operations

A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

- Account number
- Account holder name
- Balance

Create the following methods:

deposit() � Add an amount to the balance.

withdraw() � Subtract an amount from the balance.

display_account() � Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000
"""

class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Final Balance:", self.balance)


account = BankAccount(1001, "Rahul", 25000)

account.deposit(5000)
account.withdraw(3000)

account.display_account()