travel_class = input("Class = ").lower()
distance = int(input("Distance = "))
booking = input("Booking = ").lower()

if travel_class == "business":
    if distance > 1000:
        print("Ticket Price = 8000")
    else:
        print("Ticket Price = 5000")
else:
    if distance > 1000:
        if booking == "early":
            print("Ticket Price = 4000")
        else:
            print("Ticket Price = 5000")
    else:
        print("Ticket Price = 2500")