n = int(input("Input: "))
temp = n

rev = 0

while n>0:
    rev = rev*10 + n%10
    n = n//10

if rev == temp:
    print("Output: Palindrome")
else:
    print("Output:Not a Palindrome")