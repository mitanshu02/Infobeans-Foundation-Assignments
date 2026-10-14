"""
Q6. FIND THE LONGEST WORD

A document-processing application needs to identify the longest word in a text document.

Write a Python program that reads a file named "article.txt" and finds the longest word in the file.

Display:

Longest Word
Length
"""
with open("article.txt","r") as f:
    data = f.read()
    maximum = 0
    longestWord = ""
    for word in data.split():
        if len(word) > maximum:
            maximum = len(word)
            longestWord = word

    print("Longest Word :",longestWord)
    print("Length :",maximum)