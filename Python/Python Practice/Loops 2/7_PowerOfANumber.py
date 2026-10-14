n,p = map(int,input("Input n and p: ").split(" "))

ans = 1
for i in range(p):
    ans = ans*n

print("Output:",ans)