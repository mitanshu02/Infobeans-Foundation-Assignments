s= input("s = ")
t = input("t = ")

visited = ""
a1 = []
a2 = []

for ch in s:
    if ch not in visited:
        a1.append(s.count(ch))
    visited += ch
print(a1)
visited = ""
for ch in t:
    if ch not in visited:
        a2.append(t.count(ch))
    visited += ch
print(a2)
if sorted(a1) == sorted(a2):
    print("true")
else:
    print("false")
