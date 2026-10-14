#15 Find the last occurrence of a character.

s = input("Enter string: ")
c = input("Enter Character: ")

for i in range(len(s)-1,-1,-1):
    if s[i] == c:
        print(i)
        break