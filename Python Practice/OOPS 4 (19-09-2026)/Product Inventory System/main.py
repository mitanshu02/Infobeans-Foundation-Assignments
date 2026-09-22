from models import Product

p1 = Product(101, "Laptop", 55000, 5)
p2 = Product(102, "Mouse", 800, 25)
p3 = Product(103, "Keyboard", 1500, 12)
p4 = Product(104, "Monitor", 12000, 7)
p5 = Product(105, "Printer", 9000, 15)

products = [p1, p2, p3, p4, p5]

while True:
    print("""
1. Display all products.
2. Display total value of each product.
3. Display low stock products.
4. Find product having highest price.
5. Calculate total inventory value.
6. Search product using Product ID.
7. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Product Information ----")
        print()

        for prod in products:
            prod.display()

    elif n == 2:
        print("---- Product Total Values ----")
        print()

        for prod in products:
            print(f"{prod.product_name:15} = {prod.total_value()}")

    elif n == 3:
        print("---- Low Stock Products ----")
        print()

        for prod in products:
            if prod.quantity < 10:
                print(prod.product_name)

    elif n == 4:
        highest = 0
        prodId = None

        for prod in products:
            if prod.price > highest:
                highest = prod.price
                prodId = prod.product_id

        for prod in products:
            if prod.product_id == prodId:
                print("---- Highest Price Product ----")
                print(f"{prod.product_name} = {prod.price}")
                break

    elif n == 5:
        total = 0

        for prod in products:
            total += prod.total_value()

        print("Total Inventory Value:", total)

    elif n == 6:
        prodId = int(input("Enter Product ID: "))

        for prod in products:
            if prod.product_id == prodId:
                print("---- Product Found ----")
                prod.display()
                break
        else:
            print("[ Product Not Found ]")

    elif n == 7:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue