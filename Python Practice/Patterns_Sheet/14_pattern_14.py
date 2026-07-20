'''
1
23
456
78910
'''

n = int(input("Enter n: "))
k = 1

for i in range(0,n):
    for j in range(0,i):
        print(k,end = "")
        k += 1
    print()