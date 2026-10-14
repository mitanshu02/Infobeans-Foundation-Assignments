'''
5
54
543
5432
54321
'''
n = int(input("Enter n: "))

i = 1
while i<=n:
    j = n
    while j >= n+1-i:
        print(j,end = "")
        j = j - 1
    print()
    i = i+1 

