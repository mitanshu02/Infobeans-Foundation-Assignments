"""
QUESTION 1: ONLINE PAYMENT MANAGEMENT SYSTEM

Develop a MENU-DRIVEN Online Payment Management System for an
e-commerce company.

The company supports different payment methods:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

Every payment method follows a common payment process, but the
actual validation, authentication, processing fee and payment
processing logic are different.

Therefore, the system must be designed using ABSTRACTION.

ABSTRACT CLASS:

Create an abstract class named:

Payment

The class should define the following abstract methods:

1. validate_payment()
2. calculate_processing_fee()
3. authenticate_payment()
4. process_payment()
5. generate_receipt()

Create separate child classes for:

1. UPIPayment
2. CreditCardPayment
3. DebitCardPayment
4. NetBankingPayment
5. WalletPayment

Each child class must provide its own implementation of all
required abstract methods.

MAIN MENU:

1. Make Payment
2. View Payment Details
3. Exit

OPTION 1: MAKE PAYMENT

Ask the user to enter:

Customer Name
Order ID
Order Amount

Then select payment method:

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet

UPI:
UPI ID
UPI PIN
Processing Fee: 0%

CREDIT CARD:
Card Number
Card Holder Name
CVV
Expiry Date
Processing Fee: 2% of Order Amount

DEBIT CARD:
Card Number
Card Holder Name
CVV
Expiry Date
Processing Fee: 1% of Order Amount

NET BANKING:
Bank Name
Account Number
Customer ID
Processing Fee: 0.5% of Order Amount

WALLET:
Wallet Name
Mobile Number
Wallet PIN
Processing Fee: 1.5% of Order Amount

OPTION 2: VIEW PAYMENT DETAILS

Ask for Order ID.

If the order exists, display:

Order ID
Customer Name
Payment Method
Order Amount
Processing Fee
Final Amount
Transaction ID
Payment Status

If the order does not exist:

Payment record not found.

OPTION 3:

Display:

Thank you for using Online Payment System.
"""

from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, customer_name, order_id, order_amount):
        self.customer_name = customer_name
        self.order_id = order_id
        self.order_amount = order_amount
        self.transaction_id = "TXN" + order_id
        self.status = "SUCCESS"

    @abstractmethod
    def validate_payment(self):
        pass

    @abstractmethod
    def calculate_processing_fee(self):
        pass

    @abstractmethod
    def authenticate_payment(self):
        pass

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def generate_receipt(self):
        pass


class UPIPayment(Payment):
    def __init__(self, customer_name, order_id, order_amount, upi_id, upi_pin):
        super().__init__(customer_name, order_id, order_amount)
        self.upi_id = upi_id
        self.upi_pin = upi_pin

    def validate_payment(self):
        if self.upi_id and self.upi_pin:
            print("Payment details validated successfully.")
            return True
        else:
            print("Invalid UPI details.")
            return False

    def calculate_processing_fee(self):
        return 0

    def authenticate_payment(self):
        if self.upi_pin:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

    def process_payment(self):
        print("Payment processed successfully.")

    def generate_receipt(self):
        fee = self.calculate_processing_fee()
        total = self.order_amount + fee

        print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : UPI

Order Amount        : Rs.{self.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}

Validating payment details...""")

        if self.validate_payment():
            print("""
Authenticating payment...""")

            if self.authenticate_payment():
                print("""
Processing payment...""")

                self.process_payment()

                print(f"""
Transaction ID      : {self.transaction_id}
Payment Status      : {self.status}

========================================
""")


class CreditCardPayment(Payment):
    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        card_number,
        card_holder_name,
        cvv,
        expiry_date
    ):
        super().__init__(customer_name, order_id, order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date

    def validate_payment(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3 and self.expiry_date:
            print("Payment details validated successfully.")
            return True
        else:
            print("Invalid card details.")
            return False

    def calculate_processing_fee(self):
        return self.order_amount * 0.02

    def authenticate_payment(self):
        if self.cvv:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

    def process_payment(self):
        print("Payment processed successfully.")

    def generate_receipt(self):
        fee = self.calculate_processing_fee()
        total = self.order_amount + fee

        print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : Credit Card

Order Amount        : Rs.{self.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}

Validating payment details...""")

        if self.validate_payment():
            print("""
Authenticating payment...""")

            if self.authenticate_payment():
                print("""
Processing payment...""")

                self.process_payment()

                print(f"""
Transaction ID      : {self.transaction_id}
Payment Status      : {self.status}

========================================
""")


class DebitCardPayment(Payment):
    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        card_number,
        card_holder_name,
        cvv,
        expiry_date
    ):
        super().__init__(customer_name, order_id, order_amount)
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.cvv = cvv
        self.expiry_date = expiry_date

    def validate_payment(self):
        if len(self.card_number) == 16 and len(self.cvv) == 3 and self.expiry_date:
            print("Payment details validated successfully.")
            return True
        else:
            print("Invalid card details.")
            return False

    def calculate_processing_fee(self):
        return self.order_amount * 0.01

    def authenticate_payment(self):
        if self.cvv:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

    def process_payment(self):
        print("Payment processed successfully.")

    def generate_receipt(self):
        fee = self.calculate_processing_fee()
        total = self.order_amount + fee

        print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : Debit Card

Order Amount        : Rs.{self.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}

Validating payment details...""")

        if self.validate_payment():
            print("""
Authenticating payment...""")

            if self.authenticate_payment():
                print("""
Processing payment...""")

                self.process_payment()

                print(f"""
Transaction ID      : {self.transaction_id}
Payment Status      : {self.status}

========================================
""")


class NetBankingPayment(Payment):
    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        bank_name,
        account_number,
        customer_id
    ):
        super().__init__(customer_name, order_id, order_amount)
        self.bank_name = bank_name
        self.account_number = account_number
        self.customer_id = customer_id

    def validate_payment(self):
        if self.bank_name and self.account_number and self.customer_id:
            print("Payment details validated successfully.")
            return True
        else:
            print("Invalid banking details.")
            return False

    def calculate_processing_fee(self):
        return self.order_amount * 0.005

    def authenticate_payment(self):
        if self.customer_id:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

    def process_payment(self):
        print("Payment processed successfully.")

    def generate_receipt(self):
        fee = self.calculate_processing_fee()
        total = self.order_amount + fee

        print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : Net Banking

Order Amount        : Rs.{self.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}

Validating payment details...""")

        if self.validate_payment():
            print("""
Authenticating payment...""")

            if self.authenticate_payment():
                print("""
Processing payment...""")

                self.process_payment()

                print(f"""
Transaction ID      : {self.transaction_id}
Payment Status      : {self.status}

========================================
""")


class WalletPayment(Payment):
    def __init__(
        self,
        customer_name,
        order_id,
        order_amount,
        wallet_name,
        mobile_number,
        wallet_pin
    ):
        super().__init__(customer_name, order_id, order_amount)
        self.wallet_name = wallet_name
        self.mobile_number = mobile_number
        self.wallet_pin = wallet_pin

    def validate_payment(self):
        if self.wallet_name and self.mobile_number and self.wallet_pin:
            print("Payment details validated successfully.")
            return True
        else:
            print("Invalid wallet details.")
            return False

    def calculate_processing_fee(self):
        return self.order_amount * 0.015

    def authenticate_payment(self):
        if self.wallet_pin:
            print("Authentication successful.")
            return True
        else:
            print("Authentication failed.")
            return False

    def process_payment(self):
        print("Payment processed successfully.")

    def generate_receipt(self):
        fee = self.calculate_processing_fee()
        total = self.order_amount + fee

        print(f"""
========================================
          PAYMENT PROCESSING
========================================

Customer Name       : {self.customer_name}
Order ID            : {self.order_id}
Payment Method      : Wallet

Order Amount        : Rs.{self.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}

Validating payment details...""")

        if self.validate_payment():
            print("""
Authenticating payment...""")

            if self.authenticate_payment():
                print("""
Processing payment...""")

                self.process_payment()

                print(f"""
Transaction ID      : {self.transaction_id}
Payment Status      : {self.status}

========================================
""")


payments = {}

while True:
    print("""
========================================
       ONLINE PAYMENT SYSTEM
========================================

1. Make Payment
2. View Payment Details
3. Exit
""")

    n = int(input("Enter your choice: "))

    if n == 1:
        name = input("Enter Customer Name: ")
        order_id = input("Enter Order ID: ")
        amount = float(input("Enter Order Amount: "))

        print("""
Select Payment Method

1. UPI
2. Credit Card
3. Debit Card
4. Net Banking
5. Wallet
""")

        p = int(input("Enter your choice: "))

        if p == 1:
            upi_id = input("Enter UPI ID: ")
            upi_pin = input("Enter UPI PIN: ")

            obj = UPIPayment(
                name,
                order_id,
                amount,
                upi_id,
                upi_pin
            )

            method = "UPI"

        elif p == 2:
            card_number = input("Enter Card Number: ")
            card_holder_name = input("Enter Card Holder Name: ")
            cvv = input("Enter CVV: ")
            expiry_date = input("Enter Expiry Date: ")

            obj = CreditCardPayment(
                name,
                order_id,
                amount,
                card_number,
                card_holder_name,
                cvv,
                expiry_date
            )

            method = "Credit Card"

        elif p == 3:
            card_number = input("Enter Card Number: ")
            card_holder_name = input("Enter Card Holder Name: ")
            cvv = input("Enter CVV: ")
            expiry_date = input("Enter Expiry Date: ")

            obj = DebitCardPayment(
                name,
                order_id,
                amount,
                card_number,
                card_holder_name,
                cvv,
                expiry_date
            )

            method = "Debit Card"

        elif p == 4:
            bank_name = input("Enter Bank Name: ")
            account_number = input("Enter Account Number: ")
            customer_id = input("Enter Customer ID: ")

            obj = NetBankingPayment(
                name,
                order_id,
                amount,
                bank_name,
                account_number,
                customer_id
            )

            method = "Net Banking"

        elif p == 5:
            wallet_name = input("Enter Wallet Name: ")
            mobile_number = input("Enter Mobile Number: ")
            wallet_pin = input("Enter Wallet PIN: ")

            obj = WalletPayment(
                name,
                order_id,
                amount,
                wallet_name,
                mobile_number,
                wallet_pin
            )

            method = "Wallet"

        else:
            print("Invalid payment method.")
            continue

        payments[order_id] = obj

        obj.generate_receipt()

    elif n == 2:
        order_id = input("Enter Order ID: ")

        if order_id in payments:
            obj = payments[order_id]
            fee = obj.calculate_processing_fee()
            total = obj.order_amount + fee

            if isinstance(obj, UPIPayment):
                method = "UPI"
            elif isinstance(obj, CreditCardPayment):
                method = "Credit Card"
            elif isinstance(obj, DebitCardPayment):
                method = "Debit Card"
            elif isinstance(obj, NetBankingPayment):
                method = "Net Banking"
            else:
                method = "Wallet"

            print(f"""
========================================
        PAYMENT DETAILS
========================================

Order ID            : {obj.order_id}
Customer Name       : {obj.customer_name}
Payment Method      : {method}
Order Amount        : Rs.{obj.order_amount:.2f}
Processing Fee      : Rs.{fee:.2f}
Final Amount        : Rs.{total:.2f}
Transaction ID      : {obj.transaction_id}
Payment Status      : {obj.status}

========================================
""")

        else:
            print("Payment record not found.")

    elif n == 3:
        print("Thank you for using Online Payment System.")
        break

    else:
        print("Invalid choice.")