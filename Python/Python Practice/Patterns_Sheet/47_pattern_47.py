'''
    1
   11
  1*1
 1**1
11111

'''
n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            if j == n or i == n or j == n-i+1:
                print("1",end ="")
            else:
                print("*",end = "")
    print()