#23 Print all characters that occur exactly twice. S = "aabbcdee" b', 'e'

n = input("Enter string: ")
visited = ""

for i in n:
    if i not in visited:
        c = 0
        for j in n:
            if i == j:
                c+=1
        if c == 2:
            print(i,end = " ") 
        visited += i