"""
Assignment 2 – Vehicle Rental System

Create a parent class Vehicle with:

vehicle_no
brand
rent_per_day

Create two child classes:

Car
Bike

Requirements

Take vehicle details and number of rental days from the user.
Use super() to initialize common attributes.
Create a method calculate_rent(days) in the parent class.
Override the method in both child classes.
For a Car, add ₹500 service charge to the rental amount.
For a Bike, add ₹200 service charge.

Display the final rental amount.

Sample Input

Enter Vehicle Number: MP09AB1234
Enter Brand: Honda
Enter Rent Per Day: 800
Enter Number of Days: 3
Enter Vehicle Type: Car

Expected Output

----- Rental Details -----
Vehicle Number : MP09AB1234
Brand          : Honda
Rent Per Day   : 800
Number of Days : 3
Vehicle Type   : Car
Rental Amount  : 2400
Service Charge : 500
Final Amount   : 2900
"""
class Vehicle:
    def __init__(self,vehicle_no,brand,rent_per_day):
        self.vehicle_no = vehicle_no
        self.brand = brand
        self.rent_per_day = rent_per_day

    def calculate_rent(self,days):
        return self.rent_per_day*days

class Car(Vehicle):
    def __init__(self, vehicle_no, brand, rent_per_day):
        super().__init__(vehicle_no, brand, rent_per_day)
        self.service_charge = 500
        self.vehicle_type = "Car"

    def calculate_rent(self, days):
        return super().calculate_rent(days) + self.service_charge

class Bike(Vehicle):
    def __init__(self, vehicle_no, brand, rent_per_day):
        super().__init__(vehicle_no, brand, rent_per_day)
        self.service_charge = 200
        self.vehicle_type = "Bike"

    def calculate_rent(self, days):
        return super().calculate_rent(days) + self.service_charge


no = input("Enter vehicle number: ")
brand = input("Enter vehicle brand: ")
rent_per_day = int(input("Enter rent per day: "))
days = int(input("Enter number of days: "))

print("""
Type:
    1. Car
    2. Bike
    """)

n = int(input("Select Vehicle type: "))

if n == 1:
    obj = Car(no,brand,rent_per_day)
elif n == 2:
    obj = Car(no,brand,rent_per_day)
else:
    print("Invalid input.")

print(f"""
----- Rental Details -----
Vehicle Number : {obj.vehicle_no}
Brand          : {obj.brand}
Rent Per Day   : {obj.rent_per_day}
Number of Days : {days}
Vehicle Type   : {obj.vehicle_type}
Rental Amount  : {Vehicle.calculate_rent(days)}
Service Charge : {obj.service_charge}
Final Amount   : {obj.calculate_rent(days)}
""")