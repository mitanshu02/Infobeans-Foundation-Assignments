"""
Q1. STUDENT ATTENDANCE MANAGER

A school wants to maintain the attendance of students in a text file named attendance.txt.

Each line contains:
RollNo,StudentName,Status

where Status is either Present or Absent.

Write a Python program to:

1. Accept attendance details for N students.
2. Store the details in attendance.txt.
3. Read the file and display:
   - Total students
   - Number of present students
   - Number of absent students
   - Attendance percentage
"""

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"Enter details of student {i+1}: ")
    print()
    roll = int(input("Enter roll no. : "))
    name = input("Enter name : ")
    status = input("Enter present/absent : ")

    with open("attendance.txt","a") as f:
        f.write(f"{roll} {name} {status}\n")

with open("attendance.txt","r") as f:
   count = 0
   present = 0
   for student in f:
       count += 1
       if student.strip().split()[2] == "present":
           present += 1

   print()
   print("Total Students: ",count)
   print("Present students: ",present)
   print("Absent Students: ",count-present)
   print("Attendance Percentage: ",(present/count)*100,"%") 
    
    