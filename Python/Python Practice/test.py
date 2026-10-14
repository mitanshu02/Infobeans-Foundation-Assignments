s = input("Enter the string: ")

ans = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]

        if sub in s[j:]:
            if len(sub) > len(ans):
                ans = sub

print(ans)