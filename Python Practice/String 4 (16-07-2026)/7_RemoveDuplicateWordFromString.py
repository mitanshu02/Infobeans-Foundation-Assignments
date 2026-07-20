'''
7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.

``
hello hello how are are you


Output:


hello how are you
'''

m = input("Input Sentence: ")
l = len(m)

finalString = ""

for i in range(l):
    ch = m[i]

    if ch != " ":

        if (i == 0 or m[i-1] == " ") and (i == l-1 or m[i+1] == " "):
            res = m[i]

        elif i == 0 or m[i-1] == " ":
            start = i
            continue

        elif i == l-1 or m[i+1] == " ":
            end = i
            res = m[start:end+1]

        else:
            continue

        # Search res inside finalString

        found = False
        lf = len(finalString)

        for j in range(lf):

            ch2 = finalString[j]

            if ch2 != " ":

                if (j == 0 or finalString[j-1] == " ") and (j == lf-1 or finalString[j+1] == " "):
                    temp = finalString[j]

                elif j == 0 or finalString[j-1] == " ":
                    s = j
                    continue

                elif j == lf-1 or finalString[j+1] == " ":
                    e = j
                    temp = finalString[s:e+1]

                else:
                    continue

                if temp == res:
                    found = True
                    break

        if not found:

            if finalString == "":
                finalString += res
            else:
                finalString += " " + res

print("Output:",finalString)