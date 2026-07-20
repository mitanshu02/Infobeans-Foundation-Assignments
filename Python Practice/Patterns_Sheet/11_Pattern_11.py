'''
A
AB
ABC
ABCD
ABCDE

'''

n = int(input("Enter n: "))

i = 0
while i < n:
    j = 0
    while j<=i:
        print(chr(65+j),end = "")
        j = j+1
    print()
    i = i+1
    