#35 Find the first palindrome word. S = "this madam is here" "madam"

s = input("Enter sentence: ").split()

for word in s:
    if word == word[::-1]:
        print(word)
        break
else:
    print("No Palindrome")