class Employee:
    def __init__(self, employee_id, name, salary, department):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary
        self.__department = department

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def department(self):
        return self.__department

    def display(self):
        print(f"{self.__employee_id:10}|{self.__name:20}|{self.__salary:10}|{self.__department:15}")