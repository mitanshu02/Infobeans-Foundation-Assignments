'''
    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end ="")
    for j in range(1,2*i):
        print("*",end="")
    print()



























'''
for i in range(1,n+1):
    for j in range(1,2*n):
        if j<=n-i:
            print(" ",end ="")
        elif n-i<j<

'''