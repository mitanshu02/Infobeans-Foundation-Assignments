age = int(input("Enter age: "))

if age<12:
    tp = 100
elif age >=12 and age <= 60:
    tp = 200
else:
    tp = 150

print("Ticket Price: ₹",tp)