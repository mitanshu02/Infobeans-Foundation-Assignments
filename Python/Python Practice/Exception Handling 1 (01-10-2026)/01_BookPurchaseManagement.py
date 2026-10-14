"""
Q1. BOOK PURCHASE MANAGEMENT

Create a class named Book with the following attributes:

book_id
book_title
author_name
price
quantity

Create a custom exception class named InvalidQuantityException.

Requirements:

1. Create the Book class.
2. Create InvalidQuantityException by inheriting from Exception.
3. Create a method purchase(quantity).
4. If requested quantity is greater than available quantity,
   raise InvalidQuantityException with:
   Quantity not available
5. If purchase is successful, reduce the available quantity.
6. Display the remaining quantity.
7. Use try-except to handle the custom exception.
8. Quantity purchased must be a positive integer.
"""
class InvalidQuantityException(Exception):
    pass


class Book:
    def __init__(self,book_id,book_title,author_name,price,quantity):
        self.book_id = book_id
        self.book_title = book_title
        self.author_name = author_name
        self.price = price
        self.quantity = quantity

    def purchase(self,quantity):
        if quantity > self.quantity:
            raise InvalidQuantityException("Quantity not available")
        else:
            self.quantity -= quantity
            return f"Remaining Quantity {self.quantity}"

b1 = Book("b1","Rich Dad Poor Dad","Richard",503,15)
try:
    print(b1.purchase(15))
except InvalidQuantityException as e:
    print("Error :",e)

        
        