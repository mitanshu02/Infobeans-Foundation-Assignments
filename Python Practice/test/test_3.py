m = input("Input: ")
n = m.split()
r = ""

i = len(n) - 1

while i>=0:
    w = n[i]
    w = w[::-1]
    r = r + w + " "
    i -= 1

m = r
print(m)
    
    
    
    
    
    
