'''
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching

'''
# manual way 

first = input("Enter first product code: ").lower()
second = input("Enter second product code: ").lower()

l1 = len(first)
l2 = len(second)

for i in range(l1):
    ch = first[i]

    c1 = 0
    c2 = 0
    for j in range(l1):
        if first[j] == ch:
            c1 += 1
    
    for j in range(l2):
        if second[j] == ch:
            c2 += 1
    
    if c1 != c2:
        print("Both Product codes are not matching")
        break
else:
    print("Both Product Codes are Matching")
    
    
        



'''
# using methods: 
first = input("Enter first product code: ").lower().replace(" ", "")
second = input("Enter second product code: ").lower().replace(" ", "")

if sorted(first) == sorted(second):
    print("Both Product Codes are Matching")
else:
    print("Product Codes are Not Matching")

'''