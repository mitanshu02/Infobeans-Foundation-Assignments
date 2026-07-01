"""
9.

 Bike Service Kilometer Checker


A bike needs service every 3000 km.


Write a program to:


- Read travelled kilometers

- Print every service checkpoint till entered km


Input:

10000


Output:

3000 6000 9000

"""
n = int(input("Input: "))

'''
cp = n//3000

for i in range(1,cp+1):
    print(i*3000,end = " ")
'''

for i in range(3000, n + 1, 3000):
    print(i,end = " ")