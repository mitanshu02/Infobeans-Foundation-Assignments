"""
Assignment 9: Hospital Record System (Search Digit)

Write a recursive function to determine whether a given digit is present in a patient ID.

Input:
Enter Patient ID:
5837264

Enter Digit:
7

Output:
Digit Found
"""
id = int(input("Enter Patient ID: "))
d = int(input("Enter Digit: "))

def searchDigit(id,d):
    if id == 0:
        return False

    if id%10 == d:
        return True
    return searchDigit(id//10,d)

if searchDigit(id, d):
    print("Digit Found")
else:
    print("Digit Not Found")
