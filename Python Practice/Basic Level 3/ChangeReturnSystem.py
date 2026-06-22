amount = int(input("Enter amount: ₹"))
Notes100 = amount//100
remFrom100 = amount - (100 * Notes100)

Notes50 = remFrom100//50
remFrom50 = remFrom100 - (50 * Notes50)

Notes10 = remFrom50//10
 
print(f"₹100 x {Notes100}")
print(f"₹50 x {Notes50}")
print(f"₹10 x {Notes10}")