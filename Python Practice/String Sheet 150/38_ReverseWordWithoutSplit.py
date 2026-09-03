#38 Reverse words without split(). S = "are boss cute" "cute boss are"

s = input("Enter String: ")
word = ""
words = []

for ch in s:
    if ch != " ":
        word += ch
    else:
        if word != "":
            words.append(word)
            word = ""

if word != "":
    words.append(word)

result = ""

for i in range(len(words)-1,-1,-1):
    result += words[i] + " "

print(result)

    
