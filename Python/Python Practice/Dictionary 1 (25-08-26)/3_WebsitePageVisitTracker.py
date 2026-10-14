'''
3.

=========================================
WEBSITE PAGE VISIT TRACKER
==========================

A website records page visits.

pages = ["Home","About","Home","Contact","Home","About"]

Write a program to:

* Count visits of each page using a dictionary.
* Display page name and visit count.

Sample Output:
Home visited 3 times
About visited 2 times
Contact visited 1 time

---
'''

pages = [x for x in input("Enter pages visited: ").split()]

d = {}

for page in pages:
    d[page] = pages.count(page)

    
for key,val in d.items():
    print(f"{key} visited {val} times")

