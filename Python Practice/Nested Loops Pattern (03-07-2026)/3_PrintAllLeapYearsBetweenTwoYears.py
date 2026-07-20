'''
3. WAP to print all the leap years between two years
'''

s = int(input("Enter starting year: "))
e = int(input("Enter ending year: "))

print()
for y in range(s,e+1):
    if y%4 == 0 or y%100 != 0 and y%400 == 0:
        print(y, end = " ")
          