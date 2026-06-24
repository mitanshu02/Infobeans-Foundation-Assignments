age = int(input("Age = "))
show_time = input("Show Time = ").lower()
day = input("Day = ").lower()

if age < 18:
    if show_time == "morning":
        print("Ticket Price = 100")
    else:
        print("Ticket Price = 150")
else:
    if show_time == "evening":
        if day == "weekend":
            print("Ticket Price = 300")
        else:
            print("Ticket Price = 250")
    else:
        print("Ticket Price = 200")