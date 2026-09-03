# 30 Replace a word with another word. S = "old data", Old="old", New="new" "new data"

s = input("Enter string: ")
old_word = input("Enter old word: ")
new_word = input("Enter new word: ")
new = ""
skip = 0

for i in range(len(s)):
    match = 1
    if skip > 0:
            skip -= 1
            continue
    
    for j in range(len(old_word)):
        if s[i+j] != old_word[j]:
            match = 0
            break

    if match:
        new += new_word
        skip = len(old_word)-1
    else:
        new += s[i]

print(new)