'''
12.
=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza

---
'''

orders = [x for x in input("Enter food name: ").split()]

d = {}

for o in orders:
    d[o] = d.get(o,0)+1

maximum = 0
maxProductName = ""

for order,qty in d.items():
    print(order,":",qty)

    if qty > maximum:
        maximum = qty
        maxProductName = order

print()
print("Most ordered: ",maxProductName)