'''
7.
=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi

---
'''
n = int(input("Enter number of students: "))

d = {}

for i in range(n):
    print(f"Enter details of student {i+1}:")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    d[name] = marks
    print()

print("Passed Students: ")
for name,marks in d.items():
    if marks >= 50:
        print(name)