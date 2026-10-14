'''
    x
   xx
  x_x
 x__x
xxxxx

'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end ="")
    for j in range(1,i+1):
        if i<n and i>1 and j<i and j>1:
            print("_",end = "")
        else:
            print("x",end ="")
    print() 