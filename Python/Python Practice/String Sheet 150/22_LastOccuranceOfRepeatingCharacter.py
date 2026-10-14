#22 Find the last repeating character. S = "abracadabra" r'

n = input("Enter : ")

for i in n:
    count = 0
    for j in n:
        if i == j:
            count += 1
    if count > 1:
        l = i

print(l)