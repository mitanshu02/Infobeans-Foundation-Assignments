'''
3.  Smart Chat Message Cleaner

A social media company noticed that users often enter messages with
unnecessary spaces. To improve readability and storage efficiency, the
system should remove extra spaces and keep only a single space between
words.

Input: Enter message: Java is easy

Output: Cleaned Message: Java is easy
'''
msg = input("Enter message: ")

l = len(msg)
firstWord = False
cleaned = ""

for i in range(l):
    ch = msg[i]
    if ch == " ":
        continue
    elif i == 0:
        cleaned = cleaned + ch
        firstWord = True
    elif msg[i-1] == " ":
        if firstWord == False:
            cleaned += ch
            firstWord = True
        else:
            cleaned += " "
            cleaned += ch
    else:
        cleaned += ch
print(cleaned)  


'''
# Note

Idea: Instead of processing spaces, process words. A word starts when a non-space character appears after the beginning of the string or after one or more spaces.

1. Traverse the input string character by character from left to right.
2. Ignore every space character. This automatically removes leading, trailing, and multiple consecutive spaces.
3.Identify the start of a new word. A new word begins when:
    -> it is the first character of the string, or
    -> the previous character is a space.
4. For the first word, append its characters directly to the cleaned string without adding any space before it.
5. For every subsequent word, first append a single space, then append the word's characters.
6. Continue until the end of the string. The final string will contain no leading or trailing spaces and exactly one space between consecutive words.

'''

# Don't try to remove extra spaces. Instead, identify where each new word starts and decide # whether a space should be inserted before that word.
