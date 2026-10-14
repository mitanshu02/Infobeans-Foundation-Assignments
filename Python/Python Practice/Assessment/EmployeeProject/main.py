from models import Employee,Project

e = []
print("Enter details of 5 employees")

for i in range(5):
    id = input("Enter id: ")
    name = input("Enter name:")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    obj = Employee(id,name,department,salary)
    e.append(obj)

p = []

print("enter project details")

for i in range(5):
    id = input("Enter project id: ")
    name = input("enter project name: ")
    e_id = input("Enter employee id : ")
    cost = int(input("Enter project cost: "))

    obj = Project(id,name,e_id,cost)
    p.append(obj)


while True:
    print("""
========== MENU ==========

1. Display All Employees(.5 marks)
2. Search Employee by ID(.5 marks)
3. Display Employees by Department(.5 marks)
4. Find Highest Paid Employee(.5 marks)
5. Display Employee Projects(.5 marks)
6. Find Highest Cost Project(.5 marks)
7. Exit
""")

    n = int(input("Select an option: "))

    match n:
        case 1:
            for emp in e:
                print(emp.employee_id," ",emp.employee_name," ",emp.department," ",emp.salary)
                print()
        case 2:
            id = input("Enter Employee id: ")

            for emp in e:
                if emp.employee_id == id:
                    print("Employee Id: ",emp.employee_id)
                    print("Employee name: ",emp.employee_name)
                    print("Department : ",emp.department)
                    print("Salary : ₹",emp.salary)
                    print()
                    break
            else:
                print("Not found")
            
        case 3:
            dept = input("Enter department name: ")

            for emp in e:
                if emp.department == dept:
                    print(emp.employee_id," | ",emp.employee_name)
        case 4:
            highest = 0
            id = None

            for emp in e:
                if emp.salary > highest:
                    highest = emp.salary
                    id = emp.employee_id

            print("Highest paid:",end = " ")
            print()
            for emp in e:
                if emp.employee_id == id:
                    print(emp.employee_name)
        case 5:
            for pr in p:
                print(pr.project_id," ",pr.project_name," ",pr.employee_id," ",pr.project_cost)
                print()


        case 6:
            highest = 0
            id = None
            e_id = None
            for pr in p:
                if pr.project_cost > highest:
                    highest = pr.project_cost
                    id = pr.project_id

            for pr in p:
                if pr.project_id == id:
                    print("Project : ",pr.project_name)
                    print("cost: ",pr.project_cost)
                    e_id = pr.employee_id

            for emp in e:
                if e_id == emp.employee_id:
                    print("Emoployee: ",emp.employee_name)

        case 7:
            print("Terminating program")
            break