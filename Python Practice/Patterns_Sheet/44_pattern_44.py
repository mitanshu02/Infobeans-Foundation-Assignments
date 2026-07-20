'''
    1
   22
  333
 4444
55555
'''
n = int(input("Enter n: "))

for i in range(1, n+1):
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            print(i,end ="")
    print()