'''
*****



'''

n = int(input("Enter n: "))

for i in range(n):
    for j in range(n):
        if i == 0:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()