'''
55555
 4__4
  3_3
   22
    1
'''

n = int(input("Enter n: "))

i = n
while i >= 1:
    j = 5
    while j > i:
        print(" ",end = "")
        j -= 1
    j = i
    while j>=1:
        if i == n or j == 1 or j == i:
            print(i,end = "")
        else: 
            print("_",end = "") 
        j -= 1
    print()
    i -= 1
