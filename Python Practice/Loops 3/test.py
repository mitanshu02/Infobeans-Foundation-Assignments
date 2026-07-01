n = int(input("Input a Number: "))
sq = n**2

while n>0:
    if n%10 == sq%10:
        n = n//10
        sq = sq//10
        continue
    else:
        print("Not an Automorphic Number")
        break
else:
    print("Automorphic Number")
