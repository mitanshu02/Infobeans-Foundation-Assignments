"""
Assignment 3 � Date Difference Calculator

Create a program that accepts two dates and displays:

- Difference in days
- Difference in weeks
- Difference in hours
- Difference in minutes

Input:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Example Output:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640
"""
from datetime import datetime

d1 = input("Enter first Date (dd-mm-yyyy): ")
d2 = input("Enter second Date (dd-mm-yyyy): ")

first = datetime.strptime(d1,"%d-%m-%Y")
second = datetime.strptime(d2,"%d-%m-%Y")

diff = abs(first - second)

print("Days Difference:",diff.days)
print("Week Difference:",diff.days//7)
print("Hours Difference:",int(diff.total_seconds()//3600))
print("Minutes Difference:",int(diff.total_seconds()//60))