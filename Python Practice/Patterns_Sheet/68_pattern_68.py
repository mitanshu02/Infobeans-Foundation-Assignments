'''
    #
   *#*
  **#**
 ***#***
****#****

'''
n = int(input("Enter n: "))

for i in range(n):
    for j in range(n-i):
        print(" ",end = "")
    for j in range(1,2*i + 2):
        if j == i+1:
            print("#",end ="")
        else:
            print("*",end = "")
    print()
        


