'''
a
bc
d f
g  j
klmno

'''

n = int(input("Enter n: "))
k = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(97 + k), end = "")
        else:
            print(" ", end ="")
        k += 1
    print()