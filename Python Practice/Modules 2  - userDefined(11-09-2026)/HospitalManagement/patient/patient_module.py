"""
Hospital Management System
Patient Management Package

This module contains functions for:
- Adding patients
- Displaying patients
- Searching patients
"""
patients = []

def addPatient():
    p = {}
    p["pid"] = input("Enter Patient ID: ")
    p["patientName"] = input("Enter Patient Name: ")
    p["Age"] = int(input("Enter age: "))
    p["gender"] = input("Enter gender: ")
    p["disease"] = input("Enter disease: ")
    p["mobile"] = input("Enter Mobile Number: ")

    patients.append(p)
    print()
    print("Patient Added Succsessfully.")

def displayPatients():
    print("Patients Information: ")
    print()
    for patient in patients:
        print()
        print("Patient ID:",patient['pid'])
        print("Name      :",patient['patientName'])
        print("Age       :",patient['Age'])
        print("Gender    :",patient['gender'])
        print("Disease   :",patient['disease'])
        print("Mobile No.:",patient['mobile'])
        print()
        print("=========================================")

def searchPatient():
    id = input("Enter Patient ID: ")

    for patient in patients:
        if patient['pid'] == id:
            print()
            print("Patient ID:",patient['pid'])
            print("Name      :",patient['patientName'])
            print("Age       :",patient['Age'])
            print("Gender    :",patient['gender'])
            print("Disease   :",patient['disease'])
            print("Mobile No.:",patient['mobile'])
            print()
    else:
        print("Patient Not Found.")
        
