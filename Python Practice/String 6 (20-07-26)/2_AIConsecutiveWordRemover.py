'''
# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started
'''

m = input("Input: ")
l = len(m)
m = m.split()
answer = []

for w1 in m:
    if w1 not in answer:
        answer.append(w1)
    else:
        continue

print(" ".join(answer))



