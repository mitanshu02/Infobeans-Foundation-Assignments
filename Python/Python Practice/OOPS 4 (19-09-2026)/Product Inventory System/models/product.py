class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price
        self.__quantity = quantity

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def total_value(self):
        return self.__price * self.__quantity

    def display(self):
        print(f"{self.__product_id:10}|{self.__product_name:15}|{self.__price:10}|{self.__quantity:10}")