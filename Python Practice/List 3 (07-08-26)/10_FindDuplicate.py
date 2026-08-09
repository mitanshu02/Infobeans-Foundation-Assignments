'''
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

'''
elem = [int(x) for x in input("Input: ").split()]
duplicate = []
v = []

for i in range(len(elem)):
    if elem[i] not in v:
        if elem[i] in elem[i+1:]:
            duplicate.append(elem[i])
        v.append(elem[i])
if duplicate:
    print("Duplicate Numbers =",duplicate)
    print("Count =",len(duplicate))
else:
    print("No Duplicate Numbers Found")


