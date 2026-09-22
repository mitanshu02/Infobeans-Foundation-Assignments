r = int(input("Enter rows no.: "))
c = int(input("Enter coloumn no.: "))

m = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    m.append(row)

print(m)

print("Original Matrix: ")
for row in m:
   print(*row)

print("Main Digonal Elements: ")
for i in range(r):
    for j in range(c):
        if i == j:
            print(m[i][j],end = " ")
print()

print("Secondary Digonal: ")
for i in range(r):
    for j in range(c):
        if (c-1)-i == j:
            print(m[i][j],end = " ")

print()
print("Transpose matrix: ")
t = []

for i in range(c):
    row = []
    for j in range(r):
        row.append(m[j][i])
    t.append(row)

for row in t:
    print(*row)


main = []
secondary = []

for i in range(c):
    for j in range(r):
        if i == j:
            main.append(t[i][j])

for i in range(c):
    for j in range(r):
        if (r-1)-i == j:
            secondary.append(t[i][j])

p = 0
q = 0
for i in range(c):
    for j in range(r):
        if i == j:
            t[i][j] = secondary[p]
            p += 1
        if (r-1)-i == j:
            t[i][j] = main[q]
            q += 1

print()
print("Final matrix after digonal swapping: ")

for row in t:
    print(*row)   
