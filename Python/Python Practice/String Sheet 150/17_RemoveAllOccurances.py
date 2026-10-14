#17 Remove occurrences of a character. S = "banana", Char = 'a', Remove All ,"bnn"

s = input("Enter string: ")
c = input("Enter Character: ")
p =""
for i in range(len(s)):
    if s[i] != c:
        p += s[i]
        

print(p)