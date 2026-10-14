#26 Find the first occurrence of a word. S = "Test this test", Word = "test" 10 (index)

# Approach 1: O(nm), n-> length of s, m -> length of word

s = input("Enter String: ")
word = input("Enter word to search: ")

for i in range(len(s)-len(word)+1):
    if s[i] == word[0]:
        if s[i:i+len(word)] == word:
            print(i)
            break

#Approach 2: O(nm)

# for i in range(len(s) - len(word) + 1):
#     match = True

#     for j in range(len(word)):
#         if s[i+j] != word[j]:
#             match = False
#             break

#     if match:
#         print(i)
#         break