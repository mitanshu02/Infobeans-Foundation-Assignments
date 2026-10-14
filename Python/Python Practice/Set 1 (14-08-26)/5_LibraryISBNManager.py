'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.

'''


isbn = set()


while True:
    print("""
Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit
    """)

    n = int(input("Select option: "))

    match n:

        case 1: 
            s = int(input("Enter number of books to add: "))

            print("Enter ISBN: ")
            for i in range(s):
                isbn.add(input())
        case 2:
            b = input("enter book's ISBN to remove: ")
            isbn.discard(b)
        case 3:
            b = input("Enter ISBN to search book: ")
            if b in isbn:
                print("Book Present in Record")
            else:
                print("Book Not Present")
        case 4:
            print(*isbn, sep = ", ")
        case 5:
            print("Book Count: ",len(isbn))
        case 6:
            print("[Exiting]")
            break
        case _:
            continues