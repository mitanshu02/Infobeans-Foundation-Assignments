'''
1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3
'''
l = int(input("Enter l: "))
marks = []

for i in range(l):
    item = int(input(f"Enter marks of sub {i+1}: "))
    marks.append(item)

print("Marks are: ",marks)

lowest = marks[0]
highest = marks[0]

count = 0
for m in marks:
    if m > 75:
        count += 1
    if m < lowest:
        lowest = m
    elif m > highest:
        highest = m

print("Lowest Marks are: ",lowest)
print("Highest Marks are: ",highest)  
print("Number of Students who scored above 75 are : ",count)  

