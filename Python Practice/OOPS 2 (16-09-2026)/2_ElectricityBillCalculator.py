"""
Question 2: Electricity Bill Calculator

Scenario:
An electricity company wants to generate monthly bills for its customers.

Requirements:
Create a class named Customer with:
- customer_id
- customer_name
- units_consumed

Initialize the values using a constructor.

Calculations:
Cost per Unit = ?8
Fixed Charge = ?150
Total Bill = (Units � 8) + 150

Sample Input:
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350

Sample Output:
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ?2950.0
"""
class Customer:
    def __init__(self, consumer_number, consumer_name, units_consumed):
        self.consumer_number = consumer_number
        self.consumer_name = consumer_name
        self.units_consumed = units_consumed

    def calculate_total_bill(self):
        return self.units_consumed*8 + 150

    def display_bill(self):
        print("--------- Electricity Bill -------")
        print("=====================================")
        print("Consumer ID:", self.consumer_number)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units_consumed)
        print("Total Bill: ₹", self.calculate_total_bill())

id = input("Enter customer id: ")
name = input("Enter customer name: ")
units = int(input("Enter no. of units consumed: "))

c1 = Customer(id,name,units)
c1.display_bill()
    
