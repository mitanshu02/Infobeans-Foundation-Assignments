"""
Assignment 2 � Employee Joining & Experience System

Create an employee experience calculator.

Read:
- Employee name
- Joining date
- Current date

Calculate:
- Total days worked
- Total years worked
- Total months approximately
- Experience in Years Months Days
- Whether employee has completed 1 year
- Whether employee has completed 5 years

Example:

Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026

Output:

Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes
"""
from datetime import datetime

eName = input("Enter employee name: ")
jDate = input("Enter joining date (dd-mm-yyyy): ")
cDate = input("Enter current date (dd-mm-yyyy): ")

JDate = datetime.strptime(jDate,"%d-%m-%Y")
CDate = datetime.strptime(cDate,"%d-%m-%Y")
print("Employee: ",eName)
print("Joining Date: ",jDate)
if CDate.month >= JDate.month:
    months = CDate.month - JDate.month
else:
    months = 12-(CDate.month - JDate.month)

if CDate.day >= JDate.day:
    days = CDate.day - JDate.day
else:
    pass
print("Experience: ",CDate.year-JDate.year,"Years",months,"Months",)


