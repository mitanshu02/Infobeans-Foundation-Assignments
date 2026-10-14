"""
Q4. BANK ACCOUNT MANAGEMENT SYSTEM

Create a class named BankAccount with:

account_number
account_holder
balance

Create the following custom exceptions:

1. InsufficientBalanceException
2. NegativeDepositException
3. InvalidWithdrawalException
4. InvalidAmountException

Requirements:

Create the following methods:

1. deposit(amount)
2. withdraw(amount)
3. check_balance()
4. display_account_details()

deposit(amount):

1. If deposit amount is negative:
   NegativeDepositException:
   Deposit amount cannot be negative

2. If deposit amount is zero:
   InvalidAmountException:
   Deposit amount must be greater than zero

3. Otherwise add the amount to the balance.
4. Display the updated balance.

withdraw(amount):

1. If withdrawal amount is negative:
   InvalidWithdrawalException:
   Withdrawal amount cannot be negative

2. If withdrawal amount is zero:
   InvalidAmountException:
   Withdrawal amount must be greater than zero

3. If withdrawal amount is greater than balance:
   InsufficientBalanceException:
   Insufficient balance

4. Otherwise deduct the amount.
5. Display the updated balance.

MENU:

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit

For invalid menu choices:
Invalid choice

Option 5:
Thank you for using Bank Account System

Exception Handling:

Every transaction must be handled using try-except.

The program should NOT terminate when an exception occurs.
After displaying the exception message, display the menu again.
"""
class InsufficientBalanceException(Exception):
    pass
class NegativeDepositException(Exception):
    pass
class InvalidWithdrawalException(Exception):
    pass
class InvalidAmountException(Exception):
    pass

class BankAccount:
   def __init__(self,account_number,account_holder,balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

   def deposit(self,amount):
      if amount < 0:
           raise NegativeDepositException("Deposit amount cannot be negative")

      elif amount == 0:
          raise InvalidAmountException("Deposit amount must be greater than zero")

      else:
          self.balance += amount
          print("Available Balance:",self.balance)

   def withdraw(self,amount):
      if amount < 0:
          raise InvalidWithdrawalException("Withdrawal amount cannot be negative")

      elif amount == 0:
          raise InvalidAmountException("withdrawal amount must be greater than zero")

      elif amount > self.balance:
          raise InsufficientBalanceException("Insufficient balance")

      else:
          self.balance -= amount
          print("Available Balance:",self.balance)

   def check_balance(self):
       print("Available Balance:",self.balance)
   
   def display_account_details(self):
       print()
       print("====== Account Details =======")
       print()
       print("Account No.       :",self.account_number)
       print("Account Holder    :",self.account_holder)
       print("Available Balance :",self.balance)


b1 = BankAccount(1214546235,"Amit",12000)

while True:
   print("""
MENU:

1. Deposit
2. Withdraw
3. Check Balance
4. Display Account Details
5. Exit
""")

   n = int(input("choice : "))

   match n:
       case 1:
           amount = int(input("Enter Amount: "))
           try:
               b1.deposit(amount)
           except NegativeDepositException as e:
               print("NegativeDepositException :",e)
           except InvalidAmountException as e:
               print("InvalidAmountException :",e) 
       case 2:
           amount = int(input("Enter Amount: "))
           try:
               b1.withdraw(amount)
           except InvalidWithdrawalException as e:
               print("InvalidWithdrawalException :",e)
           except InvalidAmountException as e:
               print("InvalidAmountException :",e)
           except InsufficientBalanceException as e:
               print("InsufficientBalanceException :",e)

       case 3:
           b1.check_balance()

       case 4:
           b1.display_account_details()

       case 5:
           print("Thank you for using Bank Account System")
           break
       
       case __:
           print("Invalid choice")
           input("press Enter to continue")
           continue
   