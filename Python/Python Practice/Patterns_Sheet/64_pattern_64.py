'''
    * 
   *_*
  *___*
 *_____*
*********

'''
n = int(input("Enter n:"))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end = "")

    for j in range(1,2*i):
        if i < n:
            if j == 1 or j == (2*i) - 1:
                print("*",end ="")
            else:
                print("_",end = "")
        else:
            print("*",end = "")
    print()
