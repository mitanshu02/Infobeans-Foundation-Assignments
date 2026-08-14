'''
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple

orders = namedtuple("patient",["o_id","c_name","p_name","amount"])

n = int(input("Enter number of orders: "))

o = []

for i in range(n):
    o_id = input(f"Enter id of order {i+1}: ")
    name = input(f"Enter name of customer having order {i+1}: ")
    p_name = input(f"Enter product name of product {i+1}: ")
    amount = int(input(f"Enter amouunt of product {i+1}: "))
   
    ord = orders(o_id,name,p_name,amount)
    o.append(ord)
    print()

for ord in o:
    print(*ord)

highest = o[0].amount
h_idx = 0
total = 0
above10k = 0

for i in range(n):
    total = total + o[i].amount

    if o[i].amount > highest:
        highest = o[i].amount
        h_idx = i

    if o[i].amount > 10000:
        above10k += 1

print()
print("Highest Value Order: ")
print(*o[h_idx])

print()

print("Total Sales: ")
print(total)

print()

print("Order Above ₹10,000: ")
print(above10k)
        