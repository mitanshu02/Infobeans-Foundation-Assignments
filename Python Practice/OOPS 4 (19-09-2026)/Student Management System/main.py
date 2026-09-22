from models import Student

s1 = Student(101, "Amit", 78)
s2 = Student(102, "Rahul", 55)
s3 = Student(103, "Priya", 91)
s4 = Student(104, "Neha", 67)
s5 = Student(105, "Rohit", 45)

students = [s1, s2, s3, s4, s5]

while True:
    print("""
1. Display all students.
2. Display students having marks greater than 60.
3. Find student having highest marks.
4. Calculate average marks.
5. Exit
""")

    n = int(input("Choose an option: "))

    if n == 1:
        print("---- Student Information ----")
        print()

        for stu in students:
            stu.display()

    elif n == 2:
        print("---- Students Having Marks Greater Than 60 ----")
        print()

        for stu in students:
            if stu.marks > 60:
                stu.display()

    elif n == 3:
        highest = 0
        stuRoll = None

        for stu in students:
            if stu.marks > highest:
                highest = stu.marks
                stuRoll = stu.roll_no

        for stu in students:
            if stu.roll_no == stuRoll:
                print("---- Highest Marks Student ----")
                stu.display()
                break

    elif n == 4:
        total = 0

        for stu in students:
            total += stu.marks

        average = total / len(students)

        print("Average Marks:", average)

    elif n == 5:
        print("[ Exiting Program ]")
        break

    else:
        print("[ Enter a valid option ]")
        input("Press enter to continue...")
        continue