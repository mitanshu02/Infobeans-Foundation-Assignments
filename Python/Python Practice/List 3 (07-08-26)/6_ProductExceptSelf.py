'''
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]


'''
n = int(input("Enter n: "))

elem = [int(x) for x in input("Input: ").split()]

m = 1
ans = []
for ch in elem:
    m *= ch

for ch in elem:
    ans.append(m//ch)
print(ans)