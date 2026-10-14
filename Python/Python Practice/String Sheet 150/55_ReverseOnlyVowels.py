#55 Reverse only vowels. S = "hello" "holle"

s = input("Enter String: ")
ans  = ""
i = 0
j = len(s)-1

while i < len(s):
    if s[i] in 'aeiouAEIOU':
        while j >= 0:
            if s[j] in 'aeiouAEIOU':
                ans += s[j]
                j -= 1
                break
            j -= 1
    else:
        ans += s[i]
    i += 1

print(ans)
 

