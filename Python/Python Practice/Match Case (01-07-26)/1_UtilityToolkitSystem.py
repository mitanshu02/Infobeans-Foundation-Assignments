"""
1. Utility Toolkit System

You are developing a Utility Toolkit Application for a small office. Employees use this tool to quickly perform common number operations like checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions

"""
import math
while True:
    print("1 → Check Prime Number")
    print("2 → Check Palindrome Number")
    print("3 → Reverse a Number")
    print("4 → Count Digits")
    print("5 → Exit")

    i = int(input("Enter your choice: "))
    
    match i:
        case 1:
            n = int(input("Enter Number: "))
            if n <= 1:
                print("Not Prime Number")
            elif n == 2:
                print("Prime Number")
            else:
                i = 2
                while i <= int(math.sqrt(n)):
                    if n % i == 0:
                        print("Not Prime Number")
                        break
                    i = i+1
                else:
                    print("Prime Number")
        case 2:
            n = int(input("Enter Number: "))
            temp = n
            r = 0
            
            while n>0:
                r = r*10 + n%10
                n = n//10
            if r == temp:
                print(f"{temp} is Palindrome")
            else:
                print(f"{temp} is not Palindrome")
                
        case 3:
            n = int(input("Enter Number: "))
            r = 0
            
            while n>0:
                r = r*10 + n%10
                n = n//10
            print(f"Reversed Number is: {r}")

        case 4:
            n = int(input("Enter Number: "))
            print("Total Digits:",len(str(n)))
        case 5:
            print("Exiting program... Thank you!")
            break
        case __:
            print("Invalid choice, please enter choice between 1-5")
            continue
    ask = input("Do you wish to continue(yes/no) :").lower()
    if ask == "yes":
        continue
    elif ask == "no":
        break
    else:
        print("wrong input")
        break
