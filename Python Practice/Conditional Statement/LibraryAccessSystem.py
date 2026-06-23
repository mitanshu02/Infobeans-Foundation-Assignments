membership = input("Membership active (yes/no): ")
books = int(input("Books issued: "))

if membership.lower() == "yes":
	print("Entry allowed")
if books < 3:
	print("Can issue more books")