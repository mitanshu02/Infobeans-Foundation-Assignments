'''
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000

==========================================================================================
'''






from collections import namedtuple

emp = namedtuple("employee",["emp_id","emp_name","department","salary"])

n = int(input("Enter number of employees: "))

employees = []

for i in range(n):
    id = int(input(f"Enter Employee {i+1} id: "))
    name = input(f"Enter Employee {i+1} name: ")
    department = input(f"Enter Employee {i+1} department: ")
    salary = int(input(f"Enter Employee {i+1} Salary: "))    

    e = emp(id,name,department,salary)
    
    employees.append(e)  
    print()  

dept = input("Enter Department: ")

for emp in employees:
    print(emp.emp_id, emp.emp_name,emp.department,emp.salary)
   
print()
highest = employees[0].salary
lowest = float('inf')
h_idx = 0
l_idx = 0
total = 0
for i in range(len(employees)):
    total = total + employees[i].salary
    if employees[i].salary > highest:
        highest = employees[i].salary
        h_idx = i
    if employees[i].salary < lowest:
        lowest = employees[i].salary
        l_idx = i

print("Highest Salary Employee: ")
print(employees[h_idx].emp_id,employees[h_idx].emp_name,employees[h_idx].department,employees[h_idx].salary)

print()

print("Lowest Salary Employee: ")
print(employees[l_idx].emp_id,employees[l_idx].emp_name,employees[l_idx].department,employees[l_idx].salary)

print()

print("Average Salary = ",total/n)    

print()
print(f"Employee in {dept} department")
for emp in employees:
    if emp.department == dept:
        print(emp.emp_id, emp.emp_name,emp.department,emp.salary)
