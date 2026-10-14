class Book:
    def __init__(self, book_id, book_name, author, price):
        self.__book_id = book_id
        self.__book_name = book_name
        self.__author = author
        self.__price = price

    @property
    def book_id(self):
        return self.__book_id

    @property
    def book_name(self):
        return self.__book_name

    @property
    def author(self):
        return self.__author

    @property
    def price(self):
        return self.__price

    def display(self):
        print(f"{self.__book_id:10}|{self.__book_name:25}|{self.__author:15}|{self.__price:10}")