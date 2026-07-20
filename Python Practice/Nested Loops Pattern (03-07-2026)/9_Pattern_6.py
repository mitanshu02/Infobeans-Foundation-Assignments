'''
    1
   10
  101
 1010
10101
'''
n = int(input("Enter n:"))

i = n
while i>=1:
    
    j = i-1
    while j>=1:
        print("*", end = "")
        j = j-1
    
    k = i
    while k<=n:
        if i %2 != 0:
            if k%2 ==0:
                print(0,end = "")
            else:
                print(1,end = "")
        else:
            if k%2 ==0:
                print(1,end = "")
            else:
                print(0,end = "")
        k = k+1

    print()
    i = i-1


# will  try by putting i = 0, k = 0 and j = 0
    