'''
6. Find Occurrence of a Word in a String

Product Review Analysis System

An e-commerce company wants to analyze customer reviews.

The company wants a Python program to count how many times a particular word appears in a review.

Input Sentence:


iphone is good and iphone battery is strong


Word:


iphone


Output:


2
'''
m = input("Input Sentence:")
word = input("Word: ")
count = 0
l = len(m)
for i in range(l):
    ch = m[i]
    res = ""
    if ch != " ":
        if (i == 0 or m[i-1] == " ") and (i == l-1 or m[i+1] == " "):
            res = m[i]
            if res == word:
                count += 1
        elif i == 0 or m[i-1] == " ":
            start = i
        elif i == l-1 or m[i+1] == " ":
            end = i
      
            res = m[start:end+1]
            if res == word:
                count += 1
        

print("Output:",count)
        






'''
# Using split
m = input("Input Sentence:")
word = input("Word: ")
count = 0

for w in m.split():
    if word == w:
        count += 1

print("Output:",count)

'''
