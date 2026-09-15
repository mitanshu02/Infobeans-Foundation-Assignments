"""
Assignment 1 � Age Calculator

Create a program that accepts the user's date of birth and calculates:

- Current age in years
- Completed months
- Total number of days lived
- Next birthday date
- Number of days remaining for the next birthday

Input:
Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:
Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
"""
from datetime import datetime,timedelta

dob = input("Enter DOB (DD-MM-YYYY): ")

convertedDOB = datetime.strptime(dob,"%d-%m-%Y")
now = datetime.now()
yearDiff = now.year-convertedDOB.year
diff = now - convertedDOB

print("Age: ",yearDiff)
print("Completed Months: ",(yearDiff)*12+(abs(now.month-convertedDOB.month)))
print("Total Days Lived:",diff.days,"days")
nextBday = convertedDOB.replace(year=now.year + 1)
print("Next Birthday: ",nextBday.strftime("%d-%m-%Y"))

diffBday = nextBday - now 
print("Days Remaining: ",diffBday.days,"days")



