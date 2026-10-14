print(chr(65))
'''
A
AB
A C
A  D
ABCDE

'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(64 + j), end = "")
        else:
            print(" ", end ="")
    print()