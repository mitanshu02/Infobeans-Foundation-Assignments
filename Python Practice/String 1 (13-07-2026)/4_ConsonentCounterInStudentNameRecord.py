'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U

'''
print(chr(65))
inp = input("Enter student name: ").upper()
count = 0
for ch in inp:
    if 'A'<= ch <= 'Z' and ch not in 'AEIOU':
        count += 1

print(f"Total consonents: {count}")
    