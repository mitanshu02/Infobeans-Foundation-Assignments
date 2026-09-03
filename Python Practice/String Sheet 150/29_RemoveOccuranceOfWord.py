#29 Remove occurrences of a word. S = "a test b test c", Word = "test", Remove All "a b c"

s = input("Enter string: ")
word = input("Enter word: ")
new = ""
skip = 0
for i in range(len(s)):
    match = 1
    if skip > 0:
        skip -= 1
        continue

    for j in range(len(word)):
        if s[i+j] != word[j]:
            match = 0
            break

    if match:
        skip = len(word)-1
    else:
        new += s[i]

print(new)