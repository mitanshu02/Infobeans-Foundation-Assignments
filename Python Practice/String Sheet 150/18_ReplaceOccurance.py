#18 Replace occurrences of a character. S = "apple", Old='p', New='x', "axxle"

s = input("Enter string: ")
c = input("Enter old Character: ")
n = input("Enter new Character: ")
p =""
for i in range(len(s)):
    if s[i] != c:
        p += s[i]
    else:
        p += n
        

print(p)