'''
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''
m = input("Input: ").lower()
l = len(m)
secondHighest = 0
highest = 0
secondHighestChar = ""
highestChar = ""
visited = ""

for i in range(l):
    ch = m[i]
    if ch != " ":
        if ch in visited:
            continue
        else:
            count = 0
            for j  in range(l):
                if ch == m[j]:
                    count += 1
            visited += ch
            if count > highest:
                secondHighest = highest
                secondHighestChar = highestChar 
                highest = count
                highestChar = ch
            elif count >= secondHighest and count < highest:
                secondHighest = count
                secondHighestChar = ch

if secondHighestChar != "":     
    print(secondHighestChar)
else:
    print("Second highest repeating character not found")                