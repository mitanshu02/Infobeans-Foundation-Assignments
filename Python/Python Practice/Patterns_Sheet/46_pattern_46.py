'''
    A
   AB
  ABC
 ABCD
ABCDE

'''

n= int(input("Enter n: "))

for i in range(1, n+1):
    c = 65
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            print(chr(c),end ="")
            c += 1
    print()