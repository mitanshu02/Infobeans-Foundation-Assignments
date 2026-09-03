'''
10.
=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}
---
'''

emails = [x for x in input("Enter Emails: ").split()]

d = {}

for mail in emails:
    domain = mail.split("@")
    d[domain[1]] = d.get(domain[1],0)+1

print(d)

