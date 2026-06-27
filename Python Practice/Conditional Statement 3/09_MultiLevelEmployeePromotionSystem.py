experience = int(input("Experience = "))
rating = int(input("Rating = "))

if experience >= 5:
    if rating >= 4:
        projects = int(input("Projects = "))

        if projects >= 3:
            salary = int(input("Salary = "))

            if salary <= 50000:
                print("Promotion Status = Promoted with 30% Hike")
            else:
                print("Promotion Status = Promoted with 20% Hike")
        else:
            print("Promotion Status = Promoted with 10% Hike")
    else:
        print("Promotion Status = No Promotion")
else:
    if rating == 5:
        print("Promotion Status = Fast Track Promotion")
    else:
        print("Promotion Status = No Promotion")