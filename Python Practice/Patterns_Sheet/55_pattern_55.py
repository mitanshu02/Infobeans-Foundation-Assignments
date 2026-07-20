'''
ABCDE
 ABCD
  ABC
   AB
    A

'''

n = int(input("Enter n: "))

for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(" ",end = "")
    for j in range(i,0,-1):
        print(chr(64+ i - j + 1),end ="")
    print()