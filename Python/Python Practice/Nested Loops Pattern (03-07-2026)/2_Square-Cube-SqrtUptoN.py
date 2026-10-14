'''
2_ WAP to print square, cube and sqrt of number upto n.

'''
n = int(input("Enter a number: "))

for i in range(1,n):
    print(f"For {i}:")
    print()
    print(f"Square of {i} is {i*i}") 
    print(f"Cube of {i} is {i**3}")
    print(f"Square root of {i} is {i**(1/2)}")
    print()   