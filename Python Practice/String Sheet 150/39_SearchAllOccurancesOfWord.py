#39 Search all occurrences of a character. S = "banana", Char='a' 1, 3, 5 (indices)

s = input("Enter String: ")
ch = input("Enter character to search for : ")

for i in range(len(s)):
    if s[i] == ch:
        print(i,end = " ")
