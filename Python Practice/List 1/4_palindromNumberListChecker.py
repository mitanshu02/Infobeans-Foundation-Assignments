'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

nums = [x for x in input("Enter Nummbers: ").split()]
palindromes = []

for n in nums:
    if n == n[::-1]:
        palindromes.append(int(n))

print("Palindromes: ",palindromes)
print("Count: ",len(palindromes))
print("largest: ",max(palindromes))
palindromes.sort()
print("Sorted: ", palindromes)
    