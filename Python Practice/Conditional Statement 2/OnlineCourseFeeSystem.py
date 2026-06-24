course = input("Enter course category: ").lower()
user = input("Enter user type: ").lower()

if course == "Programming":
    amount = 5000
elif course == "Design":
    amount = 4000
else:
    amount = 3000

if user == "Student":
    total = amount - (amount * 0.20)
elif user == "Working Professional":
    total = amount - (amount * 0.10)
else:
    total = amount

print("Final Course Fee: ₹", total)