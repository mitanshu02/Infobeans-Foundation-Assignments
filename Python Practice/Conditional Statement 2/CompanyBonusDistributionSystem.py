salary = int(input("Enter Salary: "))
experience = int(input("Enter years of experience: "))

if experience < 2:
    bonus = 0
elif 5>= experience >= 2: 
    bonus = salary*0.05
elif 10 >= experience > 5:
    bonus = salary*0.1
else:
    bonus = salary*0.2

print(f"Bonus Amount: ₹{bonus}")