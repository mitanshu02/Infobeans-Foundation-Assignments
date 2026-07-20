'''
1. WAP to print the sum of all the numbers between 100 and 200 which are divisible by 9.

'''
total = 0
for i in range(100,201):
    if i % 9 == 0:
        total = total + i
print(total)