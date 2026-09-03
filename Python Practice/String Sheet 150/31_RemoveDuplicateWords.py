#31 Remove duplicate words. S = "the cat and the dog" "the cat and dog"

s = input("Enter string: ")
wordStarted = False
word = ""
seen = set()
ans = ""

for i in range(len(s)):
    if s[i] != " ":
        if wordStarted == False:
            wordStarted = True 
        elif i == len(s) - 1:
            word += s[i]
            if word not in seen:
                ans += word 
                word = ""
        word += s[i]
    else:
        if wordStarted == True:
            wordStarted = False
            if word not in seen:
                ans += word
                ans += " "
                seen.add(word)
                word = ""
            else:
                word = ""     
        else:
            ans += s[i]

print(ans)