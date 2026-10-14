'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

'''
un = input("Enter username: ")

l = len(un)

if not 5<=l<=12:
    print("Invalid Username")
else:
    valid = True
    for i in range(l):
        ch = un[i]
        if i == 0 and not (('a'<=ch<='z')or('A'<=ch<='Z'))  :
            valid = False
            break
        elif 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9' or ch == "_":
            pass
        else:
            valid = False
            break
    
    if valid :
        print("Valid Username")
    else:
        print("Invalid Username")            
             