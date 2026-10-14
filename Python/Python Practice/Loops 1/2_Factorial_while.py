n = int(input("n = "))
fact = 1

while n>0:
    fact*=n
    n-=1

print("Total Ways =",fact)