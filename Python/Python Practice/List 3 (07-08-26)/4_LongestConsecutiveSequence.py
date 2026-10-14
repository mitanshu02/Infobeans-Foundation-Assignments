'''
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3

'''
n = int(input("Enter n: "))

elem = [int(x) for x in input("Input: ").split()]

elem.sort()
seqStarted = False
count = 0
longest = 0
for i in range(len(elem)):
    if i < len(elem)-1:
        if seqStarted == False:
            if elem[i] + 1 == elem[i+1]:
                count += 1
                seqStarted = True
        else:
            if elem[i] + 1 == elem[i+1]:
                count += 1
            else:
                count += 1
                seqStarted = False
                if count>longest:
                    longest = count
                count = 0
    else:
        if elem[i]-1 == elem[i-1] and seqStarted == True:
            count += 1
            seqStarted = False
            if count > longest:
                longest = count 
print(f"Longest Consecutive Length ={longest}")

#Correct if no duplicate numbers in the list
    