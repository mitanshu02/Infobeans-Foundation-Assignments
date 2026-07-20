'''
1
123
12345
1234567
123456789

'''

n = int(input("Enter n: "))

i = 1
while i<=n:
    j = 1
    while j <= 2*i-1:
        print(j,end = "")
        j = j + 1
    print()
    i = i+1 
