'''
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found

'''
n = int(input("Enter n: "))

elem = [int(x) for x in input("Input: ").split()]

for i in range(1,len(elem)-1):
    sum1 = 0
    sum2 = 0
    for j in elem[:i]:
        sum1 += j
    for k in elem[i+1:]:
        sum2 += k
    if sum1 == sum2:
        print(f"Equilibrium Index = {i}")
        break
else:
    print("No Equilibrium index found")

