# 41 Check if a string contains a substring (without using built-in method). S1 = "Hello", Sub="ell" TRUE

s = input("Enter string: ")
w = input("Enter substring: ")
i = 0
while i < len(s):
    if s[i] == w[0]:
        j = 0
        while j < len(w):
            if s[i] != w[j]:
                break
            i += 1
            j += 1
        else:
            print("True")
            break
    else:
        i += 1
else:
    print("False")