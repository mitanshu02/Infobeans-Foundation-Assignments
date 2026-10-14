'''
12345
 1234
  123
   12
    1

'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end ="")
    for j in range(1,n-i+2):
        print(j,end ="")
    print()