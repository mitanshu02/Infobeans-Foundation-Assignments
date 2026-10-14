'''
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)

'''
products = []

n = int(input("Enter no. of products you want to enter: "))

for i in range(n):
    print(f"Enter details of product {i+1}")
    product_id = input("Enter product id: ")
    product_name = input("Enter product name: ")
    price = int(input("Enter price: "))
     
    products.append((product_id,product_name,price))
    print()

print("All Products: ")
for p in products:
    print(p)

total = 0
costliest = products[0][2]
h_idx = 0
cheapest = float("inf")
l_idx = 0

for i in range(n):
    total = total + products[i][2]
    
    if products[i][2] > costliest:
        costliest = products[i][2]
        h_idx = i
    
    if products[i][2] < cheapest:
        cheapest = products[i][2]
        l_idx = i

print()
print("Costliest Product: ")
print(products[h_idx])

print()

print("Cheapest product: ")
print(products[l_idx])

print()

print("Average Price: ")
print(total/n)

print()

print("Products above ₹50,000: ")
for p in products:
    if p[2] > 50000:
        print(p) 
