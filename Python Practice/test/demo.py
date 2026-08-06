
s = input("s = ")
temp = ""
length = 0
largest = 0
for i in range(len(s)):
    for j in range(i,len(s)):
        if s[j] not in temp:
            temp+= s[j]
        else:
            print(temp)
            length = len(temp)
            if length >= largest:
                largest = length
            temp = ""
            break