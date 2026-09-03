#43 Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab" TRUE

s1 = input("Enter first String: ")
s2 = input("Enter second string: ")
s1copy = s1
new = ""

while s1 != new:
    new = s1copy[-1] + s1copy[:-1]

    if new == s2:
        print(True)
        break

    s1copy = new
else:
    print(False)