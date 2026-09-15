"""
Assignment 1: Smart Street Lights (Fibonacci Series)

Write a recursive function to print the first N Fibonacci numbers.

Input:
Enter the number of months:
7

Output:
0 1 1 2 3 5 8
"""

def fabonacci(first = 0,second = 1,rem = 0):
    if rem == 0:
        return
    print(first, end = " ")
    next = first + second
    first = second
    second = next
    return fabonacci(first,second,rem-1)

fabonacci(0,1,7)

# def fibonacci(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(7))