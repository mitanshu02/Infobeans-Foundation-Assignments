'''
1
12
123
1234
12345
'''
n = int(input("Enter n: "))

i = 1
while i<=n:
    j = 1
    while j<=i:
        print(j,end = "")
        j = j+1
    print()
    i = i+1
