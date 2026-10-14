s = input("Enter String: ")
p =""
for ch in s:
    if 'A'<=ch<='Z':
        p += chr(ord(ch)+32)
    elif 'a'<=ch<='z':
        p += chr(ord(ch)-32)
    else:
        p += ch

print(p)