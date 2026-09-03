#33 Find the longest word. S = "find the longest word" "longest"
s = input("Enter String: ").split()

print(max(s, key=len))