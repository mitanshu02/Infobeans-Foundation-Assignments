#46 Check if a substring appears at both the start and end. S = "abcabca", Sub="abca" TRUE

s = input("Enter String: ")

sub = input("Enter substring: ")

if s[:len(sub)] == sub and s[-len(sub):] == sub:
    print(True)
else:
    print(False)