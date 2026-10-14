n = int(input("Input: "))
temp = n

rev = 0

for i in range(len(str(n))):
    rev = rev*10 + n%10
    n = n//10

if rev == temp:
    print("Output: Palindrome")
else:
    print("Output:Not a Palindrome")