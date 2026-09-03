'''
QNO:
Employee Data Processing System

A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system. To make the application modular and easy to maintain, each operation must be implemented using a separate function that accepts data as a parameter and returns the result.

Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.
Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.
Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function and variable names and follow proper indentation
'''

def find_second_highest_age(ages):
    ages = sorted(list(set(ages)),reverse=True)
    return ages[1]

def count_senior_employees(ages):
    count = 0
    for age in ages:
        if age >= 50:
            count += 1

    return count

def remove_duplicate_ages(ages):
    seen = set()
    res = []
    for age in ages:
        if age not in seen:
            seen.add(age)
            res.append(age)
    return res

def count_names_starting_with_vowel(names):
    count = 0
    for name in names.split():
        if name[0] in "AEIOUaeiou":
            count += 1
    return count

def longest_name(names):
    return max(names.split(),key=len)

while True:
    print("----------------------------------------------------")
    print()
    print("             ----- MENU -----           ")
    print()
    print("""
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
""")
    print()
    n = int(input("Select an option: "))
    print()

    match n:
        case 1:
            ages = [int(x) for x in input("Enter ages seperated by space: ").split()]
            print()
            print("Second Highest Age:",find_second_highest_age(ages))
        case 2:
            ages = [int(x) for x in input("Enter ages seperated by space: ").split()]
            print()
            print("Senior Employees: ",count_senior_employees(ages))
        case 3:
            ages = [int(x) for x in input("Enter ages seperated by space: ").split()]
            print()
            print("Unique Ages: ",remove_duplicate_ages(ages))
        case 4:
            names = input("Enter names of employees seperated by space: ")
            print()
            print("Names Starting with Vowels:",count_names_starting_with_vowel(names))
        case 5:
            names = input("Enter names of employees seperated by space: ")
            print()
            print("Longest Employee Name:",longest_name(names))
        case 6:
            print("==================================")
            print("      Terminating Program         ")
            print("==================================")
            break
        case _:
            continue