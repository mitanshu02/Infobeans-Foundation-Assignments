'''
123456789
 1     7
  1   5
   1 3
    1

'''
n = int(input("Enter n: "))

for i in range(n):
    for j in range(i):
        print(" ",end = "")
    for j in range(2*(n-i)-1):
        if i == 0:
            print(j+1,end = "")
        elif j == 0 or j == 2*(n-i)-2:
            print(j+1,end = "")
        else:
            print(" ",end = "")
    print()