'''
1.
=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
'''

n = int(input("Enter number of items you want: "))

d = {}

for i in range(n):
    print(f"Enter details for product {i+1}")
    prod = input("Enter name of product: ")
    qty = int(input("Enter quantity of product: "))

    d[prod] = qty
    print()

print("Total Quantity =",sum(d.values()))