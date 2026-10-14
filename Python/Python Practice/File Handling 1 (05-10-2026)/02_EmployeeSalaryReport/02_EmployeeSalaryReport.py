"""
Q2. EMPLOYEE SALARY REPORT

A company stores employee salary information in employees.txt.

Each record contains:

EmployeeID,EmployeeName,Department,Salary

Write a Python program to:

1. Accept employee details.
2. Store them in the file.
3. Read the file.
4. Display employees whose salary is greater than ₹50,000.
5. Calculate the average salary.
"""

n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"Enter details of employee {i+1}")
    eid = input("Id : ")
    name = input("Enter name: ")
    dept = input("Enter department: ")
    salary = int(input("Enter salary: "))

    with open("employees.txt","a") as f:
        f.write(f"{eid} {name} {dept} {salary}\n")

with open("employees.txt","r") as f:
    count = 0
    total = 0
    print("Employee with salary > 50000")
    print("____________________________")
    for emp in f:
        count += 1
        total += int(emp.strip().split()[3])
        if int(emp.strip().split()[3]) > 50000:
            print(emp)

    print()
    print("Average Salary: ",total/count)
