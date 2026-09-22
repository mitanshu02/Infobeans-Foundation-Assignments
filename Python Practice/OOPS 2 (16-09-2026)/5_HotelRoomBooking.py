"""
Question 5: Hotel Room Booking System

Scenario:
A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements:
Create a class named Guest with:
- guest_id
- guest_name
- number_of_days
- room_charge_per_day

Initialize the values using a constructor.

Calculations:
Room Bill = Number of Days � Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST

Sample Input:
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500

Sample Output:
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ?2500.0
Room Bill             : ?10000.0
GST (12%)             : ?1200.0
Final Bill            : ?11200.0
"""

class Guest:

    def __init__(self, guest_id, guest_name, number_of_days, room_charge_per_day):
        self.guest_id = guest_id
        self.guest_name = guest_name
        self.number_of_days = number_of_days
        self.room_charge_per_day = room_charge_per_day

    def calculate_room_bill(self):
        return self.number_of_days * self.room_charge_per_day

    def calculate_gst(self):
        return self.calculate_room_bill() * 12 / 100

    def calculate_final_bill(self):
        return self.calculate_room_bill() + self.calculate_gst()

    def display_bill(self):
        print("------ Hotel Bill ------")
        print("Guest ID              :", self.guest_id)
        print("Guest Name            :", self.guest_name)
        print("Number of Days        :", self.number_of_days)
        print("Room Charge Per Day   :", float(self.room_charge_per_day))
        print("Room Bill             :", float(self.calculate_room_bill()))
        print("GST (12%)             :", float(self.calculate_gst()))
        print("Final Bill            :", float(self.calculate_final_bill()))


guest_id = input("Enter Guest ID : ")
guest_name = input("Enter Guest Name : ")
number_of_days = int(input("Enter Number of Days : "))
room_charge_per_day = float(input("Enter Room Charge Per Day : "))

guest = Guest(guest_id, guest_name, number_of_days, room_charge_per_day)

guest.display_bill()