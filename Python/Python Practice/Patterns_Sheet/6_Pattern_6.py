'''
1
00
111
0000
11111
'''

n = int(input("Enter n: "))

i = 1
while i<=n:
    j = 1
    while j<=n:
        print(i,end = "")
        j = j+1
    print()
    i = i+1