a,b = map(int, input("Input: ").split(" "))

count =0

if a<b:
    for i in range(a,b+1):
        if i%5 == 0:
            count += 1
else:
    for i in range(a,b-1,-1):
        if i%5 == 0:
            count += 1

print("Count =",count)