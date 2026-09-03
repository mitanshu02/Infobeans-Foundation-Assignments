#37 Reverse each word. S = "cat dog" "tac god"

s = input("Enter String: ").split()
ans = []
for w in s:
    ans.append(w[::-1])

print(" ".join(ans))