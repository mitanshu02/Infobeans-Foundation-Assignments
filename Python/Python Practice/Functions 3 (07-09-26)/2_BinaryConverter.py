"""
Assignment 2: Binary Converter for Embedded System

Write a recursive function to convert a decimal number into its binary representation.

Do not use Python's built-in bin() function.

Input:
Enter a decimal number:
25

Output:
Binary Number = 11001
"""

def decimalToBinary(n):
    if n < 2:
        if n == 0:
            return '0'
        return '1'
    return decimalToBinary(n//2)+str(n%2)

print(decimalToBinary(25))