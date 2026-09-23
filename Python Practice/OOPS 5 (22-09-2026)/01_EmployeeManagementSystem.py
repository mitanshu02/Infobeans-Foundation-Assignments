"""
ASSIGNMENT 1 — EMPLOYEE MANAGEMENT SYSTEM

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:
- employee_id
- employee_name
- salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:
display_details()

4. Developer should have:
programming_language

and a method:
write_code()

5. Manager should have:
team_size

and a method:
manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:
@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:
Enter Programming Language:

If Manager:
Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.
"""

class Employee:
    def __init__(self,employee_id,employee_name,salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.__salary = salary

    def display_details(self):
        print("----- Details ------")
        print()
        print("Employee ID   : ",self.employee_id)
        print("Employee Name : ",self.employee_name)
        print("Salary        :",self.__salary)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,amount):
        if amount > 0:
            self.__salary = amount
            print(f"Salary set to {amount}")
        else:
            print("Enter a valid salary.")

    @salary.deleter
    def salary(self):
        del self.__salary
        return "Salary deleted Successfully."
        

class Developer(Employee):
    def __init__(self, employee_id, employee_name, salary,programming_language):
        super().__init__(employee_id, employee_name, salary)
        self.programming_language = programming_language

    def write_code(self):
        print("writing code.")

    def display_details(self):
        super().display_details()
        print("Programming Language : ",self.programming_language)
        print()
        print(f"{self.employee_name} is developing application using {self.programming_language}")

class Manager(Employee):
    def __init__(self, employee_id, employee_name, salary,team_size):
        super().__init__(employee_id, employee_name, salary)
        self.team_size = team_size

    def manage_team(self):
        print("managing team members.")

    def display_details(self):
        super().display_details()
        print("Team Size : ",self.team_size)

    
id = input("Enter your id: ")
name = input("Enter your name: ")
salary = float(input("Enter salary: "))
print("Employee Type: ")
print("1. Developer")
print("2. Manager")

n = int(input("Select: "))
if n == 1:
    pl = input("Enter programming language: ")

    e1 = Developer(id,name,salary,pl)

elif n == 2:
    ts = int(input("Enter team size: "))

    e1 = Manager(id,name,salary,ts)


e1.display_details()