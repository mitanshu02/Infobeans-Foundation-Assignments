def displayCustomer(name,email,mob):
    print()
    print("------ CUSTOMER REGISTERATION -------")
    print()
    print(f"Customer Name  : {name}")
    print(f"Customer email : {email}")
    print(f"Mobile Number  : {mob}")
    print()
    print("Customer Registered Successfully.")
    

def displayProduct(p_name,p_price,p_category):
    print()
    print("----- PRODUCT INFORMATION -----")
    print()
    print(f"Product Name     : {p_name}")
    print(f"Product Price    : {p_price}")
    print(f"Product Category : {p_category}")
    print()
    print("Product Displayed Successfully.")

def generateInvoice(p_name,p_price,tax = 10):
    tax = p_price*(tax/100)
    print()
    print("----------- INVOICE -----------")
    print()
    print(f"Product Name : {p_name}")
    print(f"Product Price : {p_price}")
    print(f"Tax Percentage : {tax}%")
    print(f"Tax Amount : {tax}")
    print(f"Final Amount : {p_price + tax}")
    print()
    print("Invoice Generated Successfully.")

def totalBill(*prices):
    print()
    print(f"Total Bill Amount : {sum(prices)}")

def displayProfile(**details):
    print("------- Customer Details --------")
    print()
    for f,v in details.items():
        print(f," : ",v)


while True:
    print()
    print("MENU")
    print("""
1. Customer Registration
2. Product Information
3. Generate Invoice
4. Add Multiple Products
5. Display Customer Profile
6. Exit
""")


    n = int(input("Select an Option: "))
    print()
    
    match n:
        case 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            mobile = int(input("Enter mobile number: "))
            print()
            displayCustomer(name,email,mobile)
        case 2:
            name = input("Enter Product Name : ")
            price = int(input("Enter Product Price : "))
            category = input("Enter product Category : ")
            print()
            displayProduct(p_name = name,p_price = price,p_category = category)

        case 3:
            name = input("Enter Product Name : ")
            price = int(input("Enter product Price : "))
            print()
            generateInvoice(name,price)
        case 4:
            p = []
            n = int(input("Enter how many prices : "))
            for i in range(n):
                p.append(int(input(f"Enter Price of product {i+1} : ")))
            
            totalBill(*p)
        case 5:
            name = input("Enter name : ")
            city = input("Enter City : ")
            mail = input("Enter E-mail: ")
            mob = int(input("Enter mobile number : "))
            memb = input("Enter Membership Type : ")
  
            details = {"Name":name,"City":city,"Mail":mail,"Mobile Number":mob,"Membership Type":memb}
            print()
            displayProfile(**details)
        case 6:
            print()
            print("===================================")
            print("         Program Terminated        ")
            print("===================================")
            break
        case __:
            continue


    
    
    
    

