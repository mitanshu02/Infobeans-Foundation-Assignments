s = input("Enter string: ")
# print(s.upper())
p = ""
for ch in s:
    if 'a'<=ch<='z':
        p += chr(ord(ch)-32)
    else:
        p += ch
print(p) 