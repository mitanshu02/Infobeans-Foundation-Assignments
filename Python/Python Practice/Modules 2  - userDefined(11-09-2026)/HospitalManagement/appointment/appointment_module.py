"""
Hospital Management System
Appointment Management Package

This module contains functions for:
- Booking appointments
- Displaying appointments

- Appointment ID
- Patient ID
- Doctor ID
- Appointment Date
- Appointment Time
"""
appointments = []

def bookAppointment():
    app = {}
    print()
    print("---------- Book Appointment ---------")
    print()
    print("Enter Following information: ")

    appID  = input("Enter Appointment id: ")
    p_ID = input("Enter patient ID: ")
    d_ID = input("Enter Doctor ID: ")
    app_date = input("Enter appointment date (dd-mm-yyyy): ")
    app_time = input("Enter appointment time (hh:mm)am/pm: ")
    print()

    app["appid"] = appID
    app["pid"] = p_ID
    app["did"] = d_ID
    app["appdate"] = app_date
    app["apptime"] = app_time

    appointments.append(app)
    print("Appointment Booked Successfully.")

def displayAppointment():
    print("------------------------------------")
    print("            Appointments            ")
    print("------------------------------------")
    print()
    for app in appointments:
        print("Appointment ID   :",app["appid"])
        print("Patient ID       :",app["pid"])
        print("Doctor ID        :",app["did"])
        print("Appointment Date :",app["appdate"])
        print("Appointment Time :",app["apptime"])
        print()
        print("----------------------------------------")

    