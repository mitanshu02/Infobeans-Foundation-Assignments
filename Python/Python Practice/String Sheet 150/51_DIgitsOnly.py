#51 Extract only digits. S = "a1b2c3" "123"

s = input("Enter Sting: ")

ans = ""

for ch in s: 
    if '1'<=ch<='9':
        ans += ch

print(ans)

