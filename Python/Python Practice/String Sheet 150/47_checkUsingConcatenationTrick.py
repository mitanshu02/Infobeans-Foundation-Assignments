# 47 Check for substring using concatenation trick. S1="CDAB", S2="ABCD" True (S1 is in S2+S2)

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

twiceS2 = s2 + s2

i = 0
while i < len(twiceS2):
    if twiceS2[i] == s1[0]:
        j = 0
        while j < len(s1):
            if twiceS2[i] != s1[j]:
                break
            j += 1
            i += 1
        else:
            print(True)
            break
    else:
        i += 1
else:
    print(False)