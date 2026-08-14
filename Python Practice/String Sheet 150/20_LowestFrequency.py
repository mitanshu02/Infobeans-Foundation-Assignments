#20 Find the lowest frequency character. S = "aabbcde" c', 'd', 'e' (any one or all)

s = input("Enter string: ")
lowest = len(s)
ch = ""
for i in range(len(s)):
    c = 0
    for j in range(i,len(s)):
        if s[i] == s[j]:
            c += 1
    if c < lowest:
        lowest = c
        ch = s[i]

print(ch) 