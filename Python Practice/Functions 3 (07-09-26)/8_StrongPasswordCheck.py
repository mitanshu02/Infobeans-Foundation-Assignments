"""
Assignment 8: Cyber Security (Strong Password Check)

Write a recursive function to check whether all digits of the given number are even.

Input:
Enter Password:
248620

Output:
Strong Password

Input:
Enter Password:
248621

Output:
Weak Password
"""
p = int(input("Enter password: "))

def check(n):
    if n == 0:
        return True
    if (n%10) % 2 == 0:
        return check(n//10)
    else:
        return False

if check(p):
    print("Strong Password")
else:
    print("Weak Password")