"""
Q4. COUNT LINES, WORDS AND CHARACTERS IN A FILE

A content management company wants to analyze the size of a text document.

Write a Python program that reads a file named "article.txt" and displays:

1. Total number of lines
2. Total number of words
3. Total number of characters
"""

with open("article.txt","r") as f:
    l_count = 0
    w_count = 0
    c_count = 0

    for line in f:
        l_count += 1
        w_count += len(line.strip().split())
        for w in line.strip().split():
            c_count += len(w)

    print("Total lines: ",l_count)
    print("Total words: ",w_count)
    print("Total characters: ",c_count)
    