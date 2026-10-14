'''
8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4

=========================================================================================
'''
while True:
    print("Menu")
    print("1. Count Even Number Above Main Digonal")
    print("2. Count Odd Numbers Below Main Digonal")
    print("3. Display Boundary Elements")
    print("4. Exit")

    n = int(input("Select an operation you want to perform"))

    match n:
        case 1:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            m = []
            count = 0
            
            print("Enter Elements: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                m.append(row)
                    
            for i in range(r):
                for j in range(c):
                    if j > i and m[i][j] % 2 == 0:
                        count += 1
            print("Even numbers above Main Digonal =",count)

        case 2:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            m = []
            count = 0
            
            print("Enter Elements: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                m.append(row)
                    
            for i in range(r):
                for j in range(c):
                    if j < i and m[i][j] % 2 != 0:
                        count += 1
            print("Odd numbers below Main Digonal =",count)

        case 3:
            r = int(input("Enter number of rows: "))
            c = int(input("Enter number of columns: "))
            m = []
            count = 0
            
            print("Enter Elements: ")
            for i in range(r):
                row = []
                for j in range(c):
                    row.append(int(input()))
                m.append(row)
                    
            for i in range(r):
                for j in range(c):
                    if i == 0 or j == 0 or i == r-1 or j == c-1:
                        print(m[i][j],end = " ")
                        
            print()

        case 4:
            print("[Exiting System]")
            break
        case _:
            continue