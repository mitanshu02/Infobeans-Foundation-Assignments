print(ord('a'))

'''
a
ab
abc
abcd
abcde

'''

n = int(input("Enter n: "))

i = 0
while i < n:
    j = 0
    while j<=i:
        print(chr(97+j),end = "")
        j = j+1
    print()
    i = i+1
    