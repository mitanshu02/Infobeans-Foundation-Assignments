#28 Count occurrences of a word. S = "word word other word", Word = "word" 3

# s = input("Enter a string: ").split()
# word = input("Word : ")

# count = 0

# for w in s:
#     if w == word:
#         count += 1

# print(count)

#Approach 2:

s = input("Enter a string: ")
word = input("Word : ")

count = 0

for i in range(len(s) - len(word) + 1):
    match = True

    for j in range(len(word)):
        if s[i+j] != word[j]:
            match = False
            break

    if match:
        count += 1
        
print(f"{word} occured {count} times.")