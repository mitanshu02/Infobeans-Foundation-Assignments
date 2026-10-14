"""
4.Unique Digit Security Scanner


A smart locker accepts only numbers whose all digits are unique.


Write a program using for-else loop to:


- Check every digit

- If any repeated digit found reject

- Else accept


Input:

57294


Output:

Valid Unique Code
"""

n = int(input("Input: "))

st = 0
d = -1

while n>0:
    d = n%10

    if str(d) in str(st):
        print("Reject")
        break

    st = st*10 + n%10

    n = n//10
else:
    print("Accept")
