'''
# 6. AI Chat Toxic Pattern Detector

An AI moderation system wants to detect whether a sentence contains three consecutive repeating characters.

If found:

text
Spam Pattern Found


Else:

text
Clean Message


### Input:

text
heyyy broooo welcome


### Output:

text
Spam Pattern Found
'''

m = input("Input: ")

for i in range(len(m)-2):
    if m[i] == m[i+1] and m[i+1] == m[i+2]:
        print("Spam Pattern Found")
        break
else:
    print("Clean Message")