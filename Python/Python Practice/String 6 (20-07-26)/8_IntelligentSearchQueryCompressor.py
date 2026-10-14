'''
# 8. Intelligent Search Query Compressor

A search engine company wants to compress user queries.

## Rules:

* Count frequency of each character
* Display characters in sorted order
* Ignore spaces
* Case insensitive

### Input:

text
Google Search


### Output:

text
a1c1e2g2h1l1o2r1s1t1
'''

m = input("Input: ")

m = m.replace(" ","").lower().replace(""," ")
m = m.split()
m = sorted(m)
ans = []
count = 1
for i in range(len(m)):
    if i<len(m)-1 and m[i] == m[i+1]:
        count += 1 

    elif i == len(m)-1:
        if m[i] == m[i-1]:
            continue
        else:
            ans.append(f"{m[i]}1")
    else:
        ans.append(f"{m[i]}{count}")
        count = 1

print("".join(ans))
