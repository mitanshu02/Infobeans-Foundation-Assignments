'''
    5
   44
  333
 2222
11111
'''


n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            print(n-i+1,end ="")
    print()