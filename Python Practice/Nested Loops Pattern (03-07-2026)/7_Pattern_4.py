n = int(input("Enter n:"))

i = n

while i>=1:
    j = i-1
    while j>=1:
        print(" ",end ="")
        j = j - 1
    
    k = 1
    while k<= n-i+1:
        print("*",end = "")
        k = k + 1
    i = i - 1
    print()