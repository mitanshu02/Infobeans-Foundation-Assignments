'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''
import math

n = int(input("Enter n:"))

for i in range(0,n):
    for j in range(1,n-i+1):
        print(" ",end ="")
    for j in range(0,i+1):
        num=int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j)))
        print(num,end=" ")
    print()


