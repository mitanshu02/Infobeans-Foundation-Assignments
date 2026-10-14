'''
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good Enter character to check: o

Output: Character 'o' occurs: 4 times

'''
inp = input("Enter product review: ")
c = input("Enter character too check: ")
count = 0
for ch in inp:
    if ch == c:
        count += 1

print(f"Character '{c}' occurs: {count} times")