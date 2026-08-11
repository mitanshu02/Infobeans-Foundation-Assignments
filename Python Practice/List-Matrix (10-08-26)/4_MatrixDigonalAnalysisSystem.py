'''
4.

=========================================================
        MATRIX DIAGONAL ANALYSIS SYSTEM
=========================================================

Scenario

A security company stores surveillance data in matrix form.
The analyst wants a menu-driven application to examine the
diagonal elements of the matrix and generate reports.

The application should allow the user to:

1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Display Main Diagonal Elements
   2. Display Secondary Diagonal Elements
   3. Compare Main and Secondary Diagonal Sums
   4. Exit

2. Read the size of a square matrix from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Display Main Diagonal Elements
   -----------------------------------------
   Display all elements present in the main diagonal.

5. Choice 2 - Display Secondary Diagonal Elements
   ----------------------------------------------
   Display all elements present in the secondary diagonal.

6. Choice 3 - Compare Main and Secondary Diagonal Sums
   ---------------------------------------------------
   Calculate the sum of both diagonals and display:

   - Main Diagonal Sum
   - Secondary Diagonal Sum
   - Which diagonal has the greater sum
   - Or whether both sums are equal

7. Choice 4 - Exit
   -----------------------------------------
   Display:
   "Thank You for Using Matrix Diagonal Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Enter size of matrix: 3

Enter matrix elements:

1 2 3
4 5 6
7 8 9

Menu
1. Display Main Diagonal Elements
2. Display Secondary Diagonal Elements
3. Compare Main and Secondary Diagonal Sums
4. Exit

Enter your choice: 1

Output:
Main Diagonal Elements:
1 5 9

---------------------------------------------------------

Enter your choice: 2

Output:
Secondary Diagonal Elements:
3 5 7

---------------------------------------------------------

Enter your choice: 3

Output:
Main Diagonal Sum = 15
Secondary Diagonal Sum = 15
Both Diagonal Sums are Equal

=========================================================
'''

while True:
    print("Menu")
    print("1. Display Main Digonal Elements")
    print("2. Display Secondary Digonal Elements")
    print("3. Compare Main and Secondary Digonal Sums")
    print("4. Exit")
    print()
    
    choice = int(input("Enter your Choice: "))
    
    match choice:
        case 1:
            r1 = int(input("Enter number of rows in first Matrix: "))
            c1 = int(input("Enter number of columns in first matrix: "))
            A = []
            print("Enter Elements of Matrix 1: ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input()))
                A.append(row)

            for i in range(r1):
                print(A[i][i], end = " ")
            print()
                
        case 2:
            r1 = int(input("Enter number of rows in Matrix: "))
            c1 = int(input("Enter number of columns in matrix: "))
            A = []
            print("Enter Elements of Matrix 1: ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input()))
                A.append(row)

            for i in range(r1):
                print(A[i][c1-i-1],end = " ")             
            print()         
        case 3:
            r1 = int(input("Enter number of rows in Matrix: "))
            c1 = int(input("Enter number of columns in matrix: "))
            A = []
            sum1 = 0
            sum2 = 0
            print("Enter Elements of Matrix 1: ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input()))
                A.append(row)
            
            for i in range(r1):
                sum1 += A[i][i]
                sum2 += A[i][c1-i-1]

                
            print(f"Main Digonal Sum = {sum1}")
            print(f"Secondary Digonal Sum = {sum2}")
            if sum1 == sum2:
                print("Both digonal Sums are equal")
            else:
                print("Both digonal Sums are not equal")
            print()   

        case 4:
            print("Thank You for Using Matrix Digonal Analysis System")
            break          
            
        case _:
            print("Please Enter a valid Choice.")
            continue