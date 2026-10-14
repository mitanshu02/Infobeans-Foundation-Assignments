s = input("Enter string: ")
# print(s.lower())
p = ""
for ch in s:
    if 'A'<=ch<='Z':
        p += chr(ord(ch)+32)
    else:
        p += ch
print(p) 