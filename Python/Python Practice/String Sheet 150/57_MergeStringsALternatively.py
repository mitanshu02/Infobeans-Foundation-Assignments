#57 Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"

s1 = input("Enter String: ")
s2 = input("Enter String: ")

ans = ""

takeFromS1 = True 
j = 0
k = 0
while j<len(s1) or k<len(s2):
    if j < len(s1) and k<len(s2):
        if takeFromS1:
            ans += s1[j]
            j += 1
            takeFromS1 = False
        else:
            ans += s2[k]
            k += 1
            takeFromS1 = True
    elif j<len(s1):
        ans += s1[j]
        j += 1
    else:
        ans += s1[k]
        k += 1

print(ans)