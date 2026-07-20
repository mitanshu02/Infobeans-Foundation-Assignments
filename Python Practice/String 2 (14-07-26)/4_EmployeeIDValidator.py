'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

id = input("Enter Employee ID: ")

l = len(id)

if l != 8:
    print("Invalid Employee ID")
elif id[:3] != "EMP":
    print("Invalid Employee ID")
else:
    for ch in id[3:]:
        if not '0'<=ch<='9':
            print("Invalid Employee ID")
            break
    else:
        print("Valid Employee ID")
        