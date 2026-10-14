"""
Assignment 4: Rectangle Calculator

A civil engineer wants to calculate the area and perimeter of a rectangular plot.

Create a class Rectangle with the following attributes:

- Length
- Breadth

Create the following methods:

calculate_area() � Calculate the area.

calculate_perimeter() � Calculate the perimeter.

display_result() � Display length, breadth, area, and perimeter.

Formulas:

Area = Length � Breadth
Perimeter = 2 � (Length + Breadth)

Sample data:

Length: 15
Breadth: 8
"""
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

    def display_result(self):
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area:", self.calculate_area())
        print("Perimeter:", self.calculate_perimeter())


rectangle = Rectangle(15, 8)

rectangle.display_result()