#53 Remove punctuation. S = "Hello, world!" "Hello world"

s = input("Enter String: ")

ans = "" 

for ch in s:
    if ch == "," or ch == "." or ch == ";" or ch == ":" or ch == "?" or ch == "!":
        continue
    else:
        ans += ch
print(ans)