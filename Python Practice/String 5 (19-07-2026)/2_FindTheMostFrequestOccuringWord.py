'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india

'''
m = input("Input: ")
l = len(m)

mostFrequent = 0
mostFrequentWord = ""
word1 = ""
word2 = ""
visited = ""

for i in range(l):
    ch = m[i]
    if ch!= " ":
        if (i == 0 or m[i-1] == " ") and (i == l-1 or m[i+1] == " "):
            word1 = m[i]
        elif i == 0 or m[i-1] == " ":
            start = i
        elif i == l-1 or m[i+1] == " ":
            end = i
            word1 = m[start:end+1]
            
            if word1 not in visited:
                visited = visited + word1 + " "
                count = 0
                for j in range(l):
                    if (j == 0 or m[j-1] == " ") and (j == l-1 or m[j+1] == " "):
                        word2 = m[j]
                        if word1 == word2:
                            count +=1 

                    elif j == 0 or m[j-1] == " ":
                        start = j
                    elif j == l-1 or m[j+1] == " ":
                        end = j
                        word2 = m[start:end+1]

                        if word1 == word2:
                            count +=1
        
                    if count > mostFrequent:
                        mostFrequent = count
                        mostFrequentWord = word1
            

print(mostFrequentWord)