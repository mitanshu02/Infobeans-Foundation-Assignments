s = input("Enter string: ")

for i in range(len(s)-1,0,-1):
    if s[:i] == s[-i:]:
        print(s[:i])
        break
else:
    print("Not Found")