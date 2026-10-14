'''
a
bc
def
ghij
klmno

'''

n = int(input("Enter n: "))
k = 0
i = 0
while i < n:
    j = 0
    while j<=i:
        print(chr(97+k),end = "")
        k = k+1
        j = j+1
    print()
    i = i+1