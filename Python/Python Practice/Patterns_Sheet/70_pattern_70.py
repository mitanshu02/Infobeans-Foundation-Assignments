'''
* * * * *
 * * * *
  * * *
   * *
    *
'''
n = int(input("Enter n: "))

i = 0
while i < n:
    j = 0
    while j < i:
        print(" ",end = "")
        j += 1
    
    k = 1
    while k <= n-i:
        print("*",end = " ")
        k += 1
    print()
    i += 1

 
     