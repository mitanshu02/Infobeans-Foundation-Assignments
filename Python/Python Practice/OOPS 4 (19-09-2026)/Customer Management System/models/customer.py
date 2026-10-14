class Customer:
    def __init__(self, customer_id, customer_name, city, purchase_amount):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__city = city
        self.__purchase_amount = purchase_amount

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def customer_name(self):
        return self.__customer_name

    @property
    def city(self):
        return self.__city

    @property
    def purchase_amount(self):
        return self.__purchase_amount

    def display(self):
        print(f"{self.__customer_id:10}|{self.__customer_name:20}|{self.__city:15}|{self.__purchase_amount:10}")