from collections import namedtuple

books  = []

n = int(input("Enter number of books: "))

book = namedtuple("Book",["book_id","title","author","price"])

for i in range(n):
    print(f"Enter book {i+1} info: ")
    b_id = input("Enter book id: ")
    t = input("Enter title: ")
    a = input("Enter author: ")
    p = int(input("Enter price: "))

    b1 = book(b_id,t,a,p)
    books.append(b1)

print("All book details: ")
print()

for book in books:
    print(*book)


exp = 0
exp_id = ""
cheapest = 100000000000000
chp_id = ""

for book in books:
    if book.price > exp:
        exp = book.price
        exp_id = book.book_id
    if book.price < cheapest:
        cheapest = book.price
        chp_id = book.book_id

print()
print("Most Expensive book: ")
for book in books:
    if book.book_id == exp_id:
        print(*book)

print()
print("Most cheapest book: ")
for book in books:
    if book.book_id == chp_id:
        print(*book)

total = 0
for book in books:
    total += book.price

Avg = total/n
print("Average price: ",Avg)
print()

print("Book price greater than avg:")

for book in books:
    if book.price > Avg:
        print(*book)

