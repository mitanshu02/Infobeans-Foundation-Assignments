#48 Remove all vowels. S = "aeiou XYZ" " XYZ"

s = input("Enter String: ")
ans = ""

for ch in s:
    if ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u':
        continue
    else:
        ans += ch
print(ans)
