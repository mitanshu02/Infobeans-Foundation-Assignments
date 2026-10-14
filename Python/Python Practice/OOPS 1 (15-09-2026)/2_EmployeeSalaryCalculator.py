"""
Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

- Employee ID
- Employee name
- Basic salary
- HRA percentage
- DA percentage

Create the following methods:

calculate_hra() � Calculate HRA.

calculate_da() � Calculate DA.

calculate_gross_salary() � Calculate gross salary.

display_salary() � Display employee salary details.

Formula:

HRA = Basic Salary � HRA Percentage / 100
DA = Basic Salary � DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA
"""

class Employee:
    def __init__(self,id,name,salary,hra,da):
        self.id = id
        self.name = name
        self.salary = salary
        self.hra = hra
        self.da = da

    def calculate_hra(self):
        self.hraAmount = (self.salary*self.hra)/100
        return self.hraAmount

    def calculate_da(self):
        self.daAmount = (self.salary*self.da)/100
        return self.daAmount

    def gross_salary(self):
        self.gross = self.salary + self.hraAmount + self.daAmount
        return self.gross
    
    def display_salary(self):
        print("Employee ID   : ",self.id)
        print("Employee Name : ",self.name)
        print("Salary        : ",self.salary)
        print("HRA           : ",self.hraAmount)
        print("DA            : ",self.daAmount)
        print("----------------------------------")
        print("Gross Salary  : ",self.gross)        

e = Employee(101,"Ramesh",15000,10,12)
e.calculate_hra()
e.calculate_da()
e.gross_salary()
e.display_salary()