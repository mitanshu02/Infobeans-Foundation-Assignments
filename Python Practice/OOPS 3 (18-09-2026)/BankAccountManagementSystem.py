'''
QNO 1: Bank Account Management System

ABC Bank wants to develop a software application to manage customer accounts.

Each customer has:

Account Number
Customer Name
Account Balance

A customer should be able to:

Deposit money
Withdraw money
Check account balance
Transfer money to another customer

The bank also wants to maintain information that is common for all customers:

Bank Name
Interest Rate

The bank management may change the interest rate in the future, and the change should apply to all customers.

Additionally, the application should provide some utility operations:

Validate whether an account number is valid.
Calculate interest on a given amount.
Generate a transaction ID.
Requirements

Class Variables

bank_name
interest_rate

Instance Variables

account_no
customer_name
balance

Instance Methods

deposit(amount)
withdraw(amount)
transfer_money(receiver, amount)
display_balance()

Class Methods

change_interest_rate(new_rate)
change_bank_name(new_name)
display_bank_info()

Static Methods

validate_account_number(account_no)
calculate_interest(amount, rate)
generate_transaction_id()

Sample Input
Customer 1
Account No : 1001
Name       : deepika
Balance    : 50000

Customer 2
Account No : 1002
Name       : Priya
Balance    : 30000

Deposit Amount : 10000
Transfer Amount : 15000
New Interest Rate : 7.5
Sample Output
Customer : deepika
Balance  : 45000

Customer : Priya
Balance  : 45000

Bank Name      : ABC Bank
Interest Rate  : 7.5%
Transaction ID : TXN1025

Task: Design a Python class named BankAccount and implement all the above methods using instance methods, class methods, and static methods appropriately.
'''
import random

class Bank:
    bank_name = "SBI"
    intrest_rate = 8

    def __init__(self,accNo,Cname,balance):
        if self.validate_account_number(accNo):
            self.account_no = accNo
        else:
            print("Invalid Account Number.")
            self.account_no = None
        self.customer_name = Cname
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("------ Enter a valid amount ------")

    def withdraw(self,amount):
        if amount <= self.balance:
            if amount > 0:
                self.balance -= amount
            else:
                print("Enter valid balance")
        else:
            print("Insufficient Amount")

    def transfer_money(self,reciever,amount):
        if self.balance >= amount:
            if amount > 0:
                self.balance -= amount
                self.reciever = reciever
                reciever.balance += amount
                print("Amount Transferred Successfully")
                print(f"[Transaction ID : {self.generate_transaction_id}]")
            else:
                print("Enter a valid amount")
        else:
            print("Insufficient Amount")

    def display_balance(self):
        print("Your balance is: ",self.balance)

    @classmethod
    def change_intrest_rate(cls,new_rate):
        cls.intrest_rate = new_rate
        print(f"Intrest rate changed to {new_rate}")

    @classmethod
    def chane_bank_name(cls,new_name):
        cls.bank_name = new_name
        print(f"Bank name updated to {new_name}")

    @classmethod
    def display_bank_info(cls):
        print("================================")
        print("          Bank Info             ")
        print("================================")
        print()
        print("Bank name       :",cls.bank_name)
        print("Intrest Rate    :",cls.intrest_rate,"%")

    @staticmethod
    def validate_account_number(account_no):
        if len(str(account_no)) < 10:
            return False
        else:
            return True

    @staticmethod
    def calculate_intrest(amount,rate):
        return (amount*rate)/100

    @staticmethod
    def generate_transaction_id():
        return "TXN"+str(random.randint(1000,9999))


c1 = Bank(9856475859565,"Sumit",55000)
c2 = Bank(9898111111111115,"Ravi",10000)

# print(c1.account_no)
# print(c2.account_no)
c1.transfer_money(c2,15000)
c1.display_balance()
c2.display_balance()
# Bank.chane_bank_name("ICICI Bank")
# Bank.display_bank_info()


    
        