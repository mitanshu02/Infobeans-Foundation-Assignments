'''
x
xx
xxx
xxxx
xxx
xx
x
'''

n = int(input("Enter n: "))

mid = (n + 1) // 2

for i in range(1, n + 1):

    if i <= mid:
        print("x" * i)
    else:
        print("x" * (n - i + 1))