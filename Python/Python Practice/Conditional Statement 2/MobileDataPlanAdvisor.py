data = float(input("Enter daily data usage: "))

if data > 3:
    print("Recommended Plan: Premium Plan")
elif 1 <= data <= 3:
    print("Recommended Plan: Standard Plan")
else:
    print("Recommended Plan: Basic Plan")