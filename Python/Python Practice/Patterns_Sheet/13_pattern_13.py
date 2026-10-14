'''
1
01
101
0101
10101

'''

n = int(input("Enter n:"))

# Approach 1 

'''
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2 != 0 and j%2 != 0:
            print("1",end ="")
        elif i%2 == 0 and j%2 != 0:
            print("0",end = "")
        elif i%2 == 0 and j%2 == 0:
            print("1",end = "")
        else:
            print("0", end = "")
    print() 
'''

# Approach 2

for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j) % 2 == 0:
            print("1",end = "")
        else:
            print("0", end = "")
    print() 