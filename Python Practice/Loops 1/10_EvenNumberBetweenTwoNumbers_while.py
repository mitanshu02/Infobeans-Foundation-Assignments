a,b = map(int,input("Input: ").split(","))

if a%2 == 0:
    while(a < b):
        if a%2 == 0:
            print(a, end = " ")
    a =