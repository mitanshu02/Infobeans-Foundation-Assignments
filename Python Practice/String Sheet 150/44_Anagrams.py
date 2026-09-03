#44 Check if two strings are anagrams. S1 = "listen", S2 = "silent" TRUE

s1 = input("Enter First String: ")
s2 = input("Enter Second String:")

if len(s1) != len(s2):
    print("False")
else:
    chr_count = {}

    for c1,c2 in zip(s1,s2):
        chr_count[c1] = chr_count.get(c1,0)+1
        chr_count[c2] = chr_count.get(c2,0)-1

    print(all(count == 0 for count in chr_count.values()))