'''
QUESTION 5: LIBRARY BOOK RECORDS
================================

A library maintains book information using NamedTuple.

Fields:
book_id, title, author, price

Requirements:

1. Read N book records from the user and store them in a list of NamedTuples.

---

2. Display all book details.

---

3. Find and display the most expensive book.

---

4. Search books by author name.

---

5. Calculate and display the average price of all books.

---

Test Case:

Input:
Enter number of books: 4

B101 Python Basics John 450
B102 Java Programming James 550
B103 Data Science John 700
B104 SQL Guide Smith 300

Enter Author Name: John

Expected Output:
Most Expensive Book:
B103 Data Science John 700

Average Book Price:
500.0

Books Written By John:
B101 Python Basics John 450
B103 Data Science John 700
'''
from collections import namedtuple

book = namedtuple("books",["b_id","b_name","author","price"])

n = int(input("Enter no. of records: ")) 

br = [] #br -> book record

for i in range(n):
    print(f"Enter Records for book no. {i+1}")
    b_id = input("Enter Book ID : ")
    b_name = input("Enter book name : ")
    author = input("Enter name of author: ")
    price = int(input("Enter price of book: "))

    b = book(b_id,b_name,author,price)
    br.append(b)
    print()

print("All Books: ")

for b in br:
    print(*b)

print()

authorName = input("Enter Author name whose book you wanna search: ")

highest = br[0].price
h_idx = 0
total = 0

for i in range(n):
    total = total + br[i].price

    if br[i].price > highest:
        highest = br[i].price
        h_idx = i

    

print()
print("Most Expensive Book: ")
print(*br[h_idx])

print()

print("Average price of all books: ")
print(total/n)

print()

print(f"Books Written by {authorName}: ")

for b in br:
    if b.author == authorName:
        print(*b)

