"""
Q7. COUNT OCCURRENCE OF A PARTICULAR WORD

A company wants to analyze how frequently a particular keyword appears in a document.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a word from the user.
3. Counts how many times the given word occurs in the file.

Display the number of occurrences of the given word.
"""
with open("article.txt","r") as f:
    data = f.read()
    word  = input("Enter word to find its count in article.txt: ")
    count = 0

    for w in data.split():
        if w == word:
            count += 1

    print(f"Total occurance of {word} is {count} times.")