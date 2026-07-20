'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8

'''

msg = input("Enter feedback message: ").lower()
count = 0
for ch in msg:
    if ch in "aeiou":
        count += 1

print(f"Total vowels: {count}")