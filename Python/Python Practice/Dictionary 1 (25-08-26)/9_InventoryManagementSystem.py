'''
9.
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
---
'''

n = int(input("Enter number of articles: "))

d = {}

for i in range(n):
    print(f"Enter details of product {i+1}: ")
    item = input("Enter product name: ")
    stock = int(input("Enter product stock: "))

    d[item] = stock
    print()

print("Output: ")
for item,stock in d.items():
    if stock < 30:
        print(item)