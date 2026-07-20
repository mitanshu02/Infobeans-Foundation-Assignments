'''
1.  Bank Customer Account Privacy System

A national bank is developing a secure customer portal where account
numbers should not be displayed completely on the screen. For security
reasons, the system should hide all digits except the last four digits
before showing them to users.

Conditions: - Display only the last 4 digits - Replace all previous
characters with *

Input: Enter account number: 123456789012

Output: Masked Account: ****9012

'''
#Approach 1

m = input("Enter account number: ")

l = len(m)

s = l - 4
print("*"*s, end ="")
for i in range(s,l):
    print(m[i],end = "")

'''
#Approach 2
print("*" * (l - 4) + m[-4:])
'''

'''
#Approach 3
n = int(m)

print("*"*stars,end = "")
print(n%10000)

'''