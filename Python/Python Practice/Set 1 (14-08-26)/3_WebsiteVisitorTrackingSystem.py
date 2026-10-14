'''
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.

'''

visitor = set()


while True:
    print("""
Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit
    """)

    n = int(input("Select option: "))

    match n:

        case 1: 
            s = int(input("Enter number of visitors: "))

            print("Enter visitors: ")
            for i in range(s):
                visitor.add(input())
        case 2:
            vis = input("enter Visitor to remove: ")
            visitor.discard(vis)
        case 3:
            vis = input("Enter visitor to check: ")
            if vis in visitor:
                print("Visited")
            else:
                print("Not Visited")
        case 4:
            print(*visitor, sep = ", ")
        case 5:
            print("Unique Visitors Count: ",len(visitor))
        case 6:
            visitor.clear()
            print("Cleared Visitor list")
        case 7:
            print("[Exiting]")
            break
        case _:
            continues