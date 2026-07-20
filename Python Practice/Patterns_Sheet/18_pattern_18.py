'''
1
10
101
1010
10101

'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2 != 0:
            print("1",end = "")
        else:
            print("0",end = "")
    print()