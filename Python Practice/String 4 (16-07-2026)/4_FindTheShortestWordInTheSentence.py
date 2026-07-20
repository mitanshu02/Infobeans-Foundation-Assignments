'''

4. Program should work for both uppercase and lowercase letters.

 Find the Shortest Word in a Sentence

Telecom SMS Cost Optimization System

A telecom company charges customers based on the length of words used in bulk SMS campaigns.

The company wants to identify the shortest word in every message for analytics purposes.

Write a Python program to find the shortest word from a given sentence.

Input:


Python is very easy to learn


Output:

is

'''

m = input("Input:")
l = len(m)
l1  = 0
smallest = 999
for i in range(l):
  ch = m[i]
  if ch != " ":
    
    if (i == 0 or m[i-1] == " ") and (i == l-1 or m[i+1] == " "):
        smallest = 1
        res = m[i]
    elif i == 0 or m[i-1] == " ":
        start = i
    elif i == l-1 or m[i+1] == " ":
        end = i
      
        w = m[start:end+1]
        l1 = len(w)
        
        if l1 < smallest:
            smallest = l1
            res = w

print(res)


'''
# better space complexity 

m = input("Input: ")
l = len(m)

smallest_len = l + 1
smallest_start = -1
smallest_end = -1

i = 0

while i < l:

    while i < l and m[i] == " ":
        i += 1

    if i == l:
        break

    start = i

    while i < l and m[i] != " ":
        i += 1

    end = i - 1

    length = end - start + 1

    if length < smallest_len:
        smallest_len = length
        smallest_start = start
        smallest_end = end

if smallest_start != -1:
    print("Output:", m[smallest_start:smallest_end + 1])
else:
    print("No words found.")

'''