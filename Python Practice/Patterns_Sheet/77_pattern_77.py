'''
1
12
123
1234
123
12
1
'''

n = int(input("Enter number of rows: "))

mid = (n + 1) // 2

for i in range(1, n + 1):

    if i <= mid:
        for j in range(1, i + 1):
            print(j, end="")
    else:
        for j in range(1, n - i + 2):
            print(j, end="")

    print()