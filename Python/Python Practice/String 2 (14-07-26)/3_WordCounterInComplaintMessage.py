'''
3.
Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5

'''
#Approach 0

m = input("Enter complaint: ")

print("Total words:",len(m.split()))

'''

#Approach 1

m = input("Enter complaint: ")
l = len(m)
count = 0

for i in range(l):
    ch = m[i]
    if ('a'<=ch<='z' or 'A'<=ch<='Z') and (i == 0 or m[i-1] == " "):
        count += 1

print("Total words:",count)

'''

'''
first = 0
last = 0
for i in range(l):
    ch = m[i]
    if ch != " ":
        first = i
        break
        
for i in range(-1,-l-1,-1):
    ch = m[i]
    if ch != " ":
        last = l+i
        break

s = m[first:last+1]
 
count = 0

for i in range(len(s)):
    ch = s[i]
    if (i == 0 and ('A'<=ch<='Z' or 'a'<=ch<='z'))or (('A'<=ch<='Z' or 'a'<=ch<='z') and  s[i-1] == " "):
        count += 1

print("Total words:",count)

'''
'''
📝 Revision Notes: Count Number of Words in a String

🥇 Approach 1: Count Spaces

Logic

	Words = Spaces + 1

Code Idea
for ch in s:
    if ch == " ":
        count += 1

print(count + 1)

✅ Advantages

Very simple
Works for normal sentences

❌ Limitations

Fails when:

Hello   World

or

   Hello World

or

Hello World   

Reason:

Assumes exactly one space between every pair of words.

🥈 Approach 2: Manual strip() + Count Word Starts

Logic

First remove

leading spaces
trailing spaces

Then count

Current character is a letter

AND

Previous character is a space

Handle first word separately.

Manual strip()

Find

First non-space index

Find

Last non-space index

Then

s = s[first:last+1]
Word Rule
(i==0 AND current is letter)

OR

(current is letter AND previous is space)

✅ Advantages

Works for

Hello   World
   Hello World
Hello World

❌ Limitation

Extra work.

Need:

two additional traversals
new substring

🥇🥇 Final Approach (Best)
Main Observation ⭐

Forget spaces.

Ask

When does a word begin?

Answer

A word begins when

Current character is a letter

AND

(
    first character

    OR

    previous character is a space
)
Final Rule
Letter

AND

(i==0 OR previous is space)
Advantages

✅ One traversal

✅ No strip()

✅ No substring

✅ No extra variables

✅ Handles

Hello
Hello World
Hello   World
   Hello World
Hello World

⭐ Biggest Lesson Learned

Initially I was counting spaces.

Finally I started counting word beginnings.

This is a much stronger way of thinking because it focuses on the event instead of an indirect measure.

🧠 General Principle (Worth Remembering)

Whenever you have to count something, don't ask:

"What is related to it?"

Ask:

"When does it occur?"

For this problem:

❌ Count spaces.
✅ Count the start of each word.

This principle appears again in many topics:

counting islands in grids,
counting connected components,
counting subarrays,
detecting new groups,
parsing strings.

'''