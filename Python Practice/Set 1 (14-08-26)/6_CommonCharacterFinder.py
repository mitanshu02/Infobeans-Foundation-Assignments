'''
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}

'''
first = ""
second = ""

while True:
    print("""
Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit
""")
    n = int(input("Select an option: "))
    
    match n:
        case 1:
            first = set(input("Enter First String: "))
        case 2:
            second = set(input("Enter Second String: "))
        case 3:
            print("Common Characters:")
            print(first & second)
        case 4:
            print("Total common Characters: ",len(first & second))
        case 5:
            print("[Exiting...]")
            break
        case _:
            continue