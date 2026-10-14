'''
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.

'''
python = set()
java = set()


while True:
    print("""
Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit
    """)

    n = int(input("Select option: "))

    match n:

        case 1: 
            s = int(input("Enter number of students in python course: "))

            print("Enter students in python course: ")
            for i in range(s):
                python.add(input())
        case 2:
            r = int(input("Enter number of students in java course: "))

            print("Enter students in java course: ")
            for i in range(r):
                java.add(input())

        case 3:
            print("Students in python course: ",*python, sep = " ")
        case 4:
            print("Students in java course: ",*java, sep = " ")
        case 5:
            print("Students in both the course:", python&java)
        case 6:
            print("Student only in python course:", python-java)
        case 7:
            print("Student only in java course:", java-python)
        case 8:
            print("All unique Course Members: ", python|java)
        case 9:
            print("Total unique Students: ", len(python|java))
        case 10:
            print("[Exiting]")
            break
        case _:
            continues
