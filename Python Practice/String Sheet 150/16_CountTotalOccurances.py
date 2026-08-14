# 16 Count total occurrences of a character. S = "programming", Char = 'g' , 2

s = input("Enter string: ")
c = input("Enter Character: ")

count = 0
for i in range(len(s)):
    if s[i] == c:
        count += 1

print(count)