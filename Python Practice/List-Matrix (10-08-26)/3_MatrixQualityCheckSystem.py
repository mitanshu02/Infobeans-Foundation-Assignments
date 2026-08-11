'''
3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================

'''

while True:
    print("Menu")
    print("1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
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
                    m = n
                    l = len(str(n))
                    sum = 0
                    while n > 0:
                        r = n%10
                        sum = sum + r**l
                        n = n//10
                    if sum == m:
                        count += 1 
                print(f"Row {i+1} Armstrong Number Count = {count}")
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
                    n = str(n)
                    if n == n[::-1]:
                        count += 1
                        
                print(f"Column {i+1} Palindrome Number Count = {count}")
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
                        
                print(f"Row {i+1} Elements Average = {sum/c1}")
            print()   

        case 4:
            print("Thank You for Using Matrix Quality Check System")
            break          
            
        case _:
            print("Please Enter a valid Choice.")
            continue