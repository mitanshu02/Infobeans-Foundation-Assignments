#32 Count frequency of each word. S = "apple banana apple" apple: 2, banana: 1

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

visited = set()

for w1 in words:
    if w1 not in visited:
        count = 0
        for w2 in words:
            if w1 == w2:
                count += 1
        print(f"{w1} : {count}")
    visited.add(w1)  

