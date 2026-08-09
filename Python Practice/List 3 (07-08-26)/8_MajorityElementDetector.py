'''
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found
'''
elem = [int(x) for x in input("Input: ").split()]

visited = []
largest = 0
Hit = 2
for ch in elem:
    if ch not in visited:
        c = elem.count(ch)
    if c != largest:
        Hit -= 1
    if c > largest:
        largest = c
        ans = ch

if Hit <= 0:
    print(f"Majority Element = {ans}")
else:
    print("No Majority Element Found")

#print("Majority Element =",max(elem, key = elem.count))