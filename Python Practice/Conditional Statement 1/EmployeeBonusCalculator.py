experience = int(input("Experience = "))
rating = int(input("Rating = "))
salary = int(input("Salary = "))

if experience >= 5:
    if rating >= 4:
        if salary < 50000:
            bonus = salary * 20 / 100
            print("Bonus =", bonus)
        else:
            bonus = salary * 10 / 100
            print("Bonus =", bonus)
    else:
        bonus = salary * 5 / 100
        print("Bonus =", bonus)
else:
    print("Bonus = 0")