'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''
m = input("Input: ")
l = len(m)
visited = ""
maximum = 0
maxC = ""
for i in range(l):
    ch = m[i]
    count = 0
    if ch not in visited:
        for j in range(l): 
            if ch == m[j]:
                count += 1
        if count >= maximum:
            if count > maximum:
                maximum = count
                maxC = ch
            elif count == maximum:
                maxC += ch
    visited = visited + ch

print(*maxC,sep=" ")
            



    
