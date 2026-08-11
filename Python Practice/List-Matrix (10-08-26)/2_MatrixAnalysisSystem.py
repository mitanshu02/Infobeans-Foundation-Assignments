'''
2.

=========================================================
            MATRIX ANALYSIS SYSTEM
=========================================================


A research laboratory stores experimental data in matrix form.
Scientists want a program that can analyze the matrix and provide
different statistics through a menu-driven application.

The application should allow the user to:

1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Prime Numbers Row-wise
   2. Count Perfect Numbers Column-wise
   3. Display Row-wise Sum
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Prime Numbers Row-wise
   ---------------------------------------
   Count and display the number of prime numbers present
   in each row of the matrix.

5. Choice 2 - Count Perfect Numbers Column-wise
   --------------------------------------------
   Count and display the number of perfect numbers present
   in each column of the matrix.

   Note:
   A perfect number is a number that is equal to the sum
   of its proper divisors.

   Examples:
   6  = 1 + 2 + 3
   28 = 1 + 2 + 4 + 7 + 14

6. Choice 3 - Display Row-wise Sum
   --------------------------------
   Calculate and display the sum of each row.

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Analysis System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
2 4 5
6 7 8
11 28 13

Output:
Row 1 Prime Count = 2
Row 2 Prime Count = 1
Row 3 Prime Count = 2

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 2

Output:
Column 1 Perfect Number Count = 1
Column 2 Perfect Number Count = 1
Column 3 Perfect Number Count = 0

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 3

Output:
Row 1 Sum = 11
Row 2 Sum = 21
Row 3 Sum = 52

---------------------------------------------------------

Menu
1. Count Prime Numbers Row-wise
2. Count Perfect Numbers Column-wise
3. Display Row-wise Sum
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Analysis System

=========================================================

'''
import math

while True:
    print("Menu")
    print("1. Count Prime Numbers Row-wise")
    print("2. Count Perfect Numbers Column Wise")
    print("3. Display Row Wise Sum")
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
                count = 0
                for j in range(c1):
                    n = A[i][j]
                    if n == 1:
                        pass
                    else:
                        for k in range(2,int(math.sqrt(n))+1):
                            if n%k == 0:
                                break
                        else:
                            count += 1
                print(f"Row {i+1} Prime Number Count = {count}")
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

            for i in range(c1):
                count = 0
                for j in range(r1):
                    n = A[j][i]
                    total = 0
                    for k in range(1,n//2 + 1):
                        if n%k == 0:
                            total = total + k
                    if total == n:
                        count += 1
                        
                print(f"Column {i+1} Perfect Number Count = {count}")
            print()         
        case 3:
            r1 = int(input("Enter number of rows in Matrix: "))
            c1 = int(input("Enter number of columns in matrix: "))
            A = []
            print("Enter Elements of Matrix : ")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input()))
                A.append(row)

            for i in range(r1):
                sum = 0
                for j in range(c1):
                    sum += A[i][j] 
                        
                print(f"Row {i+1} Element Sum = {sum}")
            print()   

        case 4:
            print("Thank You for Using Matrix Analysis System")
            break          
            
        case _:
            print("Please Enter a valid Choice.")
            continue
