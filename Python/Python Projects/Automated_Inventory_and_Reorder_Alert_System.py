# Initializing the empty slots for stock 

s1_status = False
s1_id = ""
s1_name = ""
s1_stock = 0
s1_min = 0
s1_max = 0
s1_cp = 0.0
s1_sp = 0.0

#--------------------------------

s2_status = False
s2_id = ""
s2_name = ""
s2_stock = 0
s2_min = 0
s2_max = 0
s2_cp = 0.0
s2_sp = 0.0

#--------------------------------


s3_status = False
s3_id = ""
s3_name = ""
s3_stock = 0
s3_min = 0
s3_max = 0
s3_cp = 0.0
s3_sp = 0.0

#--------------------------------

s4_status = False
s4_id = ""
s4_name = ""
s4_stock = 0
s4_min = 0
s4_max = 0
s4_cp = 0.0
s4_sp = 0.0

#--------------------------------

s5_status = False
s5_id = ""
s5_name = ""
s5_stock = 0
s5_min = 0
s5_max = 0
s5_cp = 0.0
s5_sp = 0.0

total_revenue = 0.0
total_expenses = 0.0
total_opex = 0.0

#-------------------- Authentication System ---------
print("================== Register a new User =========================")

username = input("Enter your Username: ")
password = input("Make a Strong Password: ")

access_allowed = False
attempts = 3
print("========================== Login ===============================")

while attempts > 0:
     
    login_username = input("Enter Username : ")
    login_password = input("Enter Your Password: ")

    if login_username == username:
        if login_password == password:
            print("Login Successfull !!!")
            access_allowed = True
            break
        else:
            print("Incorrect Password. Please Enter a valid Password.")
            print(f" You have {attempts-1} attempts left.")
            attempts -= 1
    else:
        print("Incorrect Username !!!")
        print("Try Again...")    


#-------------------- Program Runner ----------------
if access_allowed:
    while True:
        print("================================================================")
        print("||                           DASHBOARD                         ||")
        print("================================================================")
        print("1. -> Register New Product")
        print("2. -> View Live Inventory")
        print("3. -> Log Product Sale")
        print("4. -> Check Reorder Alerts")
        print("5. -> Taxation and Operating Expenses ")
        print("6. -> Discontinue Product")
        print("7. -> Exit System")

        print()
        choice = int(input("Choose an option from above (1-7) : "))
        print()
        print()

        match choice:
            case 1:
                print("================================================================")
                print("||                    REGISTER A NEW PRODUCT                  ||")
                print("================================================================")
                print()
                
                if s1_status == False:
                    s1_id = input("Enter id of product: ")
                    s1_name = input("Enter the name of the product: ")
                    s1_cp = float(input("Enter the cost price of the product: "))
                    s1_sp = float(input("Enter the selling price of the product: "))
                    s1_stock = int(input("Enter the stock quantity: "))
                    s1_min = int(input("Enter minimum stock quantity: "))
                    s1_max = int(input("Enter maximum stock quantity: "))

                    s1_status = True

                elif s2_status == False:
                    s2_id = input("Enter id of product: ")
                    s2_name = input("Enter the name of the product: ")
                    s2_cp = float(input("Enter the cost price of the product: "))
                    s2_sp = float(input("Enter the selling price of the product: "))
                    s2_stock = int(input("Enter the stock quantity: "))
                    s2_min = int(input("Enter minimum stock quantity: "))
                    s2_max = int(input("Enter maximum stock quantity: "))

                    s2_status = True

                elif s3_status == False:
                    s3_id = input("Enter id of product: ")
                    s3_name = input("Enter the name of the product: ")
                    s3_cp = float(input("Enter the cost price of the product: "))
                    s3_sp = float(input("Enter the selling price of the product: "))
                    s3_stock = int(input("Enter the stock quantity: "))
                    s3_min = int(input("Enter minimum stock quantity: "))
                    s3_max = int(input("Enter maximum stock quantity: "))

                    s3_status = True

                elif s4_status == False:
                    s4_id = input("Enter id of product: ")
                    s4_name = input("Enter the name of the product: ")
                    s4_cp = float(input("Enter the cost price of the product: "))
                    s4_sp = float(input("Enter the selling price of the product: "))
                    s4_stock = int(input("Enter the stock quantity: "))
                    s4_min = int(input("Enter minimum stock quantity: "))
                    s4_max = int(input("Enter maximum stock quantity: "))

                    s4_status = True

                elif s5_status == False:
                    s5_id = input("Enter id of product: ")
                    s5_name = input("Enter the name of the product: ")
                    s5_cp = float(input("Enter the cost price of the product: "))
                    s5_sp = float(input("Enter the selling price of the product: "))
                    s5_stock = int(input("Enter the stock quantity: "))
                    s5_min = int(input("Enter minimum stock quantity: "))
                    s5_max = int(input("Enter maximum stock quantity: "))

                    s5_status = True
                
                else:
                    print("Insufficient Space , Create new slots.")
                    print("Navigating to Menu")
                    continue
                print()
                print("================ PRODUCT REGISTERED SUCCESSFULLY =====================")

            case 2:
                print("================================================================")
                print("||                     Current Live Inventory                  ||")
                print("================================================================")
                print()
                print()

                
                if s1_status is False and s2_status is False and s3_status is False and s4_status is False and s5_status is False:
                    print("         ----------------------------                  ")
                    print("        |  INVENTORY IS EMPTY        |                 ")
                    print("        |  REGISTER A PRODUCT FIRST  |                 ")
                    print("         ----------------------------                  ")
                    continue
                
                else:
                    if s1_status is True:
                        print(f"    ID: {s1_id} | Name: {s1_name} | Stock: {s1_stock}/{s1_max} ")
                        print(f"    Cost Price: ₹{s1_cp:.2f} | Selling Price: ₹{s1_sp:.2f}")
                        print(f"    Safety Threshold: {s1_min}")
                        print("-------------------------------------------------------------")

                    if s2_status is True:
                        print(f"    ID: {s2_id} | Name: {s2_name} | Stock: {s2_stock}/{s2_max} ")
                        print(f"    Cost Price: ₹{s2_cp:.2f} | Selling Price: ₹{s2_sp:.2f}")
                        print(f"    Safety Threshold: {s2_min}")
                        print("-------------------------------------------------------------")

                    if s3_status is True:
                        print(f"    ID: {s3_id} | Name: {s3_name} | Stock: {s3_stock}/{s3_max}  ")
                        print(f"    Cost Price: ₹{s3_cp:.2f} | Selling Price: ₹{s3_sp:.2f}")
                        print(f"    Safety Threshold: {s3_min}")
                        print("-------------------------------------------------------------")

                    if s4_status is True:
                        print(f"    ID: {s4_id} | Name: {s4_name} | Stock: {s4_stock}/{s4_max} ")
                        print(f"    Cost Price: ₹{s4_cp:.2f} | Selling Price: ₹{s4_sp:.2f}")
                        print(f"    Safety Threshold: {s4_min}")
                        print("-------------------------------------------------------------")

                    if s2_status is True:
                        print(f"    ID: {s5_id} | Name: {s5_name} | Stock: {s5_stock}/{s5_max} ")
                        print(f"    Cost Price: ₹{s1_cp:.2f} | Selling Price: ₹{s1_sp:.2f}")
                        print(f"    Safety Threshold: {s5_min}")
                        print("-------------------------------------------------------------")

                    print("================================================================")
                    print("||                      FINANCIAL PERFORMANCE                  ||")
                    print("================================================================")

                    print()
                    print(f"Total Sales Revenue: ₹{total_revenue:.2f}")
                    print(f"Total Restock Expenses: ₹{total_expenses:.2f}")
                    print()

                    net_profit = total_revenue - total_expenses
                    if net_profit >= 0:
                        print(f"Net Profit: ₹{net_profit:.2f}")
                    else:
                        net_loss = abs(net_profit)
                        print(f"Net Loss: ₹{net_loss:.2f}")

                    print("================================================================")

                
            case 3:
                print("================================================================")
                print("||                       LOG PRODUCT SALE                     ||")
                print("================================================================")
                print()
                print()

                productId = input("Enter Product id: ")
                quantity = int(input("Enter quantities sold: "))

                match productId:
                    case _ if productId == s1_id and s1_status is True:
                        revenue_earned = 0
                        if s1_stock >= quantity:
                            
                            s1_stock = s1_stock - quantity
                            revenue_earned = quantity*s1_sp
                            total_revenue = total_revenue + revenue_earned

                            print()
                            print("-------------------------------------------------------------")
                            print(f"[SALE Success] SOLD {quantity} units of {s1_name}.")
                            print(f"Transaction Value: ₹{revenue_earned:.2f} | Total Revenue Earned: ₹{total_revenue:.2f}")
                            print("-------------------------------------------------------------")

                        else:
                            print()
                            print("-------------------------------------------------------------")
                            print(f"[TRANSACTION DENIED] Insufficient stock! Only {s1_stock} units available.")
                            print("-------------------------------------------------------------")

                    case _ if productId == s2_id and s2_status is True:
                        revenue_earned = 0
                        if s2_stock >= quantity:
                            s2_stock = s2_stock - quantity
                            revenue_earned = quantity*s2_sp
                            total_revenue = total_revenue + revenue_earned

                            print()
                            print("-------------------------------------------------------------")
                            print(f"[SALE Success] SOLD {quantity} units of {s2_name}.")
                            print(f"Transaction Value: ₹{revenue_earned:.2f} | Total Revenue Earned: ₹{total_revenue:.2f}")
                            print("-------------------------------------------------------------")

                        else:
                            print()
                            print("-------------------------------------------------------------")
                            print(f"[TRANSACTION DENIED] Insufficient stock! Only {s2_stock} units available.")
                            print("-------------------------------------------------------------")

                    case _ if productId == s3_id and s3_status is True:
                        revenue_earned = 0
                        if s3_stock >= quantity:
                            s3_stock = s3_stock - quantity
                            revenue_earned = quantity*s3_sp                            
                            total_revenue = total_revenue + revenue_earned

                            print()
                            print("-------------------------------------------------------------")
                            print(f"[SALE Success] SOLD {quantity} units of {s3_name}.")
                            print(f"Transaction Value: ₹{revenue_earned:.2f} | Total Revenue Earned: ₹{total_revenue:.2f}")
                            print("-------------------------------------------------------------")

                        else:
                            print()
                            print("-------------------------------------------------------------")
                            print(f"[TRANSACTION DENIED] Insufficient stock! Only {s3_stock} units available.")
                            print("-------------------------------------------------------------")

                    case _ if productId == s4_id and s4_status is True:
                        revenue_earned = 0
                        if s4_stock >= quantity:
                            s4_stock = s4_stock - quantity
                            revenue_earned = quantity*s4_sp
                            total_revenue = total_revenue + revenue_earned

                            print()
                            print("-------------------------------------------------------------")
                            print(f"[SALE Success] SOLD {quantity} units of {s4_name}.")
                            print(f"Transaction Value: ₹{revenue_earned:.2f} | Total Revenue Earned: ₹{total_revenue:.2f}")
                            print("-------------------------------------------------------------")

                        else:
                            print()
                            print("-------------------------------------------------------------")
                            print(f"[TRANSACTION DENIED] Insufficient stock! Only {s4_stock} units available.")
                            print("-------------------------------------------------------------")

                    case _ if productId == s5_id and s5_status is True:
                        revenue_earned = 0
                        if s5_stock >= quantity:
                            s5_stock = s5_stock - quantity
                            revenue_earned = quantity*s5_sp
                            total_revenue = total_revenue + revenue_earned

                            print()
                            print("-------------------------------------------------------------")
                            print(f"[SALE Success] SOLD {quantity} units of {s5_name}.")
                            print(f"Transaction Value: ₹{revenue_earned:.2f} | Total Revenue Earned: ₹{total_revenue:.2f}")
                            print("-------------------------------------------------------------")

                        else:
                            print()
                            print("-------------------------------------------------------------")
                            print(f"[TRANSACTION DENIED] Insufficient stock! Only {s5_stock} units available.")
                            print("-------------------------------------------------------------")

                    case __:
                        print()
                        print("[ERROR] Active Product ID not found in stock. ")

            case 4:
                print()
                print("================================================================")
                print("||                 Check Reorder Alerts                        ||")
                print("================================================================")
                print()


                any_alerts = False

                if s1_status is True and s1_stock <= s1_min:
                    any_alerts = True

                    max_allowed_space = s1_max - s1_stock
                    print()
                    print(f"\n[ALERT] {s1_name} (ID: {s1_id}) is low !")
                    print(f"Current Stock: {s1_stock}/{s1_max} | Safety Limit: {s1_min}")
                    print(f"You can restock a maximum of up to {max_allowed_space} units.")

                    confirm = input(f"Do you want to restock {s1_name}? (y/n): ").lower()

                    if confirm == "yes" or confirm == "y":
                        qty_to_restock = int(input(f"Enter number of units to order for {s1_name}: "))

                        if qty_to_restock <= max_allowed_space:
                            order_cost = qty_to_restock * s1_cp
                            current_capital = total_revenue - total_expenses
                            
                            if order_cost <= current_capital:
                                total_expenses = total_expenses + order_cost
                                s1_stock = s1_stock + qty_to_restock

                                print(f"[SUCCESS] Ordered {qty_to_restock} units. Restocking Cost Charge: ₹{order_cost:.2f}")
                                print(f"New Stock Status: {s1_stock}/{s1_max}")
                            else:
                                print(f"[ERROR] Transaction Denied! Insufficient Funds.")
                                print(f"Order Cost: ₹{order_cost:.2f} | Your Available Capital: ₹{current_capital:.2f}")
                                print(f"Please Generate more revenue to buy this stock !")

                        else:
                            print(f"[ERROR] Transection Denied! Entering {qty_to_restock} units would exceed max capacity.")

                        ask = input("Do you want to see restocking alert for next product? (y/n): ").lower()

                        if ask == "yes" or ask == "y":
                            pass
                        else:
                            print("No Product for restocking")
                            print("----------------------------------------------------------")
                            continue

                if s2_status is True and s2_stock <= s2_min:
                    any_alerts = True

                    max_allowed_space = s2_max - s2_stock
                    print()
                    print(f"\n[ALERT] {s2_name} (ID: {s2_id}) is low !")
                    print(f"Current Stock: {s2_stock}/{s2_max} | Safety Limit: {s2_min}")
                    print(f"You can restock a maximum of up to {max_allowed_space} units.")

                    confirm = input(f"Do you want to restock {s2_name}? (y/n): ").lower()

                    if confirm == "yes" or confirm == "y":
                        qty_to_restock = int(input(f"Enter number of units to order for {s2_name}: "))

                        if qty_to_restock <= max_allowed_space:
                            order_cost = qty_to_restock * s2_cp
                            current_capital = total_revenue - total_expenses
                            
                            if order_cost <= current_capital:
                                total_expenses = total_expenses + order_cost
                                s2_stock = s2_stock + qty_to_restock

                                print(f"[SUCCESS] Ordered {qty_to_restock} units. Restocking Cost Charge: ₹{order_cost:.2f}")
                                print(f"New Stock Status: {s2_stock}/{s2_max}")
                            else:
                                print(f"[ERROR] Transaction Denied! Insufficient Funds.")
                                print(f"Order Cost: ₹{order_cost:.2f} | Your Available Capital: ₹{current_capital:.2f}")
                                print(f"Please Generate more revenue to buy this stock !")

                        else:
                            print(f"[ERROR] Transection Denied! Entering {qty_to_restock} units would exceed max capacity.")

                        ask = input("Do you want to see restocking alert for next product? (y/n): ").lower()

                        if ask == "yes" or ask == "y":
                            pass
                        else:
                            continue
                
                if s3_status is True and s3_stock <= s3_min:
                    any_alerts = True

                    max_allowed_space = s3_max - s3_stock
                    print()
                    print(f"\n[ALERT] {s3_name} (ID: {s3_id}) is low !")
                    print(f"Current Stock: {s3_stock}/{s3_max} | Safety Limit: {s3_min}")
                    print(f"You can restock a maximum of up to {max_allowed_space} units.")

                    confirm = input(f"Do you want to restock {s3_name}? (y/n): ").lower()

                    if confirm == "yes" or confirm == "y":
                        qty_to_restock = int(input(f"Enter number of units to order for {s3_name}: "))

                        if qty_to_restock <= max_allowed_space:
                            order_cost = qty_to_restock * s3_cp
                            current_capital = total_revenue - total_expenses
                            
                            if order_cost <= current_capital:
                                total_expenses = total_expenses + order_cost
                                s3_stock = s3_stock + qty_to_restock

                                print(f"[SUCCESS] Ordered {qty_to_restock} units. Restocking Cost Charge: ₹{order_cost:.2f}")
                                print(f"New Stock Status: {s3_stock}/{s3_max}")
                            else:
                                print(f"[ERROR] Transaction Denied! Insufficient Funds.")
                                print(f"Order Cost: ₹{order_cost:.2f} | Your Available Capital: ₹{current_capital:.2f}")
                                print(f"Please Generate more revenue to buy this stock !")

                        else:
                            print(f"[ERROR] Transection Denied! Entering {qty_to_restock} units would exceed max capacity.")

                        ask = input("Do you want to see restocking alert for next product? (y/n): ").lower()

                        if ask == "yes" or ask == "y":
                            pass
                        else:
                            continue
                
                if s4_status is True and s4_stock <= s4_min:
                    any_alerts = True

                    max_allowed_space = s4_max - s4_stock
                    print()
                    print(f"\n[ALERT] {s4_name} (ID: {s4_id}) is low !")
                    print(f"Current Stock: {s4_stock}/{s4_max} | Safety Limit: {s4_min}")
                    print(f"You can restock a maximum of up to {max_allowed_space} units.")

                    confirm = input(f"Do you want to restock {s4_name}? (y/n): ").lower()

                    if confirm == "yes" or confirm == "y":
                        qty_to_restock = int(input(f"Enter number of units to order for {s4_name}: "))

                        if qty_to_restock <= max_allowed_space:
                            order_cost = qty_to_restock * s4_cp
                            current_capital = total_revenue - total_expenses
                            
                            if order_cost <= current_capital:
                                total_expenses = total_expenses + order_cost
                                s4_stock = s4_stock + qty_to_restock

                                print(f"[SUCCESS] Ordered {qty_to_restock} units. Restocking Cost Charge: ₹{order_cost:.2f}")
                                print(f"New Stock Status: {s4_stock}/{s4_max}")
                            else:
                                print(f"[ERROR] Transaction Denied! Insufficient Funds.")
                                print(f"Order Cost: ₹{order_cost:.2f} | Your Available Capital: ₹{current_capital:.2f}")
                                print(f"Please Generate more revenue to buy this stock !")

                        else:
                            print(f"[ERROR] Transection Denied! Entering {qty_to_restock} units would exceed max capacity.")

                        ask = input("Do you want to see restocking alert for next product? (y/n): ").lower()

                        if ask == "yes" or ask == "y":
                            pass
                        else:
                            continue

                if s5_status is True and s5_stock <= s5_min:
                    any_alerts = True

                    max_allowed_space = s5_max - s5_stock
                    print()
                    print(f"\n[ALERT] {s5_name} (ID: {s5_id}) is low !")
                    print(f"Current Stock: {s5_stock}/{s5_max} | Safety Limit: {s5_min}")
                    print(f"You can restock a maximum of up to {max_allowed_space} units.")

                    confirm = input(f"Do you want to restock {s5_name}? (y/n): ").lower()

                    if confirm == "yes" or confirm == "y":
                        qty_to_restock = int(input(f"Enter number of units to order for {s5_name}: "))

                        if qty_to_restock <= max_allowed_space:
                            order_cost = qty_to_restock * s5_cp
                            current_capital = total_revenue - total_expenses
                            
                            if order_cost <= current_capital:
                                total_expenses = total_expenses + order_cost
                                s5_stock = s5_stock + qty_to_restock

                                print(f"[SUCCESS] Ordered {qty_to_restock} units. Restocking Cost Charge: ₹{order_cost:.2f}")
                                print(f"New Stock Status: {s5_stock}/{s5_max}")
                            else:
                                print(f"[ERROR] Transaction Denied! Insufficient Funds.")
                                print(f"Order Cost: ₹{order_cost:.2f} | Your Available Capital: ₹{current_capital:.2f}")
                                print(f"Please Generate more revenue to buy this stock !")

                        else:
                            print(f"[ERROR] Transection Denied! Entering {qty_to_restock} units would exceed max capacity.")

                        ask = input("Do you want to see restocking alert for next product? (y/n): ").lower()

                        if ask == "yes" or ask == "y":
                            pass
                        else:
                            continue

                if any_alerts is False:
                    print("[System Check] All active products are safely above minimum thresholds !!")

            case 5:
                print()
                print("================================================================")
                print("||                 TAXATION & OPERATING EXPENSE DESK          ||")
                print("================================================================")

                print()
                print("Select an option: ")
                print()
                print("1. Log Operating Expenses (e.g.,Rent,Electricity).")
                print("2.View live GST & tax Liability Report.")

                print()
                fin_choice = int(input("Input : "))

                if fin_choice == 1:
                    print("\n ------ LOG OPERATING EXPENSES -----")
                    expense_name = input("Enter Expense Name(e.g.,Rent,Electricity): ")
                    expense_amount = float(input(f"Enter Amount for {expense_name}: ₹"))

                    current_capital = total_revenue - total_expenses - total_opex

                    if expense_amount <= current_capital:
                        total_opex = total_opex + expense_amount
                        print(f"[SUCCESS] Recorded ₹{expense_amount:.2f} for {expense_name}.")
                    else:
                        print(f"[DENIED] Insufficient funds to pay this bill! Capital: ₹{current_capital:.2f}")

                elif fin_choice == 2:
                    gst_owed = total_revenue * 0.18
                    gross_profit = total_revenue - total_expenses
                    net_profit = gross_profit - gst_owed - total_opex

                    print("\n================================================================")
                    print("||                 OFFICIAL TAX & PROFIT REPORT                ||")
                    print("================================================================")
                    print(f"Total Sales Revenue (Gross):   ₹{total_revenue:.2f}")
                    print(f"Total Cost of Goods (Stock):  -₹{total_expenses:.2f}")
                    print("-----------------------------------------------------------------")
                    print(f"Gross Profit:                  ₹{gross_profit:.2f}")
                    print(f"GST Liability (18% on sales): -₹{gst_owed:.2f}")
                    print(f"Operating Expenses (OpEx):    -₹{total_opex:.2f}")
                    print("-----------------------------------------------------------------")
                    print(f"NET PROFIT (After Tax & OpEx): ₹{net_profit:.2f}") 
                    print("================================================================")            

                else:
                    print("[ERROR] Invalid Choice")

            case 6:
                print("\n================================================================")
                print("||                 PRODUCT DISCONTINUATION DESK                ||")
                print("================================================================")

                print()
                search_id = input("Enter the Product ID you want to Discontinue: ")

                match search_id:
                    case _ if search_id == s1_id and s1_status is True:
                        print(f"\nProduct Found: {s1_name} occupies Warehouse Slot 1.")

                        if s1_stock == 0:
                            confirm = input(f"Are you sure you want to permanently dicontinue {s1_name}? (y/n): ").lower()

                            if confirm == "y" or confirm == "yes":
                                s1_status = False
                                s1_id = ""
                                s1_name = ""
                                s1_stock = 0
                                s1_min = 0
                                s1_max = 0
                                s1_cp = 0.0
                                s1_sp = 0.0

                                print(f"\n[SUCCESS] {s1_name} has beem discontinued. Slot is now vacant.")
                            else:
                                print("[CANCELLED] Discontinuation aborted.")

                        else:
                            print(f"\n[DENIED] Cannot Discontinue {s1_name} yet!")
                            print(f"You still have {s1_stock} units left on the shelf. Sell them out first !!")

                    case _ if search_id == s2_id and s2_status is True:
                        print(f"\nProduct Found: {s2_name} occupies Warehouse Slot 1.")

                        if s2_stock == 0:
                            confirm = input(f"Are you sure you want to permanently dicontinue {s2_name}? (y/n): ").lower()

                            if confirm == "y" or confirm == "yes":
                                s2_status = False
                                s2_id = ""
                                s2_name = ""
                                s2_stock = 0
                                s2_min = 0
                                s2_max = 0
                                s2_cp = 0.0
                                s2_sp = 0.0

                                print(f"\n[SUCCESS] {s2_name} has beem discontinued. Slot is now vacant.")
                            else:
                                print("[CANCELLED] Discontinuation aborted.")

                        else:
                            print(f"\n[DENIED] Cannot Discontinue {s2_name} yet!")
                            print(f"You still have {s2_stock} units left on the shelf. Sell them out first !!")

                    case _ if search_id == s3_id and s3_status is True:
                        print(f"\nProduct Found: {s3_name} occupies Warehouse Slot 1.")

                        if s3_stock == 0:
                            confirm = input(f"Are you sure you want to permanently dicontinue {s3_name}? (y/n): ").lower()

                            if confirm == "y" or confirm == "yes":
                                s3_status = False
                                s3_id = ""
                                s3_name = ""
                                s3_stock = 0
                                s3_min = 0
                                s3_max = 0
                                s3_cp = 0.0
                                s3_sp = 0.0

                                print(f"\n[SUCCESS] {s3_name} has beem discontinued. Slot is now vacant.")
                            else:
                                print("[CANCELLED] Discontinuation aborted.")

                        else:
                            print(f"\n[DENIED] Cannot Discontinue {s3_name} yet!")
                            print(f"You still have {s3_stock} units left on the shelf. Sell them out first !!")

                    case _ if search_id == s4_id and s4_status is True:
                        print(f"\nProduct Found: {s4_name} occupies Warehouse Slot 1.")

                        if s4_stock == 0:
                            confirm = input(f"Are you sure you want to permanently dicontinue {s4_name}? (y/n): ").lower()

                            if confirm == "y" or confirm == "yes":
                                s4_status = False
                                s4_id = ""
                                s4_name = ""
                                s4_stock = 0
                                s4_min = 0
                                s4_max = 0
                                s4_cp = 0.0
                                s4_sp = 0.0

                                print(f"\n[SUCCESS] {s4_name} has beem discontinued. Slot is now vacant.")
                            else:
                                print("[CANCELLED] Discontinuation aborted.")

                        else:
                            print(f"\n[DENIED] Cannot Discontinue {s4_name} yet!")
                            print(f"You still have {s4_stock} units left on the shelf. Sell them out first !!")

                    case _ if search_id == s5_id and s5_status is True:
                        print(f"\nProduct Found: {s5_name} occupies Warehouse Slot 1.")

                        if s5_stock == 0:
                            confirm = input(f"Are you sure you want to permanently dicontinue {s5_name}? (y/n): ").lower()

                            if confirm == "y" or confirm == "yes":
                                s5_status = False
                                s5_id = ""
                                s5_name = ""
                                s5_stock = 0
                                s5_min = 0
                                s5_max = 0
                                s5_cp = 0.0
                                s5_sp = 0.0

                                print(f"\n[SUCCESS] {s5_name} has beem discontinued. Slot is now vacant.")
                            else:
                                print("[CANCELLED] Discontinuation aborted.")

                        else:
                            print(f"\n[DENIED] Cannot Discontinue {s5_name} yet!")
                            print(f"You still have {s5_stock} units left on the shelf. Sell them out first !!")

                    case _:
                        print(f"\n[ERROR] Product ID '{search_id}' is not currently active in the warehose.")

            case 7:
                print("Exiting Inventory Management System !!!")
                break

            case __:
                print("Invalid Choice! Please enter a valid choice ranging from 1 to 7.")
        
        print("----------------------------------------------------------------------")
        print()
        print("1. -> Nevigate to Dashboard")
        print("2. -> Exit System")
        print()
        final_ask = int(input("Select an option from above: "))

        match final_ask:
            case 1:
                continue
            case 2:
                print("Exiting Inventory Management System !!!")
                break
            case _:
                print("Invalid Choice")
                continue

else:
    print("Access Blocked.")
    print("No more Attempts.")

