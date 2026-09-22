"""
Question 1: Employee Salary Management System

Scenario:
A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements:
Create a class named Employee with the following attributes:
- employee_id
- employee_name
- basic_salary

Initialize the values using a constructor.

Calculations:
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA

Sample Input:
Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000

Sample Output:
------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0
"""
class Employees:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def calculate_hra(self):
            return (self.salary*20)/100
            
    
    def calculate_da(self):
        return (self.salary*15)/100


    def gross_salary(self):
        return self.salary + self.calculate_hra() + self.calculate_da()
        

    def display_salary(self):
        print("------ Employee Salary Details ------")
        print("Employee ID   : ",self.id)
        print("Employee Name : ",self.name)
        print("Salary        : ",self.salary)
        print("HRA           : ",self.calculate_hra())
        print("DA            : ",self.calculate_da())
        print("----------------------------------")
        print("Gross Salary  : ",self.gross_salary()) 

id = input("Enter your ID: ")
name = input("Enter employee name: ")
salary = float(input("Enter salary: "))

e1 = Employees(id,name,salary)
e1.display_salary()