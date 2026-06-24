units = int(input("Enter units consumed: "))

if units <= 100 :
    amount = units * 5
elif units <= 200 : 
    amount = (100 * 5) + ((units-100)*7)
else:
    amount = (100 * 5) + (100 * 7) + ((units - 200)* 10)

print("Total Electricity Bill: ₹", amount)
