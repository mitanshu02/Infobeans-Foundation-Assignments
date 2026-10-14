'''
4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---
'''
n = int(input("Enter number of students: "))

d = {}

for i in range(n):
    print(f"Enter details of student {i+1}:")
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    d[name] = marks
    print()

highest = 0
lowest = 100
HighestName = ""
LowestName = ""
for name,marks in d.items():
    if marks > highest:
        highest = marks
        HighestName = name
    if marks < lowest :
        lowest = marks
        LowestName = name

print("Highest Marks: ",HighestName,d[HighestName])
print("Lowest Marks: ",LowestName,d[LowestName])
