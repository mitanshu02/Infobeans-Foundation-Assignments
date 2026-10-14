'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for
employees while creating official email accounts. The system should take
the employee’s full name and create an ID using the first character of
each word.

Conditions: - Take first character of every word - Convert all
characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

'''
name = input("Enter employee name: ")
l = len(name)
res = ""
for i in range(l):
    ch = name[i]
    if (i == 0 or name[i-1] == " "):
        if 'a'<=ch<='z':
            res = res + chr((ord(ch)-32))
        elif ('A'<=ch<='Z'):
            res = res + ch

print("Employee Short ID:",res)