username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
	print("Valid user")
if len(password) >= 8:
	print("Strong password")