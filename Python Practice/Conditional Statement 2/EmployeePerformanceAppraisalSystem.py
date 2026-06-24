salary = int(input("Enter salary: "))
rating = int(input("Enter rating: "))

if rating == 5:
    total = salary + (salary * 0.25)

    if salary < 20000:
        total = total + 2000
elif rating == 4:
    total = salary + (salary * 0.20)

    if salary < 20000:
        total = total + 2000
elif rating == 3:
    total = salary + (salary * 0.10)
elif rating == 2:
    total = salary + (salary * 0.05)
else:
    total = salary

print("Revised Salary: ₹", total)