#50 Remove all digits. S = "a1b2c3" "abc"

s = input("Enter string: ")

ans = ""

for ch in s: 
    if '1'<=ch<='9':
        continue
    else:
        ans += ch
print(ans)