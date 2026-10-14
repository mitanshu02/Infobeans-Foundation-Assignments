#45 Check whether a string starts/ends with another string. S = "apple pie", Prefix = "apple", Suffix = "pie" Start: True, End: True

s = input("Enter string: ").strip()
start = input("Enter prefix: ")
end = input("Enter suffix: ")

prefix = True
suffix = True

for i in range(len(start)):
    if s[i] != start[i]:
        prefix = False
        break

for i in range(len(end)):
    if end[i] != s[len(s)-len(end)+i]:
        suffix = False
        break

print(f"Start = {prefix}, End = {suffix}")

