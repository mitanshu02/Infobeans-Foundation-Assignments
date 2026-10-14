'''
    *
   1*1
  1***1
 1*****1
111111111
'''
n = int(input("Enter n: "))

i = 1
while i <= n:
    j = n-i
    while j > 0:
        print(" ",end = "")
        j -= 1

    k = 1
    while k < (2*i):
        if i == n:
            print("1",end ="")
        elif k > 1 and k < (2*i) - 1:
            print("*",end = "")
        else:
            print("1",end = "")
        k += 1
    print()
    i += 1