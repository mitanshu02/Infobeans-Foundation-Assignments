'''
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12

'''

n = input("Enter contact number: ")

count= 0
for ch in n:
    if '0'<=ch<='9':
        count+=1
  
print("Total Digits:",count)