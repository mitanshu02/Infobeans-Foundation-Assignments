class Student:
    def __init__(self, roll_no, name, marks):
        self.__roll_no = roll_no
        self.__name = name
        self.__marks = marks

    @property
    def roll_no(self):
        return self.__roll_no

    @property
    def name(self):
        return self.__name

    @property
    def marks(self):
        return self.__marks

    def display(self):
        print(f"{self.__roll_no:10}|{self.__name:20}|{self.__marks:10}")