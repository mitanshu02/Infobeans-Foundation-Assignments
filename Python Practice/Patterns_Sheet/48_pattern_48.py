'''
    A
   AB
  A_C
 A__D
ABCDE

'''

n= int(input("Enter n: "))

for i in range(1, n+1):
    c = 65
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            if j == n or i == n or j == n-i+1:
                print(chr(c),end ="")
            else:
                print("_",end = "")
            c += 1            
    print()