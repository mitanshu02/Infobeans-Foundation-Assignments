#34 Find the Shortest word. S = "find the shortest word" "the"

s = input("Enter String: ").split()

print(min(s, key=len))