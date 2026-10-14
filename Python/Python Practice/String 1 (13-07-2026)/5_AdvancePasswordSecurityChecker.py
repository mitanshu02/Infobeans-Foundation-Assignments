'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

'''
pas = input("Enter password: ")
length = len(pas)

if length < 8 or length > 15:
    print("Not Secure")

elif not ('A' <= pas[0] <= 'Z') or not ('0' <= pas[-1] <= '9'):
    print("Not Secure")

else:
    digits = 0
    special = 0
    valid = True

    for ch in pas[1:]:

        if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
            pass

        elif '0' <= ch <= '9':
            digits += 1

        elif ch in "@#$%&*":
            special += 1

        else:
            valid = False
            break

    if valid and digits >= 2 and special >= 1:
        print("Secure Password")
    else:
        print("Not Secure")