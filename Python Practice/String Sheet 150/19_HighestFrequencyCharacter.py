#19 Find the highest frequency character. S = "abracadabra", a

s = input("Enter string: ")
maximum = 0
ch = ""
for i in range(len(s)):
    c = 0
    for j in range(i,len(s)):
        if s[i] == s[j]:
            c += 1
    if c > maximum:
        maximum = c
        ch = s[i]

print(ch) 