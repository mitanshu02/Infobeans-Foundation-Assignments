"""
Assignment 9: Product Inventory Management

A shopkeeper wants to manage the stock of a product.

Create a class Product with the following attributes:

- Product ID
- Product name
- Price
- Available quantity

Create the following methods:

add_stock() � Increase the available quantity.

sell_product() � Decrease the available quantity.

calculate_stock_value() � Calculate price � available quantity.

display_product() � Display product and stock details.

Sample operations:

Product Name: Laptop
Price: 45000
Initial Quantity: 10
Add Stock: 5
Sell Product: 3

Expected result:

Available Quantity: 12
Total Stock Value: 540000
"""
class Product:

    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def sell_product(self, amount):
        self.quantity -= amount

    def calculate_stock_value(self):
        return self.price * self.quantity

    def display_product(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Available Quantity:", self.quantity)
        print("Total Stock Value:", self.calculate_stock_value())


product = Product(101, "Laptop", 45000, 10)

product.add_stock(5)
product.sell_product(3)

product.display_product()