"""
8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
"""

id = int(input("Enter ID: "))
tempID = id

rev = 0
while id>0:
    rev = rev*10 + id%10
    id = id//10

print(f"Reverse = {rev}",end = " ")

# diff nikal rhe between orginal ID and reversed

diff = 0
if tempID > rev:
    diff = tempID - rev
elif tempID < rev:
    diff = rev - tempID
else:
    diff = 0

print(f"Difference = {diff}", end = " ")

# no. of digits nikal rhe

digits = len(str(diff))
print(f"Digits = {digits}", end = " ")

# condition check kr rhe

if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")
