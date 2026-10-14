# 13 Get the Unicode code point before index.

s = input("Enter string: ")
idx = int(input("Enter index: "))
if idx > 0:
    print(ord(s[idx-1]))
else:
    print("Please enter a valid range.")
