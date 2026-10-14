a,b = map(int, input("Input: ").split(","))

if a<b:
    while a <= b:
        print(a, end = " ")
        a = a+1
elif a>b:
    while a >= b:
        print(a, end = " ")
        a = a-1
else:
    print("Both numbers are same")