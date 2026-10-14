'''
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

coding = set()
robotics = set()


while True:
    print("""
Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit
    """)

    n = int(input("Select option: "))

    match n:

        case 1: 
            s = int(input("Enter number of students in Coding Club: "))

            print("Enter students in coding club: ")
            for i in range(s):
                coding.add(input())
        case 2:
            r = int(input("Enter number of students in robotics club: "))

            print("Enter students in Robotics club: ")
            for i in range(r):
                robotics.add(input())

        case 3:
            print("Students in coding club: ",*coding, sep = " ")
        case 4:
            print("Students in Robotics club: ",*robotics, sep = " ")
        case 5:
            print("Students in both the club:", coding&robotics)
        case 6:
            print("Student only in coding club:", coding-robotics)
        case 7:
            print("Student only in robotics club:", robotics-coding)
        case 8:
            print("All unique Club Members: ", coding|robotics)
        case 9:
            print("Total unique club Members: ", len(coding|robotics))
        case 10:
            print("[Exiting]")
            break
        case _:
            continues
            












