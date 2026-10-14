from models import Book

b1 = Book(101, "Java", "James", 650)
b2 = Book(102, "Python", "Mark", 550)
b3 = Book(103, "MySQL", "John", 450)
b4 = Book(104, "Advanced DSA", "James", 800)
b5 = Book(105, "DSA in Python", "Robert", 700)

books = [b1, b2, b3, b4, b5]

while True:
    print("""
1. Display all books.
2. Search a book using Book ID.
3. Display books by a particular author.
4. Display books having price greater than 500.
5. Find the most expensive book.
6. Calculate average price.
7. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Book Information ----")
        print()

        for book in books:
            book.display()

    elif n == 2:
        bookId = int(input("Enter Book ID: "))

        for book in books:
            if book.book_id == bookId:
                print("---- Book Found ----")
                book.display()
                break
        else:
            print("[ Book Not Found ]")

    elif n == 3:
        authorName = input("Enter Author Name: ")

        for book in books:
            if book.author.lower() == authorName.lower():
                print(f"{book.book_id:10}|{book.book_name:25}|{book.price:10}")

    elif n == 4:
        print("---- Books With Price Greater Than 500 ----")
        print()

        for book in books:
            if book.price > 500:
                print(book.book_name)

    elif n == 5:
        highest = 0
        bookId = None

        for book in books:
            if book.price > highest:
                highest = book.price
                bookId = book.book_id

        for book in books:
            if book.book_id == bookId:
                print("---- Most Expensive Book ----")
                print(f"{book.book_name} = {book.price}")
                break

    elif n == 6:
        total = 0

        for book in books:
            total += book.price

        average = total / len(books)

        print("Average Price:", average)

    elif n == 7:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue