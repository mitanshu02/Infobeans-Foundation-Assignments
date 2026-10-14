"""
Q5. COUNT VOWELS AND CONSONANTS

A language-learning application wants to analyze the characters used in a paragraph.

Write a Python program that reads a file named "paragraph.txt" and counts:

1. Total number of vowels
2. Total number of consonants

Ignore numbers, spaces and special characters.
"""
with open("paragraph.txt","r") as f:
    data = f.read()
    v_count = 0
    c_count = 0

    for ch in data:
        if ch in {'a','e','i','o','u','A','E','I','O','U'}:
            v_count += 1
        else:
            c_count += 1

    print("Total Vowels:",v_count)
    print("Total Consonent:",c_count)
    