'''
11.
=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''
sales = [p for p in input("Enter products names: ").split()]

d = {}

for product in sales:
    d[product] = d.get(product,0)+1

for p in sorted(d.keys()):
    print(p,":",d[p])

