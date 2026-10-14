"""
Assignment 5 � Menu-Driven Past Date & Time Calculator

Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.

Menu:

========== PAST DATE & TIME CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

Enter your choice:

CASE 1 � Subtract Days

Input:
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100

Output:
Starting Date   : 10-09-2026
Days Subtracted : 100
Past Date       : 02-06-2026

CASE 2 � Subtract Weeks

Input:
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6

Output:
Starting Date    : 10-09-2026
Weeks Subtracted : 6
Past Date        : 30-07-2026

CASE 3 � Subtract Hours

The student must read both date and time.

Input:
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15

Output:
Starting Date & Time : 10-09-2026 10:30
Hours Subtracted     : 15
Past Date & Time     : 09-09-2026 19:30

CASE 4 � Subtract Minutes

Input:
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90

Output:
Starting Date & Time : 10-09-2026 01:00
Minutes Subtracted   : 90
Past Date & Time     : 09-09-2026 23:30

CASE 5 � Exit

Enter your choice: 5

Thank you for using Past Date & Time Calculator!
"""
from datetime import datetime,timedelta

while True:
    print("""
========== FUTURE DATE CALCULATOR ==========

1. Subtract Days
2. Subtract Weeks
3. Subtract Hours
4. Subtract Minutes
5. Exit

 """)

    n = int(input("Select an option: "))

    match n:
        case 1:
            start = input("Enter starting date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter number of days to Subtract: "))
            print()
            print("Starting Date: ",start)
            print("Days Subtracted: ",increment)
            print("Past Date: ",(s-timedelta(days=increment)).strftime("%d-%m-%Y"))

        case 2:
            start = input("Enter starting date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter number of weeks to Subtract: "))
            print()
            print("Starting Date: ",start)
            print("Weeks Subtracted: ",increment)
            print("Past Date: ",(s-timedelta(weeks=increment)).strftime("%d-%m-%Y"))
        case 3:
            start = input("Enter date and time (DD-MM-YYYY HH:MM): ")
            s = datetime.strptime(start,"%d-%m-%Y %H:%M")
            increment = int(input("Enter number of hours to Subtract: "))
            print()
            print("Starting Date: ",start)
            print("Hours Subtracted: ",increment)
            print("Past Date: ",(s-timedelta(hours=increment)).strftime("%d-%m-%Y %H:%M"))
        case 4:
            start = input("Enter date and time (DD-MM-YYYY HH:MM): ")
            s = datetime.strptime(start,"%d-%m-%Y %H:%M")
            increment = int(input("Enter number of minutes to Subtract: "))
            print()
            print("Starting Date: ",start)
            print("Minutes Subtracted: ",increment)
            print("Past Date: ",(s-timedelta(minutes=increment)).strftime("%d-%m-%Y %H:%M"))
        case 5:
            print("Thank you for using Past Date Calculator!")
            break
        case __:
            print("Select a valid option")
            continue