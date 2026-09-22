# 60 Append two strings but remove adjacent duplicates. S1="miss", S2="issippi" "misisipi"
s1 = input("Enter s1:")
s2 = input("Enter s2: ")

k = s1+s2
ans =""

i = 0
while i < len(k)-1:
    if k[i] == k[i+1]:
        ans += k[i]
        i += 1
    else:
        ans += k[i]

    if i == len(k)-2:
        if k[i] != k[i+1]:
            ans += k[i+1]

    i += 1

print(ans)
