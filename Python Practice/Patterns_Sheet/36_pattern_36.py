'''
ABCDE
A  D
A C
AB
A

'''
n = int(input("Enter n: "))

for i in range(n,0,-1):
    for j in range(1,i+1):
        if i == n or j==1 or j==i:
            print(chr(64+j), end = "")
        else:
            print(" ", end = "")
    print()