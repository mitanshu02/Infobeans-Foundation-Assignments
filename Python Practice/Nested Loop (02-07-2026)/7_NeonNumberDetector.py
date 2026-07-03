'''

7.
Neon Number Detector

Scenario:
A smart calculator system checks special numbers used in mathematical testing.
The user enters a range of numbers.
The system identifies all Neon Numbers using nested loops.

Theory:
A Neon Number is a number where the sum of digits of its square is equal to the original number.

Example:
9

Square of 9 = 81

8 + 1 = 9

Since the sum is equal to the original number, 9 is called a Neon Number.

Input:
Enter starting number: 1
Enter ending number: 100

Output:
Neon Numbers are:
1
9

'''

s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

print("Neon Numbers are:")

for n in range(s,e+1):
    sq = n*n
    total = 0
    while sq>0:
        total = total + sq%10
        sq = sq//10
    if total == n:
        print(n)
    