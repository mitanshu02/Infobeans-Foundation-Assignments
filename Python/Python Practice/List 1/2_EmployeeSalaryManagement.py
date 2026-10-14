'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []

'''
l = int(input("Enter number of employees: "))
salary = []

for i in range(l):
    s = int(input(f"Enter Salary of Employee {i+1}: "))
    salary.append(s)

average = sum(salary)/l
print(f"Average Salary of Employees: ₹{average:.2f}")

print("Above Average: ",end = "")
for s in salary[:]:
    if s > average:
        print(s,end=" ")
    if s < 15000:
        salary.remove(s)

#print(salary)
