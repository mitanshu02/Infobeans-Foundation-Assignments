'''
# 5. Social Media Hashtag Trend Window

A social media company wants to analyze the smallest substring containing all unique characters from a hashtag.

### Input:

text
aabcbcdbca

### Output:

text
dbca

### Explanation:

dbca contains all unique characters: a,b,c,d
'''

m = input("Input: ")
ans = m
unique = ""
for ch in m:
    if ch not in unique:
        unique += ch
lu = len(unique)
# print(unique)

for i in range(len(m)):
    for j in range(i+lu,len(m)+1):
        sub=m[i:j]
        for ch in unique:
            if ch not in sub:
                break
        else:
            if len(sub)<len(ans):
                ans = sub
            

print(ans)


































'''
n=input("Enter : ")
ans=""

for i  in range(len(n)):
    temp=""
    for j in range(i,len(n)):
        if n[j]  in temp:
            
            break
        else :
            temp+=n[j]

    if len(temp)>=len(ans):
        ans=temp
    
print(ans)

'''
