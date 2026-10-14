'''
123456789
 1234567
  12345
   123
    1
'''

n = int(input("Enter n:"))

i = 1
while i <= n:
    j = 1
    while j < i:
        print(" ", end = "")
        j += 1
    
    j = 1
    while j <= 2*(n-i)+1:
        print(j,end = "")
        j += 1
    print()
    i += 1