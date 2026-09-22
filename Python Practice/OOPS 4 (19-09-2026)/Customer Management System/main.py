from models import Customer

c1 = Customer(101, "Amit", "Indore", 12000)
c2 = Customer(102, "Rahul", "Bhopal", 8000)
c3 = Customer(103, "Priya", "Indore", 15000)
c4 = Customer(104, "Neha", "Pune", 22000)
c5 = Customer(105, "Rohit", "Indore", 7000)

customers = [c1, c2, c3, c4, c5]

while True:
    print("""
1. Display all customers.
2. Display customers from a particular city.
3. Display customers having purchase amount greater than 10,000.
4. Find customer having highest purchase amount.
5. Calculate total sales.
6. Calculate average purchase amount.
7. Search customer using Customer ID.
8. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Customer Information ----")
        print()

        for cust in customers:
            cust.display()

    elif n == 2:
        cityName = input("Enter City: ")

        for cust in customers:
            if cust.city.lower() == cityName.lower():
                print(f"{cust.customer_id:10}|{cust.customer_name:20}|{cust.purchase_amount:10}")

    elif n == 3:
        print("---- Customers With Purchase Greater Than 10,000 ----")
        print()

        for cust in customers:
            if cust.purchase_amount > 10000:
                print(f"{cust.customer_id:10}|{cust.customer_name:20}|{cust.purchase_amount:10}")

    elif n == 4:
        highest = 0
        custId = None

        for cust in customers:
            if cust.purchase_amount > highest:
                highest = cust.purchase_amount
                custId = cust.customer_id

        for cust in customers:
            if cust.customer_id == custId:
                print("---- Highest Purchase Customer ----")
                cust.display()
                break

    elif n == 5:
        total = 0

        for cust in customers:
            total += cust.purchase_amount

        print("Total Sales:", total)

    elif n == 6:
        total = 0

        for cust in customers:
            total += cust.purchase_amount

        average = total / len(customers)

        print("Average Purchase Amount:", average)

    elif n == 7:
        custId = int(input("Enter Customer ID: "))

        for cust in customers:
            if cust.customer_id == custId:
                print("---- Customer Found ----")
                cust.display()
                break
        else:
            print("[ Customer Not Found ]")

    elif n == 8:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue