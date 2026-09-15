"""
Assignment 3: Security PIN Verification (Palindrome Number)

Write a recursive function to reverse the given number and determine whether it is a palindrome.

Input:
Enter PIN:
1221

Output:
Palindrome Number

Input:
Enter PIN:
1234

Output:
Not a Palindrome Number
"""
def checkPalindrome(n):
    def reverse(n):
        if n == 0:
            return ""
        return str(n%10)+reverse(n//10)
    if int(reverse(n)) == n:
        return True
    else:
        return False

print(checkPalindrome(1222221))