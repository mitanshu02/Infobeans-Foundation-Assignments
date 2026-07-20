'''
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP

'''
m = input("Input: ")

m = m.split()
res = ""
result = ""
for w in m:
    res = w[::-1]
    result = res + " " + result
m = result
   
print(m)
        
     


'''
m = input("Input:")

m = m.split("")

m = m[::-1]

print(m)

'''
