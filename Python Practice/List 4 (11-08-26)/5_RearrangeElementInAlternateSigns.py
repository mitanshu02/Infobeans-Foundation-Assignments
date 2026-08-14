'''
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers.
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input:
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input:
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0

'''
a = [int(x) for x in input("Enter elements: ").split()]

pos = []
neg = []
res = []
for c in a:
    if c<0:
        neg.append(c)
    else:
        pos.append(c)

p = 0
n = 0

for i in range(len(a)):
    if p < len(pos) and n < len(neg):
        if i%2 != 0:
            res.append(neg[n])
            n = n+1
        else:
            res.append(pos[p])
            p = p+1

    elif p < len(pos):
        res.append(pos[p])
        p = p+1
    
    elif n < len(neg):
        res.append(neg[n])
        n = n+1

print(*res)        
        
        
        