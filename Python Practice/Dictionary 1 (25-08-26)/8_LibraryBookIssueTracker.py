'''
8.
=========================================
LIBRARY BOOK ISSUE TRACKER
==========================

A library records issued books.

books = [
"Python",
"Java",
"Python",
"C++",
"Java",
"Python"
]

Write a program to:

* Count how many times each book was issued.

Sample Output:
{
'Python':3,
'Java':2,
'C++':1
}

---
'''
books = [book for book in input("Enter books: ").split()]

d= {}

for book in books:
    d[book] = d.get(book,0)+1

print(d)