"""
Q8. COUNT WORDS STARTING WITH A PARTICULAR LETTER

A search engine wants to analyze words beginning with a particular character.

Write a Python program that:

1. Reads a file named "article.txt".
2. Accepts a character from the user.
3. Counts the number of words starting with that character.

Display the count.
"""
with open("article.txt","r") as f:
    data = f.read()
    letter = input("Enter letter to find count of words starting with it in article.txt: ")
    count = 0

    for w in data.split():
        if w.startswith(letter):
            count += 1

    print(f"Total no. words starting with {letter} are {count}")