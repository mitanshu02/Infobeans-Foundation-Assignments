salary = int(input("Monthly Salary = "))
w_days = int(input("Working Days = "))
w_hours = int(input("Working hours per day = "))

print(f"Salary Per day = {salary/w_days}")
print(f"Salary Per hour = {salary/(w_days*w_hours)}")