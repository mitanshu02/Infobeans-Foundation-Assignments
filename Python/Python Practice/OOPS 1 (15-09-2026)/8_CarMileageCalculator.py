"""
Assignment 8: Car Mileage Calculator

A car owner wants to calculate the mileage and fuel cost of a journey.

Create a class Car with the following attributes:

- Car brand
- Car model
- Distance travelled in km
- Fuel consumed in litres
- Petrol price per litre

Create the following methods:

calculate_mileage() � Calculate kilometres per litre.

calculate_fuel_cost() � Calculate total fuel cost.

display_trip_details() � Display car and journey details.

Formulas:

Mileage = Distance / Fuel Consumed
Fuel Cost = Fuel Consumed � Petrol Price

Sample data:

Car Brand: Maruti
Car Model: Swift
Distance: 320 km
Fuel Consumed: 20 litres
Petrol Price: 105
"""
class Car:

    def __init__(self, car_brand, car_model, distance, fuel_consumed, petrol_price):
        self.car_brand = car_brand
        self.car_model = car_model
        self.distance = distance
        self.fuel_consumed = fuel_consumed
        self.petrol_price = petrol_price

    def calculate_mileage(self):
        return self.distance / self.fuel_consumed

    def calculate_fuel_cost(self):
        return self.fuel_consumed * self.petrol_price

    def display_trip_details(self):
        print("Car Brand:", self.car_brand)
        print("Car Model:", self.car_model)
        print("Distance Travelled:", self.distance, "km")
        print("Fuel Consumed:", self.fuel_consumed, "litres")
        print("Petrol Price:", self.petrol_price)
        print("Mileage:", self.calculate_mileage(), "km/l")
        print("Fuel Cost:", self.calculate_fuel_cost())


car = Car("Maruti", "Swift", 320, 20, 105)

car.display_trip_details()