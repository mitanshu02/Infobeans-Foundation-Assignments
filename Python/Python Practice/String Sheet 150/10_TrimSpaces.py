#Trim leading, trailing, or extra spaces.

s = input("Enter String: ")
p = ""
for i in range(len(s)):
    if i == 0:
        if s[i] == " ":
            continue
        else:
            p += s[i]
    elif i == len(s)-1:
        if s[i] != " ":
            p += s[i]
    else:        
        if s[i+1] != " ":
            p += s[i]
        else:
            if s[i] != " ":
                p += s[i]

print(p)