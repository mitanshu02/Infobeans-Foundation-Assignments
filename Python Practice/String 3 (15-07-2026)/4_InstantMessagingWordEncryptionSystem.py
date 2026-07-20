'''
4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop

'''
m = input("Enter message: ")

l = len(m)

wordStarted = False
res = ""
for i in range(l):
    ch = m[i]

    if ch != " " and wordStarted == False:
        end = i
        wordStarted = True

    elif ch != " " and (i == l-1 or m[i+1] == " "):
        start = i
        for j in range(start,end-1,-1):
            letter = m[j]
            res = res + letter
        start = 0
        end = 0
        wordStarted = False

    elif ch == " ":
        res = res + ch

print(res)