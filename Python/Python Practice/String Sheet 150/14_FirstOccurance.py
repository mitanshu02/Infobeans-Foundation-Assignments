#14 Find the first occurrence of a character.

s = input("Enter string: ")
c = input("Enter Character: ")

for i in range(len(s)):
    if s[i] == c:
        print(i)
        break
