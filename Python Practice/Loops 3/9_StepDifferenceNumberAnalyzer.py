"""
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number

"""

n = int(input("Input: "))
temp = n

r = 0 

while n>0:
    r = r*10 + n%10
    n = n//10

sum = 0
largest = 0
print("Step Difference:", end = " ")

for i in range(1,len(str(temp))):
    sd = 0
    d1 = r%10
    r = r//10
    d2 = r%10

    if d1 > d2:
        sd = d1 - d2
    elif d1 < d2:
        sd = d2 - d1
    else:
        sd = 0
    
    print(sd,end = " ")
    sum = sum + sd

    if sd > largest:
        largest = sd 

   

print("\nSum =",sum)
print("Largest =",largest)

if sum % len(str(temp)) == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")

    

    
    