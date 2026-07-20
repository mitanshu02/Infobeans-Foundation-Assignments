'''
1
222
33333
4444444
555555555

'''

n = int(input("Enter n: "))

i = 1
while i<=n:
    j = 1
    while j <= 2*i-1:
        print(i,end = "")
        j = j + 1
    print()
    i = i+1 