'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''
m = input("Input: ")
l = len(m)
ans = ""

for i in range(l):
    if i < l-1:
        if m[i] != m[i+1]:
            ans = ans + m[i]
    else:
            ans = ans + m[i]

print(ans)