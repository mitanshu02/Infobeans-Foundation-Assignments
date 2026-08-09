'''
1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found
'''
n = int(input("Enter n: "))

votes = [int(x) for x in input("Input: ").split()]
visited = []
for i in range(len(votes)):
    c = votes[i]
    if c not in visited:
        if c not in votes[i+1:len(votes)]:
            print(f"First Non Repeating Number = {c}")
            break
    visited.append(c)
else:
    print("No Non-Repeating Number Found")