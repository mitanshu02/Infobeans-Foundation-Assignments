'''
# 4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

### Input:

text
file file image file image data


### Output:

text
file file(1) image file(2) image(1) data
'''

m = input("Input: ")
l = len(m)
m = m.split()
visited = []
ans = []
for w in m:
    if w not in visited:
        visited.append(w)
        ans.append(w)
    else:
        visited.append(w)
        c = visited.count(w)-1
        wModified = w + f"({c})"
        ans.append(wModified)

print(" ".join(ans))
