#54 Replace duplicate chars with '$'. S = "hello" "he$lo"

s = input("Enter string: ")

ans = ""

for i in range(len(s)):
    if s[i] in s[:i]:
        ans += "$"
    else:
        ans += s[i] 

print(ans)