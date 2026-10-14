'''
    1
   12
  123
 1234
12345

'''
n = int(input("Enter n: "))

# approach 1:

for i in range(1, n+1):
    c = 1
    for j in range(1,n+1):     
        if j< n-i+1:
            print(" ",end ="")
        else:
            print(c,end ="")
            c += 1
    print()
    
#approach 2:
'''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j < n - i + 1:
            print(" ", end="")
        else:
            print(j - n + i, end="")
    print()
'''