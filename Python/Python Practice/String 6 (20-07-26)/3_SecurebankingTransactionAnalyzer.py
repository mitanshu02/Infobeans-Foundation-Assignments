'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8
'''

m = input("Input: ")
l = len(m)
visited = ""

for i in range(l):
    ch = m[i]
    if '0'<=ch<='9':
        if ch not in visited:
            for j in range(i+1,l):
                if m[j] == ch:   
                    break    
            else:
                print("Output:",ch)
                break
            visited = visited + ch

else:
    print("No Unique Digit Found")


