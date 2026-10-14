"""
QUESTION 2: HOSPITAL PATIENT BILLING SYSTEM

Develop a MENU-DRIVEN Hospital Patient Billing System.

The hospital treats different categories of patients:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

Every patient must perform common operations such as:

calculate_bill()
calculate_discount()
calculate_final_amount()
generate_bill()

However, the calculation rules are different for each type
of patient.

Therefore, use ABSTRACTION to design the system.

ABSTRACT CLASS:

Create an abstract class:

Patient

It should contain appropriate abstract methods required for
billing.

Create the following child classes:

1. GeneralPatient
2. EmergencyPatient
3. InsurancePatient
4. CorporatePatient

MAIN MENU:

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit

OPTION 1: REGISTER PATIENT

Input:

Patient ID
Patient Name
Patient Age

Then select patient type:

1. General Patient
2. Emergency Patient
3. Insurance Patient
4. Corporate Patient

GENERAL PATIENT:

Consultation Fee: Rs.500
Room Charge: Rs.1000 per day
Medicine Charge: Actual amount
Discount: No discount

Input:

Number of Days
Medicine Charge

EMERGENCY PATIENT:

Consultation Fee: Rs.1000
Emergency Charge: Rs.500
Room Charge: Rs.2000 per day
Medicine Charge: Actual amount
Discount: No discount

Input:

Number of Days
Medicine Charge

INSURANCE PATIENT:

Consultation Fee: Rs.800
Room Charge: Rs.1500 per day
Medicine Charge: Actual amount

Insurance covers 70% of the total hospital bill.

Patient pays remaining 30%.

Input:

Number of Days
Medicine Charge

CORPORATE PATIENT:

Consultation Fee: Rs.700
Room Charge: Rs.1200 per day
Medicine Charge: Actual amount

Corporate Discount = 20%

Input:

Number of Days
Medicine Charge

OPTION 2: GENERATE PATIENT BILL

Ask for Patient ID.

If patient exists, generate and display the bill according
to the patient's type.

The calculation must be performed by the appropriate child
class.

OPTION 3: VIEW PATIENT BILL

Ask for Patient ID.

Display the complete patient bill.

If patient does not exist:

Patient record not found.

OPTION 4:

Display:

Thank you for using Hospital Management System.
"""

from abc import ABC, abstractmethod


class Patient(ABC):
    def __init__(self, patient_id, patient_name, patient_age):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def calculate_discount(self):
        pass

    @abstractmethod
    def calculate_final_amount(self):
        pass

    @abstractmethod
    def generate_bill(self):
        pass


class GeneralPatient(Patient):
    def __init__(self, patient_id, patient_name, patient_age, days, medicine):
        super().__init__(patient_id, patient_name, patient_age)
        self.days = days
        self.medicine = medicine
        self.consultation = 500
        self.room = 1000

    def calculate_bill(self):
        return self.consultation + self.room * self.days + self.medicine

    def calculate_discount(self):
        return 0

    def calculate_final_amount(self):
        return self.calculate_bill() - self.calculate_discount()

    def generate_bill(self):
        bill = self.calculate_bill()
        discount = self.calculate_discount()
        final = self.calculate_final_amount()

        print(f"""
========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : General

Consultation Fee : Rs.{self.consultation:.2f}
Room Charges     : Rs.{self.room * self.days:.2f}
Medicine Charges : Rs.{self.medicine:.2f}

----------------------------------------

Total Hospital Bill : Rs.{bill:.2f}
Discount            : Rs.{discount:.2f}
Patient Payable     : Rs.{final:.2f}

Bill Status         : GENERATED

========================================
""")


class EmergencyPatient(Patient):
    def __init__(self, patient_id, patient_name, patient_age, days, medicine):
        super().__init__(patient_id, patient_name, patient_age)
        self.days = days
        self.medicine = medicine
        self.consultation = 1000
        self.emergency = 500
        self.room = 2000

    def calculate_bill(self):
        return (
            self.consultation
            + self.emergency
            + self.room * self.days
            + self.medicine
        )

    def calculate_discount(self):
        return 0

    def calculate_final_amount(self):
        return self.calculate_bill() - self.calculate_discount()

    def generate_bill(self):
        bill = self.calculate_bill()
        discount = self.calculate_discount()
        final = self.calculate_final_amount()

        print(f"""
========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : Emergency

Consultation Fee : Rs.{self.consultation:.2f}
Emergency Charge : Rs.{self.emergency:.2f}
Room Charges     : Rs.{self.room * self.days:.2f}
Medicine Charges : Rs.{self.medicine:.2f}

----------------------------------------

Total Hospital Bill : Rs.{bill:.2f}
Discount            : Rs.{discount:.2f}
Patient Payable     : Rs.{final:.2f}

Bill Status         : GENERATED

========================================
""")


class InsurancePatient(Patient):
    def __init__(self, patient_id, patient_name, patient_age, days, medicine):
        super().__init__(patient_id, patient_name, patient_age)
        self.days = days
        self.medicine = medicine
        self.consultation = 800
        self.room = 1500
        self.insurance = 70

    def calculate_bill(self):
        return self.consultation + self.room * self.days + self.medicine

    def calculate_discount(self):
        return self.calculate_bill() * self.insurance / 100

    def calculate_final_amount(self):
        return self.calculate_bill() - self.calculate_discount()

    def generate_bill(self):
        bill = self.calculate_bill()
        amount = self.calculate_discount()
        final = self.calculate_final_amount()

        print(f"""
========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : Insurance

Consultation Fee : Rs.{self.consultation:.2f}
Room Charges     : Rs.{self.room * self.days:.2f}
Medicine Charges : Rs.{self.medicine:.2f}

----------------------------------------

Total Hospital Bill : Rs.{bill:.2f}

Insurance Coverage  : {self.insurance}%
Insurance Amount    : Rs.{amount:.2f}

Patient Payable     : Rs.{final:.2f}

Bill Status         : GENERATED

========================================
""")


class CorporatePatient(Patient):
    def __init__(self, patient_id, patient_name, patient_age, days, medicine):
        super().__init__(patient_id, patient_name, patient_age)
        self.days = days
        self.medicine = medicine
        self.consultation = 700
        self.room = 1200
        self.discount_rate = 20

    def calculate_bill(self):
        return self.consultation + self.room * self.days + self.medicine

    def calculate_discount(self):
        return self.calculate_bill() * self.discount_rate / 100

    def calculate_final_amount(self):
        return self.calculate_bill() - self.calculate_discount()

    def generate_bill(self):
        bill = self.calculate_bill()
        discount = self.calculate_discount()
        final = self.calculate_final_amount()

        print(f"""
========================================
            PATIENT BILL
========================================

Patient ID       : {self.patient_id}
Patient Name     : {self.patient_name}
Patient Age      : {self.patient_age}
Patient Type     : Corporate

Consultation Fee : Rs.{self.consultation:.2f}
Room Charges     : Rs.{self.room * self.days:.2f}
Medicine Charges : Rs.{self.medicine:.2f}

----------------------------------------

Total Hospital Bill : Rs.{bill:.2f}

Corporate Discount  : {self.discount_rate}%
Discount Amount     : Rs.{discount:.2f}

Patient Payable     : Rs.{final:.2f}

Bill Status         : GENERATED

========================================
""")


patients = {}

while True:
    print("""
========================================
       HOSPITAL MANAGEMENT SYSTEM
========================================

1. Register Patient
2. Generate Patient Bill
3. View Patient Bill
4. Exit
""")

    n = int(input("Enter your choice: "))

    if n == 1:
        id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))

        print("""
Select Patient Type:

1. General
2. Emergency
3. Insurance
4. Corporate
""")

        p = int(input("Enter choice: "))

        if p not in [1, 2, 3, 4]:
            print("Invalid patient type.")
            continue

        days = int(input("Enter Number of Days: "))
        medicine = float(input("Enter Medicine Charge: "))

        if p == 1:
            obj = GeneralPatient(id, name, age, days, medicine)

        elif p == 2:
            obj = EmergencyPatient(id, name, age, days, medicine)

        elif p == 3:
            obj = InsurancePatient(id, name, age, days, medicine)

        else:
            obj = CorporatePatient(id, name, age, days, medicine)

        patients[id] = obj

        print("Patient registered successfully.")

    elif n == 2:
        id = input("Enter Patient ID: ")

        if id in patients:
            obj = patients[id]
            obj.generate_bill()
        else:
            print("Patient record not found.")

    elif n == 3:
        id = input("Enter Patient ID: ")

        if id in patients:
            obj = patients[id]
            obj.generate_bill()
        else:
            print("Patient record not found.")

    elif n == 4:
        print("Thank you for using Hospital Management System.")
        break

    else:
        print("Invalid choice.")