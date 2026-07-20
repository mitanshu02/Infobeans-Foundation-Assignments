'''
654321
 65432
  6543
   654
    65
'''
n = int(input("Enter n:"))

i = 6
while i > 1:
    j = 1
    while j <= 6-i:
        print(" ",end = "")
        j = j + 1
    
    k = 6
    while  k>= 7-i:
        print(k,end = "")
        k = k - 1

    print()
    i = i - 1