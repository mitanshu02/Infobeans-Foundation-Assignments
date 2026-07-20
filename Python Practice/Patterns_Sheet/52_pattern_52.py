'''
12345
 1__4
  1_3
   12
    1
'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end = "")
    for j in range(1,n-i+2):
        if i == 1 or j == 1 or j == n-i+1:
            print(j,end = "")
        else:
            print("_",end = "")
    print()

