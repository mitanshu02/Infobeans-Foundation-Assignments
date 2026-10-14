#42 Check if two strings are equal without equals(). S1 = "abc", S2 = "abc" TRUE

s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

if len(s1) != len(s2):
    print("False")
else:
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            print("False")
            break
    else:
        print("True")