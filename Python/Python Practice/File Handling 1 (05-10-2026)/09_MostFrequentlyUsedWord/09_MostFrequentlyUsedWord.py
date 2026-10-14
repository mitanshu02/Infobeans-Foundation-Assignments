"""
Q9. FIND THE MOST FREQUENTLY USED WORD

A content-analysis application wants to identify the most frequently used word in an article.

Write a Python program that reads a file named "article.txt" and finds the word that occurs the maximum number of times.

Display:

Most Frequently Used Word
Frequency
"""
with open("article.txt","r") as f:
    data = f.read()
    words = {}

    for w in data.split():
        words[w] = words.get(w,0)+1

    highest = 0
    mostFrequent = ''

    for w,c in words.items():
        if c > highest:
            highest = c
            mostFrequent = w

    print(f"Most frequent word is {mostFrequent} that appeared {highest} times.")
    