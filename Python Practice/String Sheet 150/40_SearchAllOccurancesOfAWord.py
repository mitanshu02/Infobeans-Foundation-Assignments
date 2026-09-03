#40 Search all occurrences of a word. S = "a b a b", Word='b' 2, 6 (start indices)

s = input("Enter string: ")
w = input("Enter word: ")
i = 0
while i < len(s):
    if s[i] == w[0]:
        j = 0
        while j < len(w):
            if s[i] != w[j]:
                break
            i += 1
            j += 1
        else:
            print(i-len(w))
    else:
        i += 1