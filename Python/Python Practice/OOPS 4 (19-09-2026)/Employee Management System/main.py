from models import Employee

e1 = Employee(101, "Amit", 45000, "IT")
e2 = Employee(102, "Rahul", 35000, "HR")
e3 = Employee(103, "Priya", 60000, "IT")
e4 = Employee(104, "Neha", 50000, "Finance")
e5 = Employee(105, "Rohit", 30000, "HR")

employees = [e1, e2, e3, e4, e5]

while True:
    print("""
1. Display all employees.
2. Display employees having salary greater than 40,000.
3. Display employees from IT department.
4. Find employee having highest salary.
5. Calculate total salary.
6. Calculate average salary.
7. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Employee Information ----")
        print()

        for emp in employees:
            emp.display()

    elif n == 2:
        print("---- Employees With Salary Greater Than 40,000 ----")
        print()

        for emp in employees:
            if emp.salary > 40000:
                emp.display()

    elif n == 3:
        print("---- IT Department Employees ----")
        print()

        for emp in employees:
            if emp.department == "IT":
                emp.display()

    elif n == 4:
        highest = 0
        empId = None

        for emp in employees:
            if emp.salary > highest:
                highest = emp.salary
                empId = emp.employee_id

        for emp in employees:
            if emp.employee_id == empId:
                print("---- Highest Salary Employee ----")
                emp.display()
                break

    elif n == 5:
        total = 0

        for emp in employees:
            total += emp.salary

        print("Total Salary:", total)

    elif n == 6:
        total = 0

        for emp in employees:
            total += emp.salary

        average = total / len(employees)

        print("Average Salary:", average)

    elif n == 7:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue