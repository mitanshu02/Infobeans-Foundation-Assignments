'''
7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

'''
elem = [int(x) for x in input("Input: ").split()]
k = int(input("enter k: "))

k = k % len(elem) #coz for n > k the simple logic won't work

ans = elem[len(elem)-k : ] + elem[:len(elem)-k]
print(ans)