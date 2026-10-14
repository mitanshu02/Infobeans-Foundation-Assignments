'''
3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45

'''
while True:
    print("Menu")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score ")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")
    choice = int(input("Enter Choice: "))
    match choice:
        case 1:
            r = int(input("Enter no. of employees: "))
            c = int(input("Enter no. of months: "))
            M = []

            print("Enter scores: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                M.append(row)
                
            highest = 0
            for i in range(r):
                sum = 0
                for j in range(c):
                    sum += M[i][j]
                if sum > highest:
                    idx = i
                    highest = sum
                    
            print(f"Employee {idx+1} has highest Total Score = {highest}")

        case 2:
            r = int(input("Enter no. of employees: "))
            c = int(input("Enter no. of months: "))
            M = []

            print("Enter scores: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                M.append(row)

            for i in range(c):
                sum = 0
                for j in range(r):
                    sum += M[j][i]
                print(f"Month {i+1} Average = {sum//r}")

        case 3:
            r = int(input("Enter no. of employees: "))
            c = int(input("Enter no. of months: "))
            M = []

            print("Enter scores: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                M.append(row)

            for i in range(len(M)):
                print(f"Employee {i+1} Max Score = {max(M[i])}")

        case 4:
            print("Exiting...")
            break
        case _:
            continue