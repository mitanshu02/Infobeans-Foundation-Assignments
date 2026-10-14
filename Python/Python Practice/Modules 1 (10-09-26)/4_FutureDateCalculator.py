"""
Assignment 4 � Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu:

========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice:

CASE 1 � Add Days

Read:
- Starting date
- Number of days

Input:
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100

Output:
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026

CASE 2 � Add Weeks

Read:
- Starting date
- Number of weeks

Input:
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4

Output:
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026

CASE 3 � Add Hours

For this case, the student should take date and time as input.

Input:
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15

Output:
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30

This case should test whether students understand that adding hours can change the date.

CASE 4 � Add Minutes

Take date/time and number of minutes.

Input:
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90

Output:
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00

Students must correctly handle the change from 10 September to 11 September.

CASE 5 � Exit

Enter your choice: 5

Thank you for using Future Date Calculator!

Complete Sample Run:

========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice: 1

Enter starting date (DD-MM-YYYY): 25-12-2026
Enter number of days to add: 15

Starting Date : 25-12-2026
Days Added    : 15
Future Date   : 09-01-2027

Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 31-12-2026 23:30
Enter number of minutes to add: 90

Starting Date & Time : 31-12-2026 23:30
Minutes Added        : 90
Future Date & Time   : 01-01-2027 01:00

Enter your choice: 5

Thank you for using Future Date Calculator!
"""
from datetime import datetime,timedelta

while True:
    print("""
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

 """)

    n = int(input("Select an option: "))

    match n:
        case 1:
            start = input("Enter starting date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter number of days to add: "))
            print()
            print("Starting Date: ",start)
            print("Days Added: ",increment)
            print("Future Date: ",(s+timedelta(days=increment)).strftime("%d-%m-%Y"))

        case 2:
            start = input("Enter starting date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter number of weeks to add: "))
            print()
            print("Starting Date: ",start)
            print("Weeks Added: ",increment)
            print("Future Date: ",(s+timedelta(weeks=increment)).strftime("%d-%m-%Y"))
        case 3:
            start = input("Enter date and time (DD-MM-YYYY HH:MM): ")
            s = datetime.strptime(start,"%d-%m-%Y %H:%M")
            increment = int(input("Enter number of hours to add: "))
            print()
            print("Starting Date: ",start)
            print("Hours Added: ",increment)
            print("Future Date: ",(s+timedelta(hours=increment)).strftime("%d-%m-%Y %H:%M"))
        case 4:
            start = input("Enter date and time (DD-MM-YYYY HH:MM): ")
            s = datetime.strptime(start,"%d-%m-%Y %H:%M")
            increment = int(input("Enter number of minutes to add: "))
            print()
            print("Starting Date: ",start)
            print("Minutes Added: ",increment)
            print("Future Date: ",(s+timedelta(minutes=increment)).strftime("%d-%m-%Y %H:%M"))
        case 5:
            print("Thank you for using Future Date Calculator!")
            break
        case __:
            print("Select a valid option")
            continue
        