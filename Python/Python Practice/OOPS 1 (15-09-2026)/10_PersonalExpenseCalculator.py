"""
Assignment 10: Personal Expense Calculator

A person wants to calculate monthly expenses and savings.

Create a class ExpenseTracker with the following attributes:

- Person name
- Monthly salary
- Rent
- Food expenses
- Travel expenses
- Other expenses

Create the following methods:

calculate_total_expenses() � Calculate all expenses.

calculate_savings() � Calculate salary minus total expenses.

display_expense_report() � Display salary, expenses, and savings.

Formula:

Total Expenses = Rent + Food + Travel + Other Expenses
Savings = Monthly Salary - Total Expenses

Sample data:

Monthly Salary: 60000
Rent: 12000
Food: 8000
Travel: 5000
Other Expenses: 3000

Expected result:

Total Expenses: 28000
Savings: 32000
"""
class ExpenseTracker:

    def __init__(self, person_name, monthly_salary, rent, food_expenses, travel_expenses, other_expenses):
        self.person_name = person_name
        self.monthly_salary = monthly_salary
        self.rent = rent
        self.food_expenses = food_expenses
        self.travel_expenses = travel_expenses
        self.other_expenses = other_expenses

    def calculate_total_expenses(self):
        return self.rent + self.food_expenses + self.travel_expenses + self.other_expenses

    def calculate_savings(self):
        return self.monthly_salary - self.calculate_total_expenses()

    def display_expense_report(self):
        print("Person Name:", self.person_name)
        print("Monthly Salary:", self.monthly_salary)
        print("Rent:", self.rent)
        print("Food Expenses:", self.food_expenses)
        print("Travel Expenses:", self.travel_expenses)
        print("Other Expenses:", self.other_expenses)
        print("Total Expenses:", self.calculate_total_expenses())
        print("Savings:", self.calculate_savings())


expense = ExpenseTracker("Rahul", 60000, 12000, 8000, 5000, 3000)

expense.display_expense_report()