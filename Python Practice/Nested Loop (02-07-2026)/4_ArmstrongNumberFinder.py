#problem in output

'''
4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407

'''


s = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

print("Armstrong Numbers are:")

while s <= e:
    n = s
    total = 0
    l = len(str(n))
    
    while n>0:
        total = total + (n%10)**l
        n = n//10
    if total == s:
        print(s)
    s = s+1