'''

2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")

'''
n = int(input("Enter N: "))
p = input("Enter passwords: ").split()

count = 0

for i in range(n):
    for j in range(i + 1, n):

        common = False

        for ch in p[i]:
            if ch in p[j]:
                common = True
                break

        if not common:
            count += 1

print(count)