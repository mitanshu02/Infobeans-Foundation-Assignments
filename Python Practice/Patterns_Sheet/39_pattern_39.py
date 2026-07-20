'''
123456
54321
1234
321
12
1

'''
# approach 1:

n = int(input("Enter n: "))

i = n

while i>=1:
    if i % 2 == 0:
        j = 1
        while j<=i:
            print(j,end ="")
            j += 1
    else:
        j = i
        while j>=1:
            print(j,end = "")
            j -= 1
    print()
    i -= 1
    
#=========================================================

# approach 2:

n = int(input("Enter n: "))

i = n

while i >= 1:

    if i % 2 == 0:
        j = 1
        step = 1
    else:
        j = i
        step = -1

    while 1 <= j <= i:
        print(j, end="")
        j = j + step

    print()
    i = i - 1