'''
*
**
****
*******
***********

'''
#Approach 1

n = int(input("Enter n:"))

next = 1
for i in range(1, n+1):
    for j in range(1,(i-1)+next+1):
        if j == (i-1)+next :
            next = j
        print("*", end ="")
    print()

# Approach 2
'''
n = int(input("Enter n: "))

for i in range(1, n + 1):

    stars = 1 + (i - 1) * i // 2

    for j in range(1, stars + 1):
        print("*", end="")

    print()
'''
Differences:

+1
+2
+3
+4

The differences are the first natural numbers.

Sum of first n natural numbers:

1 + 2 + 3 + ... + n = n(n + 1) / 2

Since each row adds the sum up to (row - 1),

Stars = 1 + (1 + 2 + ... + (row - 1))

Therefore,

Stars = 1 + (row - 1) × row / 2

'''