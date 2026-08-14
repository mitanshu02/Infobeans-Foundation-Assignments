'''
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92

'''

from collections import namedtuple

student = namedtuple("student",["roll_no","name","course","marks"])

n = int(input("Enter number of students: "))

s = []

for i in range(n):
    roll = int(input(f"Enter roll no. of student {i+1}: "))
    name = input(f"Enter name of student {i+1}: ")
    course = input(f"Enter course of student {i+1}: ")
    marks = int(input(f"Enter marks of student {i+1}: "))
   
    std = student(roll,name,course,marks)
    s.append(std)
    print()

c = input("Enter course name: ")
print()

for std in s:
    print(std.roll_no,std.name,std.course,std.marks)

print()
highest = s[0].marks
above80 = 0
h_idx = 0
total = 0

for i in range(len(s)):
    total = total + s[i].marks
    if s[i].marks > highest:
        highest = s[i].marks
        h_idx = i
    if s[i].marks > 80:
        above80 += 1

print("Topper: ")
print(s[h_idx].roll_no,s[h_idx].name,s[h_idx].course,s[h_idx].marks)

print()

print("Students above 80: ")
print(above80)

print()

print("Average Marks: ")
print(total/n)

print()

print(f"Student in {c} course: ")
for std in s:
    if c == std.course:
        print(std.roll_no,std.name,std.course,std.marks)

