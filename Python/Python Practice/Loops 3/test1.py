n = input("Input: ")

l = len(n)

fd = int(n) // (10**(l-1))

if fd != 0 and '0' in n:
    print("Duck Number")
else:
    print("Not a duck number") 


