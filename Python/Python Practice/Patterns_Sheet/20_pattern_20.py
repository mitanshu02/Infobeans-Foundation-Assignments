'''
1
12
1 3
1  4
12345

'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(j, end = "")
        else:
            print(" ", end ="")
    print()