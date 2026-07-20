'''
0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
'''
n = int(input("Enter n:"))
for i in range(1,n):
    for j in range(i):
        print(j,end = " ")
    print()