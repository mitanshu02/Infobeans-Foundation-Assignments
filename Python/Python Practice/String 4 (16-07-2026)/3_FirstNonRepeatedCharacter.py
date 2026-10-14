'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output:
e

'''

m = input("Input: ")

for c1 in m:
    count = 0
    for c2 in m:
        if c1 == c2:
            count += 1
    if count<=1:
        print("Output:",c1)
        break
else:
    print("No unique character present.")

