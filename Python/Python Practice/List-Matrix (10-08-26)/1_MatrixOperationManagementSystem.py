'''
1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

========================================================='''

while True:
    print("Menu")
    print("1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")
    print()
    
    choice = int(input("Enter your Choice: "))
    
    match choice:
        case 1:
            r1 = int(input("Enter number of rows in first Matrix: "))
            c1 = int(input("Enter number of columns in first matrix: "))

            r2 = int(input("Enter number of rows in second Matrix: "))
            c2 = int(input("Enter number of columns in second matrix: "))
            
            if r1 != r2 or c1 != c2:
                print("Addition Cannot Be performed.")
                print()
                continue
            else:
                A = []
                print("Enter Elements of Matrix 1: ")
                for i in range(r1):
                    row = []
                    for j in range(c1):
                        row.append(int(input()))
                    A.append(row)

                B = []
                print("Enter Elements of Matrix 2: ")
                for i in range(r2):
                    row = []
                    for j in range(c2):
                        row.append(int(input()))
                    B.append(row)
                C = []
                for i in range(r1):
                    row = []
                    for j in range(c1):
                        row.append(A[i][j] + B[i][j])
                    C.append(row)

                print("Result Matrix: ")
                for r in C:
                    print(*r)
                
        case 2:
            r1 = int(input("Enter number of rows in first Matrix: "))
            c1 = int(input("Enter number of columns in first matrix: "))

            r2 = int(input("Enter number of rows in second Matrix: "))
            c2 = int(input("Enter number of columns in second matrix: "))
            
            if r1 != r2 or c1 != c2:
                print("Subtraction Cannot Be performed.")
                print()
                continue
            else:
                A = []
                print("Enter Elements of Matrix 1: ")
                for i in range(r1):
                    row = []
                    for j in range(c1):
                        row.append(int(input()))
                    A.append(row)

                B = []
                print("Enter Elements of Matrix 2: ")
                for i in range(r2):
                    row = []
                    for j in range(c2):
                        row.append(int(input()))
                    B.append(row)
                C = []
                for i in range(r1):
                    row = []
                    for j in range(c1):
                        row.append(A[i][j] - B[i][j])
                    C.append(row)

                print("Result Matrix: ")
                for r in C:
                    print(*r)
         
        case 3:
            r1 = int(input("Enter number of rows in first Matrix: "))
            c1 = int(input("Enter number of columns in first matrix: "))

            r2 = int(input("Enter number of rows in second Matrix: "))
            c2 = int(input("Enter number of columns in second matrix: "))
            
            if r1 != r2 or c1 != c2:
                print()
                print("Matrices are Not equal")
                print()
                continue
            else:
                A = []
                print("Enter Elements of Matrix 1: ")
                for i in range(r1):
                    row = []
                    for j in range(c1):
                        row.append(int(input()))
                    A.append(row)

                B = []
                print("Enter Elements of Matrix 2: ")
                for i in range(r2):
                    row = []
                    for j in range(c2):
                        row.append(int(input()))
                    B.append(row)
  
                for i in range(r1):
                    for j in range(c1):
                        if A[i][j] != B[i][j]:
                            print("Metrices are Not Equal")
                            print()
                            break
                    else:
                        continue
                    break
                else:
                    print("Matrices are Equal")
        case 4:
            print("Thank You for Using Matrix Operations Management System")
            break          
            
        case _:
            print("Please Enter a valid Choice.")
            continue
    