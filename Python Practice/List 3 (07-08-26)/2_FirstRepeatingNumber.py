'''
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found

'''
n = int(input("Enter n: "))

votes = [int(x) for x in input("Input: ").split()]

for i in range(len(votes)):
    c = votes[i]
    if c in votes[i+1:len(votes)]:
        print(f"First Repeating Number = {c}")
        break
else:
    print("No Repeating Number Found")