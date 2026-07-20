'''
55555
 4444
  333 
   22
    1

'''

n = int(input("Enter n: "))

for i in range(n,0,-1):
    for j in range(1,n+1-i):
        print(" ",end ="")
    for j in range(n+1-i,n+1):
        print(i,end ="")
    print()