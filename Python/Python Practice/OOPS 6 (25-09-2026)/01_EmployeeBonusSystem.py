"""
Assignment 1 – Employee Bonus System

Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager

Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.

Sample Input

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output

----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000
"""
class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary


class Developer(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)

    def calculate_bonus(self):
        return self.salary*0.1

class Manager(Employee):
    def __init__(self, id, name, salary):
        super().__init__(id, name, salary)

    def calculate_bonus(self):
        return self.salary*0.2


id = input("Enter employee id: ")
name = input("Enter name : ")
salary = float(input("Enter salary: "))

print("""
Type:
    1. Developer
    2. Manager
    """)

n = int(input("Select Employee type: "))
if n == 1:
    obj = Developer(id,name,salary)
    type = "Developer"
elif n == 2:
    obj = Manager(id,name,salary)
    type = "Manager"
else:
    print("Invalid input.")

print(f"""
----- Employee Details -----
Employee ID   : {obj.id}
Employee Name : {obj.name}
Salary        : {obj.salary}
Employee Type : {type}
Bonus         : {obj.calculate_bonus()}
Total Amount  : {obj.salary + obj.calculate_bonus()}
""")

