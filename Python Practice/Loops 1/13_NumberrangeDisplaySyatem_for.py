a,b = map(int, input("Input: ").split(","))

if a<b:
    for i in range(a,b+1):
        print(i, end = " ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i, end = " ")
else:
    print("Both numbers are same")