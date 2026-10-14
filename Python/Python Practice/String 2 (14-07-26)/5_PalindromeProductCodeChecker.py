'''
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code
'''

pc = input("Enter product code: ")
'''
if pc != pc[::-1]:
    print("Not a Palindrome Code")
else:
    print("Palindrome Code")
'''

l = len(pc)
for i in range(l//2):
    if pc[i] != pc[l-i-1]:
        print("Not a Plaindrome Code")
        break
else:
    print("Palindrome code") 