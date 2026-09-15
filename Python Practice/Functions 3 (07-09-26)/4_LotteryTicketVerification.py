"""
Assignment 4: Lottery Ticket Verification (Count Occurrences Using Recursion)

Write a recursive function to count the number of occurrences of a given digit in a ticket number.

Input:
Enter Ticket Number:
1122334412

Enter Lucky Digit:
2

Output:
Digit 2 appears 3 times.
"""
n = int(input("Enter Ticket Number: "))
d = int(input("Enter Lucky Digit: "))

def countOccurances(n,d):
    if n == 0:
        return 0
    if n%10 == d:
        return 1+countOccurances(n//10,d)
    else:
        return 0+countOccurances(n//10,d)

print(f"Digit {d} appears {countOccurances(n,d)} times.")
    