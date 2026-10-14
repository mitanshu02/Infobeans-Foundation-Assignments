#52 Remove all special characters. S = "a!@b#c" "abc"

s = input("Em=nter string: ")
ans = ""

for ch in s:
    if 'a'<=ch<='z' or 'A'<=ch<='Z' or '0'<=ch<='9':
        ans += ch

print(ans)