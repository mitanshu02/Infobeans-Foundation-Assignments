#49 Replace all consonants with '*' (Example suggests replacing non-vowels). S = "apple" "a***e" (or similar output depending on implementation)

s = input("Enter String: ")
ans = ""

for ch in s:
    if ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u':
        ans += ch
    else:
        ans += "*"

print(ans)