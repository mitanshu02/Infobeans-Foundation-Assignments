"""
Question 3: Online Shopping System

Scenario:
An e-commerce company wants to calculate the final amount payable by customers after applying discounts.

Requirements:
Create a class named Product with:
- product_id
- product_name
- quantity
- price_per_item

Initialize the values using a constructor.

Calculations:
Total Amount = Quantity � Price Per Item
If Total Amount > ?5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount - Discount

Sample Input:
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000

Sample Output:
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ?70000.0
Discount          : ?7000.0
Final Amount      : ?63000.0
"""

class Product:

    def __init__(self, product_id, product_name, quantity, price_per_item):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_item = price_per_item

    def calculate_total(self):
        return self.quantity * self.price_per_item

    def calculate_discount(self):
        total = self.calculate_total()

        if total > 5000:
            return total * 10 / 100
        else:
            return total * 5 / 100

    def calculate_final_amount(self):
        return self.calculate_total() - self.calculate_discount()

    def display_bill(self):
        print("------ Shopping Bill ------")
        print("Product ID        :", self.product_id)
        print("Product Name      :", self.product_name)
        print("Quantity          :", self.quantity)
        print("Price Per Item    :", float(self.price_per_item))
        print("Total Amount      :", self.calculate_total())
        print("Discount          :", self.calculate_discount())
        print("Final Amount      :", self.calculate_final_amount())


product_id = input("Enter Product ID : ")
product_name = input("Enter Product Name : ")
quantity = int(input("Enter Quantity : "))
price_per_item = float(input("Enter Price Per Item : "))

product = Product(product_id, product_name, quantity, price_per_item)

product.display_bill()