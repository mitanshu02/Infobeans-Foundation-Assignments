#57 Merge two strings alternatively. S1 = "ABC", S2 = "def" "AdBeCf"

s1 = input("Enter String: ")
s2 = input("Enter String: ")

ans = ""

takeFromS1 = True 
j = 0
k = 0
for i in range(len(s1)+len(s2)):
    if takeFromS1:
        ans += s1[j]
        j += 1
        takeFromS1 = False
    else:
        ans += s2[k]
        k += 1
        takeFromS1 = True
print(ans)