"""
Assignment 6 � Employee Working Date & Deadline Calculator

Develop a menu-driven Python program for calculating important dates related to an employee or project.

Menu:

========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

Enter your choice:

CASE 1 � Calculate Probation End Date

Take:
- Employee joining date
- Probation period in days

Input:
Enter your choice: 1

Enter employee joining date (DD-MM-YYYY): 15-07-2026
Enter probation period in days: 90

Output:
Joining Date       : 15-07-2026
Probation Period   : 90 days
Probation End Date : 13-10-2026

Use:
timedelta(days=...)

CASE 2 � Calculate Project Deadline

Take:
- Project start date
- Project duration in days

Input:
Enter your choice: 2

Enter project start date (DD-MM-YYYY): 10-09-2026
Enter project duration in days: 120

Output:
Project Start Date : 10-09-2026
Project Duration   : 120 days
Project Deadline   : 08-01-2027

The program must correctly handle:
- Month changes
- Year changes
- Leap years

Students should not manually calculate these.

CASE 3 � Calculate Notice Period End Date

Take:
- Resignation date
- Notice period in days

Input:
Enter your choice: 3

Enter resignation date (DD-MM-YYYY): 20-09-2026
Enter notice period in days: 60

Output:
Resignation Date : 20-09-2026
Notice Period    : 60 days
Last Working Date: 19-11-2026

Additional Test:

Resignation Date : 15-12-2026
Notice Period    : 60 days

The program must correctly move into 2027.

CASE 4 � Calculate Days Remaining for Deadline

Take:
- Current date
- Project deadline

Input:
Enter your choice: 4

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 25-09-2026

Output:
Current Date     : 10-09-2026
Project Deadline : 25-09-2026
Days Remaining   : 15 days

If the deadline has already passed:

Input:
Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 01-09-2026

Output:
Current Date     : 10-09-2026
Project Deadline : 01-09-2026
Deadline Status  : Deadline has already passed
Days Overdue     : 9 days

CASE 5 � Check Employee Work Anniversary

Take:
- Employee joining date
- Current date

Input:
Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 10-09-2020
Enter current date (DD-MM-YYYY): 10-09-2026

Output:
Joining Date : 10-09-2020
Current Date : 10-09-2026

Work Anniversary: YES
Completed Years  : 6 years

If anniversary is not today:

Input:
Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 15-05-2022
Enter current date (DD-MM-YYYY): 10-09-2026

Output:
Joining Date : 15-05-2022
Current Date : 10-09-2026

Work Anniversary: NO
Completed Years  : 4 years

CASE 6 � Exit

Enter your choice: 6

Thank you for using Employee & Project Date Calculator!
"""


from datetime import datetime,timedelta

while True:
    print("""
Menu:

========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

 """)

    n = int(input("Select an option: "))

    match n:
        case 1:
            start = input("Enter employee joining date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter probation period in days: "))
            print()
            print("Output")
            print()
            print("Joining Date: ",start)
            print("Probation Period: ",increment,"days")
            print("Probation End Date: ",(s+timedelta(days=increment)).strftime("%d-%m-%Y"))
        case 2:
            start = input("Enter project start date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter project duration in days: "))
            print()
            print("Output")
            print()
            print("Project Start: ",start)
            print("Project Duration: ",increment,"days")
            print("Project Deadline: ",(s+timedelta(days=increment)).strftime("%d-%m-%Y"))
        case 3:
            start = input("Enter resignation date (DD-MM-YYYY): ")
            s = datetime.strptime(start,"%d-%m-%Y")
            increment = int(input("Enter notice priod duration in days: "))
            print()
            print("Output")
            print()
            print("Resignation Date: ",start)
            print("Notice Period: ",increment,"days")
            print("Last working day: ",(s+timedelta(days=increment)).strftime("%d-%m-%Y"))
           
        case 4:
            current = input("Enter current date (DD-MM-YYYY): ")
            end = input("Enter project deadline (DD-MM-YYYY): ")
            c = datetime.strptime(current,"%d-%m-%Y")
            e = datetime.strptime(end,"%d-%m-%Y")

            print()
            print("Current Date    :",current)
            print("Deadline        :",end)

            if c>e:
                print("Deadline Status : Deadline has already passed.")
                print("Days Overdue    :",(c-e).days,"days")
            else:
                print("Days Remaining  :",(e-c).days,"days")
        
        case 5:
            joining = input("Enter employee joining date (DD-MM-YYYY): ")
            current = input("Enter current date (DD-MM-YYYY): ")
            j = datetime.strptime(joining,"%d-%m-%Y")
            c = datetime.strptime(current,"%d-%m-%Y")
            print()
            print("Output")
            print()
            print("Joining Date: ",joining)
            print("Current Date: ",current)
            print()
            if (j.day == c.day) and (j.month == c.month):
                print("Work anniversary: YES")
            else:
                print("Work anniversary: NO")
            print("Completed Years: ",c.year-j.year,"years")

        case 6:
            print("Thank you for using Employee & Project Date Calculator!")
            break
        case __:
            print("Select a valid option")
            continue