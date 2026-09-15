"""
Hospital Management System
Doctor Management Package

This module contains functions for:
- Adding doctors
- Displaying doctors
"""
doctors = []

def add_doctor():
    d = {}
    d['id'] = input("Enter doctor id: ")
    d['name'] = input("Enter name: ")
    d['specialization'] = input("Enter Specialization: ")
    d['experience'] = input("Enter experience: ")
    d['fees'] = input("Enter Consultation Fee: ")
    doctors.append(d)
    print("Doctor Added Successfully.")

def display_doctors():
    print("Doctors Information: ")
    print()
    for doctor in doctors:
        print()
        print("Doctor ID        :",doctor['id'])
        print("Name             :",doctor['name'])
        print("Specialization   :",doctor['specialization'])
        print("Experience       :",doctor['experience'])
        print("Consultation Fees:",doctor['fees'])
        print()
        print("=========================================")