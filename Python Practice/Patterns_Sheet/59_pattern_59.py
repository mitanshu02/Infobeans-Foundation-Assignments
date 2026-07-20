'''
    A
   AB
  ABC
 ABCD
ABCDE

'''

n = int(input("Enter n: "))

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end ="")
    for j in range(1,i+1):
        print(chr(64+j),end ="")
    print() 