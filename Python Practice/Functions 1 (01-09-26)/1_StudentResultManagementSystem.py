'''
1.
STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

*** STUDENT RESULT MANAGEMENT ***

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.
'''



s = []

def LogDetails():
    name = input("Enter your name: ")
    roll = int(input("Enter your Roll No.: "))

    marks = []
    for i in range(5):
        marks.append(int(input(f"Enter marks of subject {i+1}: ")))

    s.append(name)
    s.append(roll)
    s.append(marks)
    print()
    print("----------- Student Detais Entered Successfully ------------")
    
def totalMarks():
    total = 0
    for i in range(len(s[2])):
        total = total + s[2][i]
    return total

def findPercentage():
    total = totalMarks()
    
    return (total/500)*100
     
def findGrade():
    p = findPercentage()
    
    if 90 <= p <= 100:
        return "A+"
    elif 80 <= p < 90:
        return "A"
    elif 70 <= p < 80:
        return "B"
    elif 60 <= p < 70:
        return "C"
    elif 50 <= p < 60:
        return "D"
    else:
        return "Fail" 

def findHighest():
    return max(s[2])

def findLowest():
    return min(s[2])
    

def displayResult():
    print("----------- RESULT CARD -----------")
    print()
    print("Name        : ",s[0])
    print("Roll Number : ",s[1])
    print()
    print("Marks")
    for i in range(5):
        print(f"Subject {i+1} : {s[2][i]}")

    print()
    print("Total Marks : ",totalMarks())
    print("Percentage  : ",findPercentage())
    print("Grade       : ",findGrade())
    print("Highest Mark: ",findHighest())
    print("Lowest Mark : ",findLowest())

while True:
    print()
    print("MENU")
    print()
    print("""
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
""")
    n = int(input("Select an option: "))
    
    match n:
        case 1:
            LogDetails()
        case 2:
            print()
            print("Total Marks = ",totalMarks())
        case 3:
            print()
            print("Total Percentage = ",findPercentage())
        case 4:
            print()
            print("Grade =",findGrade())
        case 5:
            print()
            displayResult()
        case 6:
            print()
            print("Highest Mark = ",findHighest())
        case 7:
            print()
            print("Lowest Mark = ",findLowest())
        case 8:
            print()
            print("============================================")
            print("          Thank You. Program Terminated.    ")
            print("============================================")
            break
        case __:
            continue
            
    