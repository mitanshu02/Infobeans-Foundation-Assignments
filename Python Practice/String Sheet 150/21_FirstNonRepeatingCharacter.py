#21 Find the first non-repeating character. S = "aabbcde" c'

s = input("Enter a string: ")

for i in s:
    if s.count(i) < 2:
        print(i)
        break