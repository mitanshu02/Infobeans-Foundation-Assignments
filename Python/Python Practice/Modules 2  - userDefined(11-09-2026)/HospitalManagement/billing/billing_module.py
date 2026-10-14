"""
Hospital Management System
Billing Package

This module contains the function for:
- Generating patient bills
"""
# - Patient ID
# - Consultation Charges
# - Medicine Cost
# - Test Charges

def generateBill():
    pid = input("Enter patient id: ")
    C_charges = float(input("Enter consultation fee: "))
    M_charges = float(input("Enter medicine cost: "))
    T_charges = float(input("Enter Test charges: "))

    print("=========================================")
    print()
    print("Patient ID          :",pid)
    print("Consultation Charges: ₹",C_charges)
    print("Medicine Cost       : ₹",M_charges)
    print("Test Charges        : ₹",T_charges)
    print("----------------------------------------")
    print("Total Bill          : ₹",C_charges+M_charges+T_charges)
    print()
    print("=========================================")