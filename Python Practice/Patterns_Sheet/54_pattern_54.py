'''
ABCDE
 A__D
  A_C
   AB
    A
'''
n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end ="")
    for j in range(1,n-i+2):
        if i>1 and i< n and j<n-i+1 and j>1:
            print("_",end = "")
        else:
            print(chr(64+j),end ="")
    print()
  	


    
