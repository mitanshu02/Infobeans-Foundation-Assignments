#27 Find the last occurrence of a word.

s = input("Enter String: ")
word = input("Enter word to search: ")

index = -1

for i in range(len(s) - len(word) + 1):
    match = True

    for j in range(len(word)):
        if s[i+j] != word[j]:
            match = False
            break

    if match:
        index = i
        
print(index)