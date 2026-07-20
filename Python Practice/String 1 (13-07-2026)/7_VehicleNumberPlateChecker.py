'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''

n = input("Enter vehicle number: ").lower()

l = len(n)

if l != 10:
    print("Invalid Vehicle Number")
else:
    for i in range(l):
        ch = n[i]
        if 0<=i<=1 and not ('a'<=ch<='z'):
            print("Invalid vehicle number")
            break
        elif 2<=i<=3 and not('0'<=ch<='9'):
            print("Invalid vehicle number")
            break
    else:
        print("Valid vehicle number")
        

