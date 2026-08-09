
s = input("s = ")

c = 0
count = 0
for ch in s:
    if ch == '0':
        c += 1
    else:
        c -= 1
    if c == 0:
        count += 1
        print(count)

# if count != 0:
#     return count
# else:
#     return -1