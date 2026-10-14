'''
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:


aabbccdde


Output:

5

'''

m = input("Input: ")
res = ""
for ch in m:
    if ch not in res:
        res = res + ch

print("Output:",len(res))