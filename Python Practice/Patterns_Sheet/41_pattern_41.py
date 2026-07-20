'''
A
BCD
EFGHI
JKLMNOP

'''
n = int(input("Enter n: "))
p = 65
for i in range(1,n+1):
    for j in range(1,2*i):
        print(chr(p),end ="")
        p = p+1
    print()