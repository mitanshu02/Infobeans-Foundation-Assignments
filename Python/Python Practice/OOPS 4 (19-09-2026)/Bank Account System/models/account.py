class Account:
    def __init__(self,acc_no,customer_name,balance):
        self.__acc_no = acc_no
        self.__customer_name = customer_name
        self.__balance = balance

    @property
    def acc_no(self):
        return self.__acc_no

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def balance(self):
        return self.__balance


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Enter a valid amount.")

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def display(self):
        print("Your Balance is: ₹",self.__balance)




